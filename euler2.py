a = 0
b = 1
fibonacci = []
while b <= 4000000:
   fibonacci.append(b)
   a,b=b,a+b
print sum([x for x in fibonacci if x%2==0])
#I feel this should be able to be a one-liner

