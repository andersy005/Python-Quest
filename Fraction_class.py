def gcd(m,n):
        while m % n != 0 :
            oldm = m
            oldn = n
            
            m = oldn
            n = oldm % oldn
            
        return n

class Fraction:
    
    def __init__ (self,top,bottom):
        self.num = top
        self.den = bottom
        
    #def show(self):
        #print self.num, "/" ,self.den
        
    def __str__(self):
        return str(self.num)+"/"+ str(self.den)
   
            
    
    def __add__(self,other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
        
    
    def __sub__(self,other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
        
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum
        
    def __mul__(self, other):
        mynum = self.num * other.num
        myden = self.den * other.den
        common = gcd(mynum, myden)
        return Fraction(mynum//common,myden//common)
        
    def __div__(self, other):
        ournum = self.num * other.den
        ourden = self.den * other.num
        common = gcd(ournum, ourden)
        return Fraction(ournum//common ,ourden//common)
    
    def __lt__(self,other):
        num = self.num * other.den
        den = self.den * other.num
        return num < den
        
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum > secondnum

    def getNum(self):
        print "The Numerator is:",(self.num)

    def getDen(self):
        print "The Denominator is:",(self.den)
        
def main():
    f1 = Fraction(2,3)
    f2 = Fraction(1,2)
    print "Addition", f1+f2
    print "Are they equal?",(f1==f2)
    print "Division",(f1 / f2)
    print"subtraction", f1 - f2
    print"multiplication", f1 * f2
    print"f1 less than f2", f1 < f2
    print"f1 greater than f2", f1 > f2

    f2.getNum()
    f2.getDen()
    
main()


