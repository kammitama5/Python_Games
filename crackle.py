def Crackle_orCracklePop():
  for num in range(1, 101):
    if ((num % 3 == 0) and (num % 5 == 0)):
      print "CracklePop"
    elif (num % 3) == 0:
      print "Crackle"
    elif (num % 5) == 0:
      print "Pop"
    else:
      print num
    
    
  return


Crackle_orCracklePop() 


