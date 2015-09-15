# -*- coding: utf-8 -*-
import re
import os
import time
from app import db
from app.modles import Mark
from config import basedir

def doitem(item):
    prog = re.compile(r"#(.*?)的标注 \| 添加于 (.*?)年(.*?)月(.*?)日")
    result = prog.findall(item)

    position = result[0][0]
    date = "%s-%s-%s" % (result[0][1], result[0][2], result[0][3])
    return position, date


def create_contents(fname):
    src = open(fname, "r", encoding="utf-8")
    src_content = src.readlines()
    content_list = []

    # (0, 'JavaScript高级程序设计(第3版) (图灵程序设计丛书) (泽卡斯（Zakas. Nicholas C.）)\n')
    # (1, '- 您在位置 #234-235的标注 | 添加于 2015年4月24日星期五 上午8:02:06\n')
    # (2, '\n')
    # (3, '原版的ISBN是978-1-118-02669-4。\n')
    # (4, '==========\n')

    for line in enumerate(src_content):
        if line[0] % 5 == 2 or line[0] % 5 == 4:
            continue
        if line[0] % 5 == 0:
            temp = []
            temp.append(line[1][:-1])
            continue
        if line[0] % 5 == 1:
            if line[1].find("书签") > -1 or line[1].find("笔记") > -1:
                continue
            else:
                item = doitem(line[1])
                temp.append(item[0])
                temp.append(item[1])
        if line[0] % 5 == 3:
            temp.append(line[1][0:-1])
            if len(temp) != 4:
                continue
            else:
                content_list.append(tuple(temp))

    return content_list


def init_db():
    db.drop_all(bind=['Mark'])
    db.create_all(bind=['Mark'])
    content_list = create_contents(os.path.join(basedir, "My Clippings.txt"))
    for line in content_list:
        mark = Mark(line[0], line[1], line[2], line[3])
        db.session.add(mark)
    db.session.commit()

    print("数据库创建完成")
    return True


if __name__ == "__main__":
    content_list = create_contents(os.path.join(basedir, "My Clippings.txt"))
    for line in content_list:
        print(line)
