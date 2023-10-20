def equal(s):
    # Convert the string to lowercase to make it case-insensitive
    s = str.lower(s)
    
    # Count the number of 'x's and 'o's in the string
    xs = s.count('x') 
    os = s.count('o') 
    
    if xs == os:
        return True
    return False
print(equal('xXoom'))
