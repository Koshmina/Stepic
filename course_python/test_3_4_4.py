import os
import re
s1=''
s2=''
sr=0
sum_one=0
sum_two=0
sum_three=0
with open("/text.txt", 'r', encoding='utf-8') as inf:
  #  s1=inf.readline().strip()
    s1 = [s.rstrip() for s in inf.readlines()]
    s2 = [s.split(';') for s in s1]
    for x in s2:
        sr=(int(x[1])+int(x[2])+int(x[3]))/3
        print(sr)
    for x in s2:
        sum_one+=int(x[1])
        sum_two+=int(x[2])
        sum_three+=int(x[3])

print(sum_one/len(s2), sum_two/len(s2), sum_three/len(s2))
