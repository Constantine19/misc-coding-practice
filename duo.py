"""
Write a function that takes two strings as inputs and returns the set of common characters between them.
"""

def common_char(str1, str2):
    count1 = {}
    count2 = {}
    common = []

    for i in range(len(str1)):
        if str1[i] in count1:
            count1[str1[i]] += 1
        else:
            count1[str1[i]] = 1

    for i in range(len(str2)):
        if str2[i] in count2:
            count2[str2[i]] += 1
        else:
            count2[str2[i]] = 1

    for i in range(len(count1)):
        if count1.keys()[i] in count2.keys():
            common.append(count1.keys()[i])
    return common


str1 = 'Constantine'
str2 = 'Zelmanovich'
print common_char(str1, str2)
