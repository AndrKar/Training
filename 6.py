if True:
    print('Conditional was True')

language = 'Python'
language = 'Java'
if language == 'Python':
    print('The language is Python')
elif language == 'Java':
    print('The language is {0}'.format(language))
else:
    print('No match')
user = 'Admin'
logged_in = True
logged_in = False
if user == 'Admin' and not logged_in:
    print('Admin\'s page')
elif user == 'Admin' or logged_in:
    print('Page loaded')
else:
    print('Bad Creds')
