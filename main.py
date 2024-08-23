your_name = input('Please enter your name: ')

with open('starting_letter.txt') as letter:
    l = letter.read()

with open('invited_names.txt') as list_names:
    names = list_names.readlines()

for name in names:
    name = name.strip()

    final = l.replace('[name]', name)
    final = final.replace('[your_name]', your_name)
    
    with open(f'letter_for_{name}.txt', 'w') as completed:
        completed.write(final)

