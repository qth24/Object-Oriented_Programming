import math
import datetime

# create fraction class
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # method to shorten the fraction
    def shorten(self):
        n = math.gcd(self.numerator, self.denominator)
        num = self.numerator // n
        deno = self.denominator // n
        if num % deno == 0:
            out = num // deno
            return str(out)
        else:
            return f"{num}/{deno}"

# function to compare two fractions
def compare(frac1: Fraction , frac2: Fraction):
    f1 = frac1.numerator / frac1.denominator
    f2 = frac2.numerator / frac2.denominator
    if f1 > f2:
        return frac1
    elif f1 < f2:
        return frac2
    else:
        return "Both equal"

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


if __name__ == "__main__":
    # Input: Get 2 fractions, the format is a/b
    print('### Input format a/b, a and b are intergers, b != 0 ###\n')
    inp1 = input('First fraction: ')
    x = inp1.split('/')
    fraction1 = Fraction(int(x[0]), int(x[1]))

    inp2 = input('Second fraction: ')
    y = inp2.split('/')
    fraction2 = Fraction(int(y[0]), int(y[1]))

    # question a: shorten the fraction
    print('> Fraction1 shorten: ' + fraction1.shorten())
    print('> Fraction2 shorten: ' + fraction2.shorten())

    # question b: compare 2 fractions and print the bigger one
    print('> The bigger fraction: ' + str(compare(fraction1, fraction2)))

    # question c: print the sum, difference, product and quotient of two fractions
    print('> Sum: ' + add(fraction1, fraction2))
    print('> Difference :' + subtract(fraction1, fraction2))
    print('> Product: ' + multiple(fraction1, fraction2))
    print('> Quotient: ' + devide(fraction1, fraction2))

    # question d: Input a datetime, write out the next day datetime
    print('\n### Input format day/month/year, example 24/3/2006 ###\n')
    inp3 = input('Date: ')
    z = inp3.split('/')
    cur_date = datetime.datetime(int(z[2]), int(z[1]), int(z[0]))
    next_day = cur_date + datetime.timedelta(days=1)
    print('> Next day: ' + next_day.strftime('%d') + '/' + next_day.strftime('%m') + '/' + next_day.strftime('%Y'))