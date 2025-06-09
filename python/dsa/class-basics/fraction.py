class Fraction:

    def __init__(self, num, den):
        self.num = num
        self.den = den
    

    def __str__(self):
        if self.num == self.den:
            return "1"
        return f"{self.num}/{self.den}"

    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        common = self.gcd(newNum, newDen)

        return Fraction(newNum // common, newDen // common)

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn

        return n

    def __eq__(self, otherFraction):
        return self.num * otherFraction.den == otherFraction.num * self.den

myf = Fraction(3, 4)
myf2 = Fraction(1, 2)


print(myf + myf2)
print(myf == myf2)