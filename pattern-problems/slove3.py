i = 1
while i <= 5:
  j = 1
  while j <= 5:
    if j==5 or j==1 or i==5 or i==1:
      print("* ",end="") 
    else:
        print(" ",end = " ") 
    j += 1
  print()
  i += 1