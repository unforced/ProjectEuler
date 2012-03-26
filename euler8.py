s = map(int, list(open('euler8.txt').read().replace('\n','')))
print max([s[index]*s[index+1]*s[index+2]*s[index+3]*s[index+4] for index in range(len(s)-5)])
