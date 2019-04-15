import json

""" Program to read from a .json file and write it back in pretty print format."""
filename = 'gdp_json.json'
with open(filename, 'r+') as outfile:
    # Loads the json string into a Python dictionary called dictdump
    dictdump = json.loads(outfile.read())
    # Start at the beginning of the file (Prevent appending)
    outfile.seek(0)
    # Write Python dictionary called dictdump to filename with indents at 4 spaces
    json.dump(dictdump, outfile, indent=4)
    # Get rid of extra spaces/characters
    outfile.truncate()