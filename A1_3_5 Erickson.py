"""
A1_3_2 Erickson.py
Programmer:Wyatt Erickson
"""
slogan = 'my school is the best'
type(slogan)

slogan

slogan(0) #remember that 0 is the first letter
#the answer would be 'm'
slogan(2)
#the answer would be s
slogan(8)

slogan(26)

slogan(-2) #unique to python: index<0 counts from end

#8 slicing allows you to take a snippet of a code that is assigned to an operator by using brackets and a colloin

slogan[0:5]#in this code slogan (my school is the best) is given this [:] that gives the first 6 letters 0=1 in the expression

slogan[17:21]# this is the code for 'best' in the term of slogan

slogan[:13] + awesome #this is 'my school is awesome'

len(slogan) # the output would be 21 due to the length of slogan

#assign theater to activity and then put
'test goo' in 'greatest good for the greatest number'
#the return value would be true becasue of the boolean expression IN
#question 13
essay='I can create a lot of things, except pottery i suck at pottery. well what do you think?'
eligible = 0
if 'I' in essay:
    eligible = eligible + 1
if '.'in essay:
    eligible = eligible + 1
if ',' in essay:
    eligible = eligible + 1
if '?' in essay:
    eligible = eligible + 1
if '\'\'' or '""':
    else
