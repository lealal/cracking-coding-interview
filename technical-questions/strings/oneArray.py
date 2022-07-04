def one_array(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False

    # store string 1 characters
    dict = {}
    for char in string1.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    print(dict)
    one_change_available = True
    for char in string2.lower():
        if char in dict:
            dict[char] -= 1
        else:
            if one_change_available:
                one_change_available = False
            else:
                return False

    return True
        


# Test 1 string1: pale string2: ple. Expected result = True
print("# Test 1 string1: pale string2: ple. Expected result = True")
print(one_array('pale', 'ple'))

print()

# Test 2 string1: pales string2: pale. Expected result = True
print("# Test 2 string1: pales string2: pale. Expected result = True")
print(one_array('pales', 'pale'))

print()

# Test 3 string1: pale string2: bale. Expected result = True
print("# Test 3 string1: pale string2: bale. Expected result = True")
print(one_array('pale', 'bale'))

print()

# Test 4 string1: pale string2: bake. Expected result = False
print("# Test 4 string1: pale string2: bake. Expected result = False")
print(one_array('pale', 'bake'))
