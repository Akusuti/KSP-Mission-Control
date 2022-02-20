from re import T
import sys
from time import sleep

words = '- - KSP Astronaut Register - -'
for char in words:
    sleep(0.06)
    sys.stdout.write(char)

sleep(1)
print('\n')

words = 'Enter the Astronauts Name. \n'
for char in words:
    sleep(0.04)
    sys.stdout.write(char)

sleep(0.5)

name = input('Name: ').title()

print('\n')

words = 'Enter the Astronauts Occupation. \n'
for char in words:
    sleep(0.04)
    sys.stdout.write(char)

sleep(0.5)

occupation = input('Occupation: ').title()

with open('registered.txt','a') as file:
    file.write(f'Name: {name} \n')
    file.write(f'Occupation: {occupation} \n')
    file.write('Mission: None \n')
    file.write('Location: Kerbal Space Center \n')
    file.write('Status: Alive \n')
    file.write('\n')

sleep(1)

print('')

words = 'Thanks for Registering.'
for char in words:
    sleep(0.07)
    sys.stdout.write(char)