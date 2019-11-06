from random import randint

print('This is an interactive guessing game!')
print('You have to enter a number between 1 and 99 to find out the' +
      'secret number.')
print('Type \'exit\' to end the game.')
print('Good luck!')

exit = False
n = randint(1, 100)
i = 1
guess = None
while guess != n and not exit:
    print('What\'s your guess between 1 and 99?')
    guess_r = input('>> ')

    if guess_r == 'exit':
        exit = True
        print('Goodbye!')
    elif not guess_r.isdigit():
        print('That\'s not a number.')
    else:
        guess = int(guess_r)
        if guess != n:
            print('Too high!' if guess > n else 'Too low!')
            i += 1

if not exit:
    if n == 42:
        print('The answer to the ultimate question of life,' +
              ' the universe and everything is 42.')
    if i > 1:
        print('Congratulations, you\'ve got it!')
        print('You won in {} attempts!'.format(i))
    else:
        print('Congratulations, you got it on your first try!')
