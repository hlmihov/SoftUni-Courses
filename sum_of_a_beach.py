input_text = input()
input_text = input_text.lower()
word_count = input_text.count('water') + input_text.count('sand') + input_text.count('fish') + input_text.count('sun')
print(word_count)
