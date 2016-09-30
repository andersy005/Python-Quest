"""Given two strings, decide if one is a permutation of the other"""

def permutationsOfStrings(string1, string2):

    if len(string1) != len(string2):
        return False

    else:
         lista = list(string1)
         listb = list(string2)
         
         if lista.sort() == listb.sort():
             return True

         else:
            return False 
         
print(permutationsOfStrings("odg", "dog"))