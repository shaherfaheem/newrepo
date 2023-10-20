def validate_pin(pin):
    import re
    pattern = r'[-!@#$%^&*()_+{}\[\]:;<>,.?~\\/]'

    if re.search(pattern, pin):
            return False
        
    for char in pin:
        if not char.isdigit():
            return False
    pin_digits= pin.count('') - 1
    print(pin_digits)
    if pin_digits == 4 or pin_digits == 6:
        return True
    return False

print(validate_pin('098761'))
