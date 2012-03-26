print max([x*y for x in range(1000) for y in range(1000) if str(x*y) == str(x*y)[::-1]])
