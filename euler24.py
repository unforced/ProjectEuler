#Oh god this was done terribly
arange=['0','1','2','3','4','5','6','7','8','9']
x=[]
for a in arange:
  brange = arange[:]
  brange.remove(a)
  for b in brange:
    crange = brange[:]
    crange.remove(b)
    for c in crange:
      drange = crange[:]
      drange.remove(c)
      for d in drange:
        erange = drange[:]
        erange.remove(d)
        for e in erange:
          frange = erange[:]
          frange.remove(e)
          for f in frange:
            grange = frange[:]
            grange.remove(f)
            for g in grange:
              hrange = grange[:]
              hrange.remove(g)
              for h in hrange:
                irange = hrange[:]
                irange.remove(h)
                for i in irange:
                  jrange = irange[:]
                  jrange.remove(i)
                  for j in jrange:
                    s = a+b+c+d+e+f+g+h+i+j
                    x.append(s)
                    if len(x)==1000000: break
print x[999999]
