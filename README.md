# kindle标注处理程序

本程序还不完善，推荐使用[http://clippings.io/](http://clippings.io/)

> 平时使用kindle时经常会标注许多内容，这些内容有许多有用的笔记，但是导入到电脑上很不方便，于是便开发了这个程序，可以方便的将kindle的标注内容导出，同时还可以针对标注内容添加批注或笔记，方便对知识进行整理

整理kindle标注内容，基于`python3`、`flask`开发


##主要功能
1. 删除无用的标注信息
2. 对标注信息添加批注、笔记

##使用方法
1. 初始化数据库
    1.1 将kindle连上电脑，在`document`文件夹中找到标注文件`My Clippings.txt`
    1.2 将kindle的标注文件导入至程序的根目录中
    1.3 执行命令`python manage.py shell`
    > 可能需要先执行`pip install requirements.txt`安装需要的包

    1.4 然后执行`init()`完成数据库的初始化

2. 开启程序
    2.1 执行`python manage.py runserver`
    2.2 浏览器访问`127.0.0.1:5000`

##后续添加功能
1. 给笔记添加标签功能，方便到时候查阅
2. 增强易用性，主要包括对标注或笔记按书名、标签名、时间等信息进行分类整理查看
3. 增加批量化操作
4. 如若有好的建议可以[邮件][1]或者[私信我][2]

---
>很久前的。。。

写的都差不多的程序了，却不小心删除了源码
数据库了使用的Sqlite3，用flask却发现不知道怎么开多线程
心塞啊心塞


[1]: mailto:lleohao@qq.com
[2]: http://weibo.com/lleohao
