import difflib

contacts = ['franz','wilfredo','elena','toño', 'gianpaul', 'chino', 'stephano']

def match(text):
    best = difflib.get_close_matches(text, contacts)
    try:
        return best[0].capitalize()
    except:
        return 'None'

# print(match('fran'))

