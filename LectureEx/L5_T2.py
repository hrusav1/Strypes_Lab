

def pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / pow(base, -exponent)
    else:
        return base * pow(base, exponent - 1)


result = pow(5, 7)

print (result)
