"""
You have a list of email addresses.
Extract the usernames (part before @) from each email.

Expected output:
['alice', 'bob', 'carol']
"""

emails = ['alice@gmail.com', 'bob@knust.com', 'carol@dev.net']

usernames = [email.split("@")[0] for email in emails]
print(usernames)


usernames = []
p = 0
for email in emails:
    user = email.split('@')[0]
    usernames.insert(p, user)
    p += 1
print(usernames)