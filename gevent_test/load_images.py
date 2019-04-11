import zlib,re,gevent,sys
from gevent import monkey
import chardet
import urllib.request

monkey.patch_all()

class Images(object):
    js = 0
    def __init__(self, one_url):
        '''接受网址返回图片列表'''
        response=urllib.request.urlopen(one_url)
        html=response.read()
        html = zlib.decompress(html, 16+zlib.MAX_WBITS)
        print(chardet.detect(html))
        html = html.decode("utf-8")
        self.img_list = re.findall(r"https://[ar]pic\.douyucdn\.cn/.{40,100}jpg",html)
        self.gev_list = list()

    @staticmethod
    def download(img_name, img_url):
        '''下载一个图片'''
        req = urllib.request.urlopen(img_url)
        content = req.read()
        with open(img_name, "wb") as f:
            f.write(content)
        print("----------%2d---------" % Images.js,end="\r")
        Images.js +=1


    def run(self):
        num = 0
        for img_url in self.img_list:
            gev_obj = gevent.spawn(self.download, str(num)+".jpg", img_url)
            self.gev_list.append(gev_obj)
            num += 1
        print("----------------%d----------" % len(self.gev_list))


def main():
    one_url = sys.argv[1]
    obj = Images(one_url)
    obj.run()
    try:
        print("开始下载")
        gevent.joinall(obj.gev_list)
        print("结束下载")
    except Exception as r:
        print(r)


if __name__ == "__main__":
    main()
    
