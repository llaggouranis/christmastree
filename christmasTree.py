i=0 
j=0 
while i<16:
    print((" " *(16-i)) + ("*" * (i*2 + 1)))
    if i>=15:
      while j<6:
        print((" " * 14) + ("*" * 5))
        j=j+1
    i=i+1 