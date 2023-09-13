def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b


def redu(x,y):
   b = pgcd(x,y)
   x /= b
   y /= b
   print ("Le plus grand diviseur commun est {0} la fraction equivaut a {1} / {2}".format(b,x,y))


redu(561,357)