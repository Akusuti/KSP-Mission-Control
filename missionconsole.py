import time

import sys
from time import sleep

missionstarted = False

words = "- - KSP Mission Console - -"
for char in words:
    sleep(0.07)
    sys.stdout.write(char)

time.sleep(1)
print(' ')
print('\n')

words = 'KSA 2021 - Kerbal Space Agency MISSION CONTROL Console'
for char in words:
    sleep(0.07)
    sys.stdout.write(char)

time.sleep(1)
print(' ')
print('\n')

words = 'Type DATA to search for a registered astronaut'
for char in words:
    sleep(0.05)
    sys.stdout.write(char)

print('\n')

words = 'Type MISSION to begin a mission'
for char in words:
    sleep(0.05)
    sys.stdout.write(char)

print('\n')

words = 'Type EXIT to quit the program'
for char in words:
    sleep(0.05)
    sys.stdout.write(char)

print('\n')

choice = input('Enter a choice: ')

if choice.upper() == 'EXIT':
    words = 'Thanks for using KSA Mission Console'
    for char in words:
        sleep(0.07)
        sys.stdout.write(char)
    
    time.sleep(0.5)
    exit()

if choice.upper() == 'DATA':
    print(' ')
    kerbaldata = []
    with open('registered.txt','r') as file:
        for lines in file:
            kerbaldata.append(lines[0:len(lines)-2])
        print('')
        words = 'Obtaining Data... '
        for char in words:
            sleep(0.1)
            sys.stdout.write(char)
        time.sleep(1)
        print('COMPLETE')
        print(' ')
    words = 'Enter Name to Search for Kerbal'
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
    time.sleep(0.5)
    print(' ')
    kerbalsearch = input('Name: ').title()

    print(' ')

    for lines in kerbaldata:
        if kerbalsearch in lines:
            namepos = kerbaldata.index(f'Name: {kerbalsearch}')
            for x in range(0, 5):
                print(kerbaldata[namepos+x])
                time.sleep(0.5)

if choice.upper() == 'MISSION':

    print(' ')

    words = 'Loading Mission Creator... '
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)

    time.sleep(1)

    print('COMPLETE.')
    print(' ')

    words = 'Enter Mission Name to Start'
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)

    time.sleep(0.5)

    print(' ')

    missionname = input('Mission Name: ').title()

    print(' ')

    words = 'How many Kerbals are taking on this mission?'
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)

    time.sleep(0.5)

    print(' ')

    missionkerbals = []

    kerbalamount = int(input('Enter Number: '))
    for x in range(kerbalamount):
        words = f'Enter the Name of Kerbal {x+1}.'
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
        time.sleep(0.5)
        print('')
        kerbalname = input('Name: ')
        missionkerbals.append(kerbalname)

    print(missionkerbals)

    words = 'Updating Kerbals...'
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
    
    registeredkerbals = []

    with open('registered.txt','r') as file:
        for lines in file:
            registeredkerbals.append(lines[0:len(lines)-1])
    
    for x in range(len(missionkerbals)):
        for lines in registeredkerbals:
            if missionkerbals[x] in lines:
                namefind = registeredkerbals.index(f'Name: {missionkerbals[x]}')
                registeredkerbals[namefind+2] = f'Mission: {missionname.title()}'

    x = 0

    with open('registered.txt','w') as file:
        file.truncate()
    
    with open('registered.txt','a') as file:
        for x in range(len(registeredkerbals)):
            file.write(registeredkerbals[x])
            file.write('\n')

    time.sleep(1)
    print('\n')

    words = '- - MISSION STARTED - -'
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)

    time.sleep(1)

    print('\n')

    missionstarted = True

    words = 'Mission is now engaged. \n'
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)

    missiondeaths = 0

    while missionstarted == True:

        time.sleep(1)
        print(' ')

        words = '- - ACTIVE MISSION CONSOLE - - \n'
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
        print(' ')
        
        words = 'Enter LOCATION to change the location of the Kerbals on the mission. \n'
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
        print(' ')

        words = 'Enter STATUS to mark a Kerbal as dead. \n'
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
        print(' ')

        words = 'Enter END to end the mission. \n'
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
        print(' ')

        choice = input('Enter a choice: ')

        if choice.upper() == 'LOCATION':
            print(' ')
            words = 'Loading Location Data. \n'
            for char in words:
                sleep(0.05)
                sys.stdout.write(char)

            time.sleep(0.5)

            location = input('Enter current mission location: ')

            for x in range(len(missionkerbals)):
                for lines in registeredkerbals:
                    if missionkerbals[x] in lines:
                        namefind = registeredkerbals.index(f'Name: {missionkerbals[x]}')
                        registeredkerbals[namefind+3] = f'Location: {location.title()}'

            x = 0

            with open('registered.txt','w') as file:
                file.truncate()
    
            with open('registered.txt','a') as file:
                for x in range(len(registeredkerbals)):
                    file.write(registeredkerbals[x])
                    file.write('\n')
            
            print(' ')

        if choice.upper() == 'STATUS':
            print(' ')
            words = 'Loading Status Data \n'
            for char in words:
                sleep(0.05)
                sys.stdout.write(char)
            time.sleep(0.5)
            words = 'Enter an active kerbal to declare as dead. \n'
            for char in words:
                sleep(0.05)
                sys.stdout.write(char)
            time.sleep(0.5)
            kerbalchoice = input('Enter Name: ')

            for x in range(len(missionkerbals)):
                for lines in registeredkerbals:
                    if kerbalchoice.title() in lines:
                        namefind = registeredkerbals.index(f'Name: {kerbalchoice.title()}')
                        registeredkerbals[namefind+4] = f'Status: Dead'

            x = 0

            with open('registered.txt','w') as file:
                file.truncate()
    
            with open('registered.txt','a') as file:
                for x in range(len(registeredkerbals)):
                    file.write(registeredkerbals[x])
                    file.write('\n')

        if choice.upper() == 'END':
            words = 'Loading Mission Data \n'
            for char in words:
                sleep(0.05)
                sys.stdout.write(char)
            sleep(0.5)
            print('COMPLETE \n')

            time.sleep(0.5)
            words = 'Was the mission Successful, Unsuccessful or Aborted. \n'
            for char in words:
                sleep(0.05)
                sys.stdout.write(char)
            time.sleep(0.5)
            
            missioncomplete = input('Enter a choice: ').title()

            with open('missionlogs.txt','a') as file:
                file.write('- \n')
                file.write(f'MISSION NAME: {missionname} \n \n')
                file.write('KERBALS: \n')
                for x in range(len(missionkerbals)):
                    file.write(f'Kerbal {x+1}: {missionkerbals[x]} \n')
                file.write('\n')
                file.write('MISSION CONCLUSION: \n')
                file.write(f'{missioncomplete} \n')
                file.write('- \n \n')

            missionstarted = False
        
words = 'Thanks for using the KSA Mission Control Console. \n'
for char in words:
    sleep(0.08)
    sys.stdout.write(char)

input()









