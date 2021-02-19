# 导入之前安装的库
#import pdfkit
import requests
from bs4 import BeautifulSoup

#url = 'https://mp.weixin.qq.com/s/j5MyWthGRkhaItZstWI-VQ'
#url = 'https://mp.weixin.qq.com/s/k8-PkrIhRWZGtt8rucVSAA'
url = 'https://mp.weixin.qq.com/s/3iZDff8ZBqZ54Zbo_3nfRA'
url = 'https://mp.weixin.qq.com/s/KvsKGLcdugu6JrJ2RXsHGg'
r = requests.get(url)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, "html.parser")

title = "".join([ x.get_text() for x in soup.find_all('h1')])
print("title:", title)

# 最后打印出网页源码
voice = soup.find('mpvoice')
#print(voice)
fileid = voice.get("voice_encode_fileid")
url = 'https://res.wx.qq.com/voice/getvoice?mediaid=' + fileid
print(url)
r = requests.get(url)
with open(title + ".mp3", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)