sum1 = 0
for i in range(1, 101):
    for j in range(1, i):
        if i%j==0:
            sum1+=j
    if sum1==i:
      print(i)
    sum1=0
