## 项目目的
你是否会有本人不在办公室或者实验室而电脑还运行着，但是某个时刻需要关闭的情况呢？这个小项目就是为了完成这个功能，使用微博进行远程关机

## 项目依赖
- 模拟登陆+页面解析：requests+pyexecjs+beautifulsoup

 - >pip install requests
 - >pip install bs4
 - >pip install PyExecJS

- 命令行解析：docopt
 - >pip install docopt
 
- phantomjs
 - windows:在[phantomjs官网](http://phantomjs.org/)下载它，并且把它的路径添加到环境变量中
 - ubuntu：*sudo apt-get install phantomjs* 或者到官网下载并且添加到环境变量中
 
## 思路
1. 定时模拟登陆（定时是因为微博cookie**24小时**失效）,关于模拟登陆可以参看[我的博文](http://www.rookiefly.cn/detail/83)和[github项目](https://github.com/ResolveWang/smart_login)
2. 定时(10分钟)获取最新一条微博，并把发布时间和系统时间做比较，如果相差半个小时以内，就执行关机命令
3. 让程序开机启动，随时监听

## 使用
- 命令行
> python pc_shutdown.py name weibo_account password weibo_password

- exe文件(我使用的rsa库直接登陆(而非phantomjs方式)，所以如果只是试试效果，那么就可以用这个
> pc_shutdown.exe name weibo_account password weibo_password

- 微博状态
> 关机 20   

这里"关机"两个字是必须的，"20"是20分钟过后关机，中间用空格隔开，如果不带参数，那么立即关机

