cel = []
far = []
for i in range(10):
    c = float(input())
    cel.append(c) 
    d = (((cel[i]) * 9/5) + 32)
    far.append(d)
for i in range(10):
     print(cel[i], "celcius =", far[i], "Farenheit")