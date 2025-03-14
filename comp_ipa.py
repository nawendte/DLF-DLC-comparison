'''
In this program, I want to create two new files. The first one will
list all DLC headwords whose IPA matches a line in the transformed
DLF IPA file. The second one will list all DLC headwords whose IPA
does not match a line in the transformed DLF IPA file. Once these
are created, I can begin to compare.
'''

# Create a list of the DLC IPA

hand1 = open("dlc_ipa.txt", "r")
dlc_ipa = hand1.readlines()
hand1.close()

# Create a list of the transformed DLF IPA

hand2 = open("dlf_trans.txt", "r")
dlf_trans = hand2.readlines()
hand2.close()

# Create a new list of DLC IPA forms that match a form in dlf_trans
# then write that new list to a file

matched_ipa = []

def matched_members(list1, list2, list3):
    for _ in list1:
        if _ in list2:
            list3.append(_)
    return list3

matched_members(dlc_ipa, dlf_trans, matched_ipa)

hand3 = open("matched_ipa.txt", "w")
idx = 1
for _ in matched_ipa:
    hand3.write(str(idx))
    hand3.write(". ")
    hand3.write(_)
    idx += 1
hand3.close()

# Create a new list of DLC IPA forms that don't match a form
# in dlf_trans then write that new list to a file

unmatched_ipa = []

def unmatched_members(list1, list2, list3):
    for _ in list1:
        if _ not in list2:
            list3.append(_)
    return list3

unmatched_members(dlc_ipa, dlf_trans, unmatched_ipa)

hand4 = open("unmatched_ipa.txt", "w")
idx = 0
for _ in unmatched_ipa:
    hand4.write(str(idx))
    hand4.write(". ")
    hand4.write(_)
    idx += 1
hand4.close()

# Just skipping ahead to Step 7 of this project...
# What proportion of DLC IPA matches a transformed line of
# transformed DLF IPA!?

print("Count of transformed DLF IPA entries: ", len(dlf_trans))
print("Count of DLC IPA entries: ", len(dlc_ipa))
print("Count of unmatched entries: ", len(unmatched_ipa))
print("Count of matched entries: ", len(matched_ipa))
print("Proportion of DLC IPA matching transformed DLF IPA: ", f"{len(matched_ipa)/len(dlc_ipa):.0%}")