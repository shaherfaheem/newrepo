def this_is_will_form_a_triangle(x,y,z):
    if x + y > z and y + z > x and x + z > y:
        if x > 0 and y > 0 and z > 0:
            return True
    else:
        return False
print(this_is_will_form_a_triangle(1,2,3))
print(this_is_will_form_a_triangle(1,1,1))
print(this_is_will_form_a_triangle(9,7,13))