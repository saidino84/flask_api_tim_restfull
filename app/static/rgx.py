import os
import re

os.chdir(os.path.dirname(__file__))
dados=os.listdir('./images')

# print(dados)

pattern = re.compile(r".+-gradient-.*\.[jpg]*")
currencys=[]
for data in dados:
    _news=pattern.findall(data)
    # print(_news)
    for d in _news:
        if pattern.match(d):
            currencys.append(d)
currencys.sort()
print(currencys)