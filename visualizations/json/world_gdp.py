import json

import pygal
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code

# Load the data into a list.
filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Print the 2016 gdp for each country.
gdp_populations = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        gdp_value = float(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            gdp_populations[code] = gdp_value

# Group the countries into 3 population levels.
gdp_pops_1,gdp_pops_2,gdp_pops_3= {}, {}, {}
for cc, gdp in gdp_populations.items():
    if gdp < 100000000000:
        gdp_pops_1[cc] = gdp
    elif gdp < 10000000000000:
        gdp_pops_2[cc] = gdp
    else:
        gdp_pops_3[cc] = gdp

# See how many countries are in each level.
print(len(gdp_pops_1), len(gdp_pops_2), len(gdp_pops_3))

wm_style = RotateStyle('#FF0000', base_style=LightColorizedStyle)   
wm = World(style=wm_style)
wm.title = 'World GDP in 2016, by Country'
wm.add('0-100bn', gdp_pops_1)
wm.add('100bn-10tn', gdp_pops_2)
wm.add('>10tn', gdp_pops_3)

wm.render_to_file('world_gdp.svg')

