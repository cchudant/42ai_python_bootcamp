from random import shuffle

def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""

    ite = text.split(sep)
    if option == 'unique':
        ite = set(ite)
    elif option == 'shuffle':
        shuffle(ite)
    elif option == 'ordered':
        ite = sorted(ite, key=str.lower)

    print(ite)
    for el in ite:
        yield el


text = 'Le Lorem Ipsum est simplement du faux texte.'
for word in generator(text, sep=' '):
    print(word)
print('--')
text = 'Le Lorem Ipsum est simplement du faux texte.'
for word in generator(text, sep=' ', option='shuffle'):
    print(word)
print('--')
text = 'Le Lorem Ipsum est simplement du faux texte.'
for word in generator(text, sep=' ', option='ordered'):
    print(word)
print('--')
text = 'Le Lorem Ipsum est simplement du faux texte.'
for word in generator(text, sep=' ', option='unique'):
    print(word)
