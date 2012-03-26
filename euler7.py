counter = 0
x=1
while counter<10001:
    x+=1
    counter += (lambda x: not bool([y for y in range(2,int(x**0.5)+1) if x%y==0]))(x):
print x
