'''
This is meant to be a parallel program for arriving at IPA
representations of headwords in the DLC. I don't think it will be too
hard to get the forms as they appear in the dictionary, but converting
them to IPA will be more of a challenge.
'''

# Per the Hammond 2020 book, working with HTML might be easier via
# a module called Beautiful Soup. This step gets me the HTML as text.

from bs4 import BeautifulSoup

with open("dlc.html") as f:
    soup = BeautifulSoup(f, 'html.parser')

f.close()
dlc = soup.get_text()

# Now I want to get the headwords as a list

dlc_lines = dlc.split("""<span class="headword">""")
dlc_hw = []

for _ in dlc_lines:
    dlc_hw.append(_[:_.find("<")])

# I want to clean these, remove duplicates, sort, then write to a file
# This next for block, I could use it, but I'd lose historical info.
# Headwords only show up with ' in front if it's a literary form.
# Same goes for headwords ending in *. They're hypothesized.
# I'll comment out this code for now.

#for _ in dlc_hw:
#    if "'" in _:
#        dlc_hw.append(_[1:len(_)-1])
#        dlc_hw.remove(_)

dlc_hw = list(set(dlc_hw))
dlc_hw.sort()

hand1 = open("dlc_hw.txt", "w")
for _ in dlc_hw:    
    hand1.write(_ + "\n")
hand1.close()

# Now I need to convert the headwords to IPA. This will be tricky...
# Gonna make a function that replaces characters in a string

def find_rep_str(string, old, new):
    return string.replace(old, new)

# Now I think I want to make a big list of tuples where each tuple
# is formatted (x, y) so that x is the old element and y is the IPA.

kv2ipa = []
def build_kv2ipa(kv, ipa):
    kv2ipa.append((kv, ipa))

build_kv2ipa("j", "ʒ")
build_kv2ipa("ch", "ʃ")
build_kv2ipa("gn", "ɲ")
build_kv2ipa("ò", "ɔ")
build_kv2ipa("y", "j")
build_kv2ipa("èr", "ær")
build_kv2ipa("è", "ɛ")
build_kv2ipa("eu", "ø")
build_kv2ipa("à", "a")
build_kv2ipa("ó", "o")
build_kv2ipa("ui", "ɥi")
build_kv2ipa("u", "y")

# I know this last one is weird, but it's the only way I can order
# the rules so that I don't replace <u> where I don't want to.

build_kv2ipa("oy", "u")

dlc_ipa = []

# Next I need to build a function to do these replacements.

def sub_ipa(list, correspond):
    for _ in list:
        for x in correspond:
            if x[0] in _:
                _ = find_rep_str(_.strip(), x[0], x[1])
        else:
            dlc_ipa.append(_.strip())
        
sub_ipa(dlc_hw, kv2ipa)

# There are some special rules that I need to write for the nasal
# vowels, and maybe others...

vowels = ["a", "e", "ɛ", "i", "o", "ɔ", "u", "y", "œ", "ø", "æ"]

list2 = []
for _ in dlc_ipa:
    if "an" in _:
        if _.index("an")+ 2 in range(len(_)) and _[_.index("an")+ 2] in vowels:
            list2.append(_)
        elif _.index("an")+ 2 not in range(len(_)):
            list2.append(find_rep_str(_, "an", "ɑ̃"))
        else:
            list2.append(find_rep_str(_, "an", "ɑ̃"))
    else:
        list2.append(_)
dlc_ipa = list2[:]

list2 = []
for _ in dlc_ipa:
    if "on" in _:
        if _.index("on")+ 2 in range(len(_)) and _[_.index("on")+ 2] in vowels:
            list2.append(_)
        elif _.index("on")+ 2 not in range(len(_)):
            list2.append(find_rep_str(_, "on", "ɔ̃"))
        else:
            list2.append(find_rep_str(_, "on", "ɔ̃"))
    else:
        list2.append(_)
dlc_ipa = list2[:]

list2 = []
for _ in dlc_ipa:
    if "en" in _:
        if _.index("en")+ 2 in range(len(_)) and _[_.index("en")+ 2] in vowels:
            list2.append(_)
        elif _.index("en")+ 2 not in range(len(_)):
            list2.append(find_rep_str(_, "en", "ɛ̃"))
        else:
            list2.append(find_rep_str(_, "en", "ɛ̃"))
    else:
        list2.append(_)
dlc_ipa = list2[:]

dlc_ipa.sort()

# This seems like a really silly way to clean a list!

dummy_list = []
for _ in dlc_ipa:
    if "'" in _:
        dlc_ipa.remove(_)
    else:
        dummy_list.append(_)
dlc_ipa = dummy_list[:]

# Might want to ponder whether this is a good thing to do or not

dummy_list = []
for _ in dlc_ipa:
    if " " in _:
        dlc_ipa.remove(_)
    else:
        dummy_list.append(_)
dlc_ipa = dummy_list[:]

# Gonna eventually have to figure out how to remove entries with
# an uppercase letter in them...

dummy_list = []
for _ in dlc_ipa:
    if any(char.isupper() for char in _) == True:
        dlc_ipa.remove(_)
    else:
        dummy_list.append(_)
dlc_ipa = dummy_list[:]

# Write the IPA of the headwords to a new file

hand2 = open("dlc_ipa.txt", "w")
idx = 1
for _ in dlc_ipa:
    hand2.write(str(idx) + ". [" + _ + "]" + "\n")
    idx += 1
hand2.close()

# This was astoundingly easy! Ah, the benefits of a phonemic
# orthography... One issue though. I'm not sure I captured
# alternative pronunciations. This will definitely be something
# to take into consideration when I conduct an analysis of my results.