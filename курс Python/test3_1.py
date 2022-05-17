import os
s=''
s2='0'
s3=''
with open("/text.txt", 'r') as inf:
    s1=inf.readline().strip()
    for i in range(len(s1)):
       if s1[i].isdigit():
           s2=s2+s1[i]
       else:
           j=0
           for j in range(int(s2)):
             s=s+str(s3)
           s2='0'
           s3 = s1[i]
       if s1[i].isalpha() and int(s2) == 1:
           s = s + str(s3)
    if i==len(s1)-1:
        j = 0
        for j in range(int(s2)):
            s = s + str(s3)

ouf=open("/text1.txt", 'w')
ouf.write(s)

