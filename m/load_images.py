import zlib,re,gevent
from gevent import monkey
import chardet
import urllib.request

monkey.patch_all()

def get_url(one_url):
    '''接受网址返回图片列表'''
    response=urllib.request.urlopen(one_url)
    html=response.read()
    html = zlib.decompress(html, 16+zlib.MAX_WBITS)
    print(chardet.detect(html))
    html = html.decode("utf-8")
    img_list = re.findall(r"https://[^/]+/[^/]+/\d+/.{4,40}jpg", html)
    return img_list

def download(img_name, img_url):
    '''下载一个图片'''
    req = urllib.request.urlopen(img_url)
    content = req.read()
    with open(img_name, "wb") as f:
        f.write(content)


def main():
    num = 0
    gev_list = list()
    img_list = get_url("https://www.douyu.com/g_yz")
    for img_url in img_list:
        gev_obj = gevent.spawn(download, str(num)+".jpg", img_url)
        gev_list.append(gev_obj)
        num += 1
    gevent.joinall(gev_list)



if __name__ == "__main__":
    try:
        main()
    except Exception as res:
        print(res)

    
