x=1
while True:
  if (lambda x: False not in [x%y==0 for y in range(11,21)])(x): print x; break
  else:  x+=1  
#Super slow, will rewrite
