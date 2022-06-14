# Treasure Island

print('Welcome to Treasure Island. Your mission is to find the treasure')

left_or_right = input('Where you want to go? Left or Right: ')

if left_or_right == 'Left':
    swim_or_wait = input('Do you want to swim or wait: ')
    if swim_or_wait == 'wait':
        which_door = input('Which door you want to open? Red, Blue or Yellow: ')
        if which_door == 'Yellow':
            print('You Win!')
        else:
            print('Game Over, Mission Failed!')
    else:
        print('Game Over, Mission Failed!')
elif left_or_right == 'Right':
    print('Game Over, Mission Failed!')