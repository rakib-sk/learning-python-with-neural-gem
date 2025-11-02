i = 5
while i >= 1:
  j = 1
  while j <= 5 - i:
    print(end=" ")
    j += 1
  while j <= 5: 
    print("*",end = " ") 
    j += 1
  print()
  i -= 1 
