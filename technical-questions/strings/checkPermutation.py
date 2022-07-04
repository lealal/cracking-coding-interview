def check_permutation(string1, string2):
    # check if words have the same legth
    if (len(string1) != len(string2)):
        return False

    # store characters of first word
    dict = {}
    for char in string1.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    
    # check if second word contains the same characters and remove char from current dict
    # if they exist
    for char in string2.lower():
        if char not in dict:
            return False
        else:
            dict[char] -= 1
    
    # check that keys are 0
    for key in dict:
        if dict[key] > 0:
            return False

    return True

# Test 1 string1: ACAAB string2: BAAAC. Expected result: True
print("# Test 1 string1: ACAAB string2: BAAAC. Expected result: True")
print(check_permutation('ACAAB', 'BAAAC'))

print()

# Test 2 string1: FGDAS string2: FGDASA. Expected result: False
print("# Test 2 string1: FGDAS string2: FGDASA. Expected result: False")
print(check_permutation('FGDAS', 'FGDASA'))

print()

# Test 3 string1: dash string2: Dase. Expected result: False
print("# Test 3 string1: dash string2: Dase. Expected result: False")
print(check_permutation('dash', 'Dase'))
