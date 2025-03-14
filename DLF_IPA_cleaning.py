'''
This is a more advanced cleaning program for the list
of supposed IPA strings I got out of the DLF.
'''

hand1 = open("dlf_ipa.txt", "r")
lines = hand1.readlines()

for _ in lines[:20]:
    if "," in _:
        print(_)
        lines.append("[" + _[_.find(",") + 2 :] + "\n")
        lines.append(_[ : _.find(",")] + "]" + "\n")
        lines.remove(_)

for _ in lines[0:15]:
    print(_)
for _ in lines[len(lines)-5 : len(lines)-1]:
    print(_)

"""
I think at this point it will be easier to go through it by hand.
Once I have the DLF IPA forms I want, I can focus on the
work of transformation and comparison. I'll use that test suite
from the textbook and class.
"""