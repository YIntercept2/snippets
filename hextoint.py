from decimal import *


mult = 64
getcontext().prec = 64*mult #65536 #64*mult

d = Decimal

def hextoint():
  # Creating the Dictionary  
  dictionary_hexa_to_decimal = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10 , 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}  
  hexadecimal_string = input("Please enter the hexadecimal value: ").strip().upper()  
  decimal = 0  
  hexadecimal_string = hexadecimal_string.replace(":", "")
  length = len(hexadecimal_string) -1  
     
  for digit in hexadecimal_string:  
      decimal += dictionary_hexa_to_decimal[digit]*d(16)**d(length)
      length -= 1  
     
  print ("The converted hexadecimal string into decimal string is: ", decimal)