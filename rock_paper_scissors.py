import random

options = ['rock', 'paper', 'scissors']

while True:
    print('\nEnter r for rock, p for paper or s for scissors.')
    player_choice = input('Please enter r/p/s: ').lower()
    if player_choice.lower() == 'r':
        player_hand = 'rock'
    elif player_choice.lower() == 'p':
        player_hand = 'paper'
    elif player_choice.lower() == 's':
        player_hand = 'scissors'
    else:
        print('Pleasd enter a valid move.')
    print(f'You chose {player_hand}.')

    computer_hand = random.choice(options)
    print(f'The computer chose {computer_hand}.')

    if player_hand == computer_hand:
        print('This match was a draw.')
    elif player_hand == 'rock' and computer_hand == 'scissors':
        print('You win.')
    elif player_hand == 'paper' and computer_hand == 'rock':
        print('You win.')
    elif player_hand == 'scissors' and computer_hand == 'paper':
        print('You win.')
    else:
        print('You lose.')
    
    rematch = input('Dou you want to play again (y/n)? ').lower()
    if rematch.lower() == 'y':
        continue
    else:
        print('\nThanks for playing!')
        break



        