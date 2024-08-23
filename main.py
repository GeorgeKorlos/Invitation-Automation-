your_name = input('Please enter your name: ')

with open('/home/useradd/100-Days/Day-24/Letters/starting_letter.txt') as letter:
    l = letter.read()

with open('/home/useradd/100-Days/Day-24/Names/invited_names.txt') as list_names:
    names = list_names.readlines()

for name in names:
    name = name.strip()

    final = l.replace('[name]', name)
    final = final.replace('[your_name]', your_name)
    
    with open(f'/home/useradd/100-Days/Day-24/ReadyToSend/letter_for_{name}.txt', 'w') as completed:
        completed.write(final)

