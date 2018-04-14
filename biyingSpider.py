
import requests
import re
import time
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text
reg = r"(az/hprichbg/rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
print(a)
picUrl = url + a
read = requests.get(picUrl)
f = open('%s.jpg', 'wb')
f.write(read.content)
f.close()
