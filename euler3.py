print [x for x in range(int(600851475143L**0.5),1,-1) if 600851475143L%x==0 and not (lambda x: bool([y for y in range(2,int(x**0.5)+1) if x%y==0]))(x)][0]
