def is_palindrome_permutation(string):
    string_copy = " ".join(string.split()).lower().replace(" ", "") # remove extra whitespace
    dict = {}
    for char in string_copy:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    
    multiple_odd_chars_check = True
    for key in dict:
        if dict[key] % 2 != 0:
            if multiple_odd_chars_check:
                multiple_odd_chars_check = False
            else:
                return False
        else:
            continue
    
    return True

# Test 1 string 'Tact Coa'. Expected result = True
print("# Test 1 string 'Tact Coa'. Expected result = True")
print(is_palindrome_permutation('Tact Coa'))

print()

# Test 2 string 'House mouse'. Expected result = False
print("# Test 2 string 'House mouse'. Expected result = False")
print(is_palindrome_permutation('House mouse'))
