import requests

with open("/text.txt", 'r') as inf:
  s1 = inf.readline().strip()
  r=requests.get(s1)
  s2 = r.text.splitlines()

  print(len(s2))