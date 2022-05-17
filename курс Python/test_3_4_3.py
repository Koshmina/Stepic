import os
import re
s=''
s2=''
s3=''
s4=''
k=0
k1=0
l=''
rez=''
with open("/text.txt", 'r') as inf:
    s1=inf.readline().strip()
    s2=s1.lower().split()
    for i in (range(len(s2))):
        s = s2[i].lower()
        k=s2.count(s)
        if k>k1 and  (s not in s3):
            s3=s+' '+ str(k)+ ' '
            k1=k
        elif k==k1 and (s not in s3):
            s3 = s3 + s + ' ' + str(k) + ' '
s4=s3.split()
'''for i in (range(len(s4))):
     if s4[i]>l:
         rez=s4[i]+''
         l=s4[i] '''
print(s4[0], s4[1])



#ouf=open("C:\\Autotest\\text1.txt",'w')
#ouf.write(s)