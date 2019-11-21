'''
A1.3.5 Reece Westhoff.py
Programmer: Reece Westhoff
Understanding how strings function in python.
'''
essay= input('Please enter essay: ')
def how_eligible(essay):
    eligible = 0
    if '?' in essay:
        eligible += 1
    if '!' in essay:
        eligible += 1
    if '""' in essay:
        eligible += 1
        print('true')
    if ',' in essay:
        eligible += 1
    print (eligible)

how_eligible(essay)
    

