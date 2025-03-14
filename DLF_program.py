'''
    So I think to get all the IPA in the DLF, my first step
    would be to isolate the pages where the IPA occurs.
    Delete what's irrelevant. Then, make the whole file one
    giant string. Next, import the string module and run the
    whole thing through a function to remove punctuation.
    Check the new string out and see if everything still looks good.
    Next, use the split method to create a list of individual "words".
    Then, peruse this list and use a combination of find and len to
    populate a new list with only IPA. Finally, write this list
    to a new file.
'''

# This is what I used to generate a list of IPA pronunciations found in the DLF.
# At this point, I don't think I need to run this again. I have made copies of
# all the relevant files and put them elsewhere. Be aware that this code does
# create new files (and overwrites old ones of the same name)!

hand1 = open("dlf.txt", "r")
lines = hand1.readlines()

def replace(string, old, new):
    new_string = new.join(string.split(old))
    return new_string

lines_str = str(lines)
hand1.close()

# I want a string that replaces paragraphs with space characters

hand2 = open("dlf_noP.txt", "w")
noP_str = replace(lines_str, "\n", " ")
hand2.write(noP_str)
hand2.close()

def get_ipa(string):
    b_idx = 0
    ipa = []
    for _ in string:
        if _ == "[":
            ipa.append(string[string.find("[", b_idx):string.find("]", b_idx) + 1])
        b_idx += 1
    return ipa

# These next functions are cleaning up my words within the list noP_str

ipa_list = get_ipa(noP_str)
ipa_list_copy = ipa_list[:]
bad_elem = ["eccl.", "baby", "offensive", "endearment", "...", "=", "i.e.", "…", "\t"]
for _ in ipa_list_copy:
    if any(x in _ for x in bad_elem) == True:
        ipa_list_copy.remove(_)
    elif len(_) > 40:
        ipa_list_copy.remove(_)

# I want to remove duplicates

ipa_list_copy = list(set(ipa_list_copy))

# This next step is meant to split entries with multiple pronunciations.
# I also need to account for entries that only show alternation in an ending.
# And I need to account for entries with more than two alternations.
# Note that right now this is only capturing entries with three alternative
# pronunciations. I should come back to clean this up later...

multi_pro = []

for _ in ipa_list_copy:
    if "," in _:
        if "-" in _:

# Rather pleased with this little bit of code for mas/fem ending alternations

            if "œr" == _[_.find(",")-2:_.find(",")] and "øz" == _[_.find("-")+1:_.find("-")+3]:
                multi_pro.append(_[:_.find(",")] + "]")
                multi_pro.append(_[:_.find(",")-2] + _[_.find("-") + 1 :])
                ipa_list_copy.remove(_)
            else:
                multi_pro.append(_[:_.find(",")] + "]")
                b = _.find("-")
                c = _[b + 1]
                multi_pro.append(_[:_.find(c)] + _[_.find("-") + 1 :])
                ipa_list_copy.remove(_)
        elif _.count(",") > 1:
            multi_pro.append(_[:_.find(",")] + "]")
            multi_pro.append("[" + _[_.find(",") + 2 : _.index(",",_.find(",") + 1)] + "]")
            multi_pro.append("[" + _[_.index(",",_.find(",") + 1) + 2:])
            ipa_list_copy.remove(_)
        else:
            multi_pro.append(_[:_.find(",")] + "]")
            multi_pro.append("[" + _[_.find(",") + 2:])
            ipa_list_copy.remove(_)

# Got to merge my multiple pronunciation items with the rest of the headwords

ipa_list_copy.extend(multi_pro)

# For good measure, I'll remove duplicates again then sort

ipa_list_copy = list(set(ipa_list_copy))
ipa_list_copy.sort()

# Again, probably a really silly way to clean a list

dummy_list = []
for _ in ipa_list_copy:
    if "'" in _:
        ipa_list_copy.remove(_)
    else:
        dummy_list.append(_)
ipa_list_copy = dummy_list[:]

dummy_list = []
for _ in ipa_list_copy:
    if "=" in _:
        ipa_list_copy.remove(_)
    else:
        dummy_list.append(_)
ipa_list_copy = dummy_list[:]

dummy_list = []
for _ in ipa_list_copy:
    if any(char.isupper() for char in _) == True:
        ipa_list_copy.remove(_)
    else:
        dummy_list.append(_)
ipa_list_copy = dummy_list[:]

# Might want to ponder whether this is a good thing to do or not

dummy_list = []
for _ in ipa_list_copy:
    if " " in _:
        ipa_list_copy.remove(_)
    else:
        dummy_list.append(_)
ipa_list_copy = dummy_list[:]

# This doesn't seem to have captured all the instances it should have...

hand3 = open("dlf_ipa.txt", "w")

def print_newline(list):
    idx = 0
    while idx < len(list):
        for _ in list:
            hand3.write(str(_)+"\n")
            idx += 1

print_newline(ipa_list_copy)

hand3.close()

'''
Honestly, at this point I feel like I am really close. I just want
to correct the rest by hand. That's probably not kosher though...
'''