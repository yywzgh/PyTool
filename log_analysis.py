import os
import re
from collections import Counter

path = "D:/log"
files= os.listdir(path)
countX = []

for file in files:
     if not os.path.isdir(file):
          f = open(path+"/"+file);
          iter_f = iter(f);
          for line in iter_f:
              if line.find("[RDP3389] get a user connection") > -1:
                 result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
                 countX.append(''.join(result))

result = Counter(countX)
d = sorted(result.items(), key=lambda x: x[1], reverse=True)
for ip in d:
    print('%-20s' % ip[0], ip[1])

