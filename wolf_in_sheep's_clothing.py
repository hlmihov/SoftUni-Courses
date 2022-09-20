input_text = input()
input_list = input_text.split(', ')
if input_list[len(input_list) - 1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for i in range(len(input_list) - 2, -1, -1):
        if input_list[i] == 'wolf':
            sheep_spot = (len(input_list) - i) - 1
            print(f'Oi! Sheep number {sheep_spot}! You are about to be eaten by a wolf!')
