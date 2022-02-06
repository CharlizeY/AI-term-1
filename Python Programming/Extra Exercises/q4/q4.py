def simplify_fraction(numerator, denominator):
    common_divisors = []
    
    for i in range(1, numerator+1 and denominator+1):
        if (numerator%i == 0 and denominator%i == 0):
            common_divisors.append(i)

    max_divisor = max(common_divisors)
    new_numerator = int(numerator/max_divisor)
    new_denominator = int(denominator/max_divisor)
    return (new_numerator, new_denominator)

