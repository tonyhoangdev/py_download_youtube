#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : download file
"""
import re, time, sys
from urllib.request import urlopen, Request, urlretrieve
from bs4 import BeautifulSoup

####
def download(url, name = "0"):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req).read()
        # print(url_req.info())

        with open(name, "wb") as f_out:
            f_out.write(resp)
    except:
        print("404: Not found")
        

if __name__=="__main__":  
    url = "https://forums.voz.vn/showthread.php?t=7382956"  

    if (len(sys.argv) < 2):
        print("Link empty!")
        sys.exit(0) 
    url = sys.argv[1]
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    url_req = urlopen(req)
    resp = url_req.read()

    soup = BeautifulSoup(resp, 'html.parser')   
    tags = soup('img')
    listImg = []
    for tag in tags:
        src = tag.get('src', None)
        if (re.findall("https://scontent", src)):
            listImg.append(src)
            # print(src)

    pre = 0
    print("==== count: ", len(listImg))
    for i in listImg:
        preStr = "{0:03}".format(pre)
        print(preStr, "====", i)
        print("[start]: ", i)
        name = re.split("\?", re.split("/", i)[-1])[0]
        download(i, preStr + "_" + name)
        print("[done]: ", i)
        pre = pre + 1
        time.sleep(1)
