'''
A1.3.5 Stainbrook.py
Programmer: Ethan Stainbrook
Understanding how strings function in python
'''
essay = input("Please enter essay:") #Iterating Input which allows the user to put their essay in.
def how_eligible(essay):
    eligible = 0 #Start with 0 because you haven't entered anything yet.
    if "!" in essay: #checking to see if ! is in the essay.
        eligible = eligible + 1
    elif ';' in essay: #Checking to see if ; is in the essay.
        eligible += 1
    elif ":" in essay: #Checking to see if : is in the essay.
        eligible += 1
    elif "?" in essay: #Checking to see if ? is in the essay
        eligible += 1
    elif "\"\"" or " ' ' ":
        eligible += 1
    else:
        eligible += 0
    print(eligible) #returning the score
    
how_eligible(essay)
# 'Falling words. Out the window you go! ahhh?
#Faceplant, on an "eggplant"
