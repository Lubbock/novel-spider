# -*- coding: utf-8 -*-
from scrapy import cmdline
import os
import shutil


def merge_txt(fp):
    msort = []
    mtd = {}
    for root, dirs, files in os.walk(fp, topdown=False):
        for name in files:
            if type(name) == str:
                mtd[name.split(".")[0]] = name
                msort.append(int(name.split(".")[0]))
    msort.sort()
    pointer = 0
    try:
        with open(os.path.join(fp, "all.txt"), 'w') as s:
            for i in msort:
                t1 = mtd[str(i)]
                pointer = pointer + 1
                s.writelines(["##第{0}章".format(pointer)])
                with open(os.path.join(fp, t1), 'r') as f:
                    s.writelines(f.readlines())
                # os.remove(os.path.join(fp,t1))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # os.makedirs("./chap0")
    fp = "./chap0"
    # if not os.path.exists(fp):
    #     os.makedirs(fp)
    # cmdline.execute("scrapy crawl novelSpider".split())
    # merge_txt(fp)
    shutil.rmtree(fp)
