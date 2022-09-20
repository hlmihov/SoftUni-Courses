input_string = input()
position_list = []
for i in range(len(input_string)):
    if input_string[i].isupper():
        position_list.append(i)
print(position_list)