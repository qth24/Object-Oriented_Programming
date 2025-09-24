import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def shorten(self):
        n = math.gcd(self.numerator, self.denominator)
        num = self.numerator // n
        deno = self.denominator // n
        if num % deno == 0:
            out = num // deno
            return str(out)
        else:
            return f"{num}/{deno}"
        
# function to add two fractions
def add(frac1: Fraction , frac2: Fraction):
    if frac1.denominator == frac2.denominator:
        num = frac1.numerator + frac2.numerator
        deno = frac1.denominator
    else:
        num1_temp = frac1.numerator * frac2.denominator
        num2_temp = frac2.numerator * frac1.denominator
        deno = frac1.denominator * frac2.denominator
        num = num1_temp + num2_temp

    sum  = Fraction(num, deno)
    return sum.shorten()

# function to subtract two fractions
def subtract(frac1: Fraction , frac2: Fraction):
    if frac1.denominator == frac2.denominator:
        num = frac1.numerator - frac2.numerator
        deno = frac1.denominator
    else:
        num1_temp = frac1.numerator * frac2.denominator
        num2_temp = frac2.numerator * frac1.denominator
        deno = frac1.denominator * frac2.denominator
        num = num1_temp - num2_temp

    sub  = Fraction(num, deno)
    return sub.shorten()

# function to mutiple two fractions
def multiple(frac1: Fraction , frac2: Fraction):
    num = frac1.numerator * frac2.numerator
    deno = frac1.denominator * frac2.denominator
    production = Fraction(num, deno)
    return production.shorten()

# function to devide two fractions
def devide(frac1: Fraction, frac2: Fraction):
    num = frac1.numerator * frac2.denominator
    deno = frac1.denominator* frac2.numerator
    quotient = Fraction(num, deno)
    if frac2.numerator == 0:
        return "Cannot devide 0"
    else:
        return quotient.shorten()

# function to calc the sum of all fractions on the list
def sum_list(fractions: list[Fraction]):
    result = Fraction(0, 1)
    for frac in fractions:
        temp = add(result, frac)
        if isinstance(temp, str): 
            num, den = map(int, temp.split('/')) if '/' in temp else (int(temp), 1)
            result = Fraction(num, den)
        else:
            result = temp
    return result.shorten()

# function to get the greatest fraction of the list
def max_frac(fractions: list[Fraction]):
    temp = Fraction(0, 1)
    min = -10**1000
    for frac in fractions:
        num_temp = frac.numerator / frac.denominator
        if num_temp > min:
            min = num_temp
            temp = frac
    return temp.shorten()


if __name__ == "__main__":
    
    # Input: Get 2 fractions, the format is a/b
    print('### Input format a/b, a and b are intergers, b != 0 ###\n')
    inp1 = input('First fraction: ')
    x = inp1.split('/')
    fraction1 = Fraction(int(x[0]), int(x[1]))

    inp2 = input('Second fraction: ')
    y = inp2.split('/')
    fraction2 = Fraction(int(y[0]), int(y[1]))

    # 1. enter 2 fraction, calculate the sum, difference, product, quotient
    print('> Sum: ' + add(fraction1, fraction2))
    print('> Difference :' + subtract(fraction1, fraction2))
    print('> Product: ' + multiple(fraction1, fraction2))
    print('> Quotient: ' + devide(fraction1, fraction2))

    # 2. enter a list of fractions, print the sum of all fractions and the biggest one
    print('\n### Enter a list of fractions ###\n' )
    n = int(input('Number of fractions: '))
    frac_list = []
    for i in range (1, n+1):
        temp = input(f'Fraction {i}: ')
        w = temp.split('/')
        temp_frac = Fraction(int(w[0]), int(w[1]))
        frac_list.append(temp_frac)

    print(f'\n> Sum of the list: {sum_list(frac_list)}')
    print(f'> The greatest fraction: {max_frac(frac_list)}')

