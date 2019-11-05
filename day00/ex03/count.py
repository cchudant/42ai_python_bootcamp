import sys

def text_analyzer(text = None):
    """This function prints the number of upper characters, lower characters,
    punctuation and spaces in a given text.

    Input is taken from stdin when no argument is passed.
    """

    if text == None:
        print('What is the text to analyze?')
        text = input('>> ')

    if len(text) == 0:
        print('The text is empty!')
        return

    upper = len(list(filter(lambda x: x.isupper(), text)))
    lower = len(list(filter(lambda x: x.islower(), text)))
    punctuation = len(list(filter(
            lambda x: x in '[.,/#!$%^&*;:{}=\-_`~()]\'"', text)))
    spaces = len(list(filter(lambda x: x == ' ', text)))

    print('The text contains %d characters:' % len(text))
    print('- %d upper letters' % upper)
    print('- %d lower letters' % lower)
    print('- %d punctuation marks' % punctuation)
    print('- %d spaces' % spaces)
