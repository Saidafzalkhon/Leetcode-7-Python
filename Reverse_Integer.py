x = int(input())
j = str(x)
if j[0] == '-':
   j = j[1:]
   j+='-'
k = int(j[::-1])
print(k if k<(2**31) and k>(-2**31) else 0)