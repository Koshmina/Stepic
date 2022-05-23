b = []
c= []
s=input().split()
while 'end' not in s :
  b.append(s)
  s = input().split()

for i in range(len(b[0])):
    for j in range (len(b)):
        if i-1==len(b[0]):
          c[i][j]=int(b[i-1][j])+int(b[i+1][j])+int(b[i][j-1])+int(b[i][j+1])
print(c)
#(i-1, j), (i+1, j), (i, j-1), (i, j+1)







