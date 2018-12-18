# 8.13 Python Crash Course
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

user_profile = build_profile('ben', 'kixmiller', location='des moines', field='programmer',
                            college='iowa state', football_team='denver broncos')
print(user_profile)
