import zlib,re,gevent,sys
from gevent import monkey
import chardet
import urllib.request

monkey.patch_all()

class Images(object):
    the_len = 0
    def __init__(self, one_url):
        '''接受网址返回图片列表'''
        response=urllib.request.urlopen(one_url)
        html=response.read()
        html = zlib.decompress(html, 16+zlib.MAX_WBITS)
        print(chardet.detect(html))
        html = html.decode("utf-8")
        self.img_list = re.findall(r"https://[ar]pic\.douyucdn\.cn/.{40,60}jpg",html)
        Images.the_len = len(self.img_list)
        self.num = 1


    def download(self, img_name, img_url):
        '''下载一个图片'''
        req = urllib.request.urlopen(img_url)
        content = req.read()
        with open(img_name, "wb") as f:
            f.write(content)
        # print("下载进度==> %2.f%%" % ((self.num/Images.the_len)*100), end="\r")
        print("===========")

    def run(self):
        print("------图片总数:%d------" % Images.the_len)
        l = list()
        for img_url in self.img_list:
            gev_obj = gevent.spawn(self.download, str(self.num)+".jpg", img_url)
            l.append(gev_obj)
            self.num += 1
        [i.join() for i in l]
        print("over")


def main():
    one_url = sys.argv[1]
    obj = Images(one_url)
    obj.run()


if __name__ == "__main__":
    main()
    
