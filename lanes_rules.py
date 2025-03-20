# This program functionalizes the proposed changes in Lane 1935

'''
1. [ɛ] > [e] in open syllables but final lost [r] preserves [ɛ]

2. [o] > [ɔ] in closed syllables

3. * [y] > [i]

4. [œ] > [ɛ], //but consider what a lost [r] would mean in this context//

5. * [ø] > [e]

6. * [ə] > [e, i] hypothesized to assimilate to other vowels in word

7. [œ̃] > [ɛ̃]

8. [ɑ̃] > [ɔ̃]

9. * final vowel nasalized after a nasal consonant (sporadic)

10. vowels denasalized after [d, b], which are assimilated to [n, m]

11. * [tɥ] > [tʃw] (No. 14 in Lane's original article)

12. * [ɥ] may be lost, //if followed by [i], it seems//

13. * [tj] > [tʃ]

14. * [ɥ] > [w] (No. 11 in Lane's original article)

15. * [dj] > [dʒ]

16. * [vw] > [w]

17. final [l] and [ɾ] often dropped after consonants

18. final [r] often dropped after vowels

* = a rule that only affects LC; others said to affect LF as well

'''

hand1 = open("dlf_ipa.txt", "r")
dlf_ipa = hand1.readlines()
hand1.close()

# Lane No. 1
# Lane No. 2

'''
Rules 1 and 2 rely on syllabification, which I am not going to mess
with for this study. At least not yet.
'''

# Lane No. 3

def lane_3(list):
    for _ in list:
        if "y" in _:
            x = _.replace("y", "i")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 4

'''
Representations of [æ] could complicate my results somewhat...
'''

def lane_4(list):
    for _ in list:
        if "œ" in _:
            x = _.replace("œ", "ɛ")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 5

def lane_5(list):
    for _ in list:
        if "ø" in _:
            x = _.replace("ø", "e")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 6 (ignoring for now)
# Lane No. 7

def lane_7(list):
    for _ in list:
        if "œ̃" in _:
            x = _.replace("œ̃", "ɛ̃")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 8

def lane_8(list):
    for _ in list:
        if "ɑ̃" in _:
            x = _.replace("ɑ̃", "ɔ̃")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 9 (ignoring for now)
# Lane No. 10 (ignoring for now)
# Lane No. 11

def lane_11(list):
    for _ in list:
        if "tɥ" in _:
            x = _.replace("tɥ", "tʃw")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 12

def lane_12(list):
    for _ in list:
        if "ɥi" in _:
            x = _.replace("ɥ", "")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 13

def lane_13(list):
    for _ in list:
        if "tj" in _:
            x = _.replace("tj", "tʃ")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 14

def lane_14(list):
    for _ in list:
        if "ɥ" in _:
            x = _.replace("ɥ", "w")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 15

def lane_15(list):
    for _ in list:
        if "dj" in _:
            x = _.replace("dj", "dʒ")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 16

def lane_16(list):
    for _ in list:
        if "vw" in _:
            x = _.replace("vw", "w")
            list.append(x)
            list.remove(_)
    return list

# Lane No. 17
# Lane No. 18

'''
Both of these seem sporadic, so I am going to ignore for now.
'''

# Let's wrap all of Lane's rules into one function

def lanes_rules(list_original):
    for _ in list_original:
        lane_3(list_original)
        lane_4(list_original)
        lane_5(list_original)
        lane_7(list_original)
        lane_8(list_original)
        lane_11(list_original)
        lane_12(list_original)
        lane_13(list_original)
        lane_14(list_original)
        lane_15(list_original)
        lane_16(list_original)
    return list_original[:]

# Next up, I need to apply all of these rules to my dlf ipa
# Then, I need to save them to a new list and save that to a new file
# Can't number the lines or it messes up matching

dlf_trans = []
dlf_trans = lanes_rules(dlf_ipa)
dlf_trans.sort()

hand2 = open("dlf_trans.txt", "w")
for _ in dlf_trans:
    hand2.write(_)
hand2.close()

# This was a good way to test my lanes_rules function

#test_list = ["kyky", "kœkœ", "køkø", "kœ̃kœ̃", "kɑ̃kɑ̃", "tɥa", "tɥi", "tjatja", "kɥo", "djo", "vwo"]
#print(lanes_rules(test_list))

'''
This also got me pretty near a finished result! Some cleaning by hand
will probably still be necessary, but this is good!
'''