class Fraction:

    def __init__(self, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise Exception("Both inputs must be int")
        
        if den < 0:
            den = den * -1
            num = num * -1
        
        common = self.gcd(num, den)
        self.num = num // common
        self.den = den // common
    

    def __str__(self):
        if self.num == self.den:
            return "1"
        return f"{self.num}/{self.den}"

    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        # common = self.gcd(newNum, newDen)

        return Fraction(newNum, newDen)

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn

        return n
    
    def lcm(self, m, n):
        return m * n // self.gcd(m, n)

    def __eq__(self, otherFraction):
        return self.num * otherFraction.den == otherFraction.num * self.den

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __sub__(self, otherFraction):
        newNum = self.num * otherFraction.den - self.den * otherFraction.num
        newDen = self.den * otherFraction.den

        return Fraction(newNum, newDen)

    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den

        return Fraction(newNum, newDen)

    def __truediv__(self, otherFraction):
        newNum = self.num * otherFraction.den
        newDen = self.den * otherFraction.num
        return newNum / newDen

    def __gt__(self, otherFraction):
        return self.num * otherFraction.den > self.den * otherFraction.num

    def __ge__(self, otherFraction):
        return self.num * otherFraction.den >= self.den * otherFraction.num

    def __lt__(self, otherFraction):
        return self.num * otherFraction.den < self.den * otherFraction.num

    def __le__(self, otherFraction):
        return self.num * otherFraction.den <= self.den * otherFraction.num
    
    def __ne__(self, otherFraction):
        return self.num * otherFraction.den != self.den * otherFraction.num



myf = Fraction(1, -4)
myf2 = Fraction(6, 8)

print(myf)