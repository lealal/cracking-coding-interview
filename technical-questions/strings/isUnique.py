def is_unique(string):
    dict = {}
    for s in string.lower():
        if s in dict:
            return False
        else:
            dict[s] = 1
    return True

# Test 1 string: 'Animal' expected result = false
print("# Test 1 string: 'Animal'. Expected result = False")
print(is_unique('Animal'))

print()

# Test 2 string: 'Caroline' expected result = true
print("# Test 2 string: 'Caroline'. Expected result = True")
print(is_unique('Caroline'))
