#This code is the couse of NetworkChuch on Youtube

print('Hello, welcome to NetworkChuck Coffee!')

name = input('whats is your name?\n')

if name == 'Ben':
  print(f'You are not welcome here {name}!')
  exit()
else:
  print(f'Hi {name}, thank you so much for coming here today\n')

menu = ['Coffee', 'Espresso', 'latte', 'juice']
price = 8

print(f'{name} what do you want to drink, we have this options:')

for i in menu:
  print(i)

option = input("Your choice:\n")

quanty = input(f"How many {option}s do you want?\n")

total = int(quanty) * 8

print(f'The total is ${total}')