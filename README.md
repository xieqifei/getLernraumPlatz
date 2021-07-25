# 自习室预定程序getLernraumPlatz (aufgegeben)
## Aktuelles Programm steht Ihnen in folgendem Repository zur Verfügung!  
[AutoLernraum](https://github.com/xieqifei/AutoLernraum)
一个Web自动化程序，用于从RWTH Lernraum订座网站上获取一个自习位置。设置定时任务，保证每个工作日都能获得自习位置。a web automatic program to get a place in RWTH-Lernraum

![](https://i.loli.net/2020/10/05/QihqIymWxtpC5S2.jpg)

# 1：使用协议：

你必须知晓，使用本程序，是为了帮助那些勤于学习的同学，简化预定座位步骤，来快速获得自习室位置。你不能恶意修改程序，影响自习室预定的正常秩序。如果你通过恶意修改本程序而干扰学校正常的运行秩序，你可能承担法律风险。

程序不会干扰，通过浏览器正常预定座位的同学。已通过程序手段，延迟了本程序预定的时间，使用本程序会比同时手动进行预定的同学更慢获取到座位。

# 2：使用指南

> 此使用指南，具有一定技术难度。具体过程报错，可自行google解决。

1. 在你的电脑上，安装python环境。python版本3.0以上。[Windows安装Python（图解）](http://c.biancheng.net/view/4161.html)
2. [安装Chrome浏览器](https://www.google.cn/chrome/index.html)。
3. 使用python包管理器，安装selenium库。windows下，搜索cmd，运行命令提示符窗口，输入

```shell
pip3 install selenium
```

3. 下载安装chrome浏览器驱动，并将驱动配置到环境变量中。[selenium 安装与 chromedriver安装](https://www.cnblogs.com/lfri/p/10542797.html)
4. 将getplatz.py程序下载到你的计算机。https://github.com/xieqifei/getLernraumPlatz/archive/main.zip 解压后，getplatz.py程序就在文件夹内。
5. 打开并按照程序内的备注，修改getplatz.py中的urinfo信息。
6. 在cmd命令提示符窗孔中输入指令，运行程序，即可完成抢座。5分钟后，你会收到学校发送的预定成功邮件。

```shell
python 程序保存目录\getplatz.py
```

比如将程序保存到了桌面，

```shell
python C:\Users\你的用户名\Desktop\main\getplatz.py
```
程序运行时，会出现运行提示。如果预定成功，几分钟之后，会收到预定成功的邮件。当然，如果你在预定的网站上看到，今日预定已经没有了，自然会抢座失败。

7. 在你的计算机上设置定时运行程序，建议设置的定时运行时间为，每周天-周四，上午八点。抢座后，大约8:05会收到学校发送的定座成功邮件。邮件中的链接，打开后就是进入自习室的二维码凭证。[win10设置定时任务的方法](https://www.jb51.net/os/win10/735135.html)

# 3：程序说明

程序会优先预定Bibliothek 2的座位，然后是Bbliothek 1，最后才是Semi temp。因为Semi temp不是每个座位都有插座，所以我将他放到最后预定。

如果你对Semitemp情有独钟，可以删除程序中的`inputs.reverse()`。这样会优先预定semi temp的位置。

设置定时任务，可以为你每天抢座，但是你需要保证你的电脑在设置的任务时间处于开机状态。。如果你有树莓派，可能会为你省一笔电费。。如果你本身就是一个勤奋的同学，比如你设置的8点抢座，而你在7点就已经开始使用电脑学习，那么你可能并不需要让计算机在你晚上睡觉的时候保持激活。

程序我有在Linux和Windows上都运行过，都是没有问题的。Mac系统，也是没有什么问题的，不过安装chrome驱动和设置环境变量，需要自行google教程。
