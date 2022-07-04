def URLify(string, code):
    string_copy = " ".join(string.split()) # remove extra whitespace
    string_copy = string_copy.replace(" ", code) # replace whitespace with character code
    return string_copy

# Test 1 string 'Hello word   test  '. Expected result: Hello%20word%20test
print("# Test 1 string 'Hello word   test  '. Expected result: Hello%20word%20test")
print(URLify('Hello world   test  ', '%20'))

print()

# Test 2 string 'Commerce Retail NewShoes    20002 '. Expected result: Commerce%20Retail%20NewShoes%2020002 
print("Test 2 string 'Commerce Retail NewShoes    20002 '. Expected result: Commerce%20Retail%20NewShoes%2020002 ")
print(URLify('Commerce Retail NewShoes    20002 ', '%20'))
