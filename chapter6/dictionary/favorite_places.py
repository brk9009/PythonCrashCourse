#6.9 Python Crash Course
favorte_places = {
    'ben': ['new york', 'denver'],
    'julie': ['denver'],
    'bob': ['kansas city'],
}

for name, places in favorte_places.items():
    print(name.title() + "'s favorite places are ")
    for place in places:
        print("\t" + place.title())
