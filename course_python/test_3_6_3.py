import requests

with open("/text.txt", 'r') as inf:
  s1 = inf.readline().strip()
  s=requests.get(s1)
  while True:
    if not s.text.startswith('We'):
      print (s.text)
      s = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + s.text)
    else:
      print(s.text)
      break
