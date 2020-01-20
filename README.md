# 查看
## <span id="view_version">查看pip支持版本方法</span>
### AMD64
* import pip._internal
* print(pip._internal.pep425tags.get_supported())
### WIN32
* import pip
* print(pip.pep425tags.get_supported())

# 安装
pip3 install psycopg2

# 升级
## 升级PIP
### 在Linux或macOS上：
* pip install -U pip
### 在Windows 4上：
* python -m pip install -U pip

#问题

## 执行pip或pip3命令时报错
* pip failed to create process.
### 错误原因
* 为了对应Linux下的python3命令，windows下手动修改了python安装文件名称，
将安装目录下(E:\Python\Python38)的python.exe、pythonw.exe文件名改名成了python3.exe、pythonw3.exe
### 解决方法
* 1.打开安装目录下的Scripts(E:\Python\Python38\Scripts)文件夹
* 2.找到pip-script.py文件，并打开
* 3.修改第一行内容并保存(#!E:\Python\Python38\python.exe修改为#!E:\Python\Python38\python3.exe)

## 安装psycopg2报错
* error: Microsoft Visual C++ 14.0 is required. 
Get it with "Microsoft Visual C++ Build Tools": 
https://visualstudio.microsoft.com/downloads/
###解决方法
* [安装Twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)
* 找到python对应的版本(python对应的是32还是64位版本)，选择对应的Twisted版本进行安装
* python3 -m pip install .\Twisted-19.10.0-cp38-cp38-win_amd64.whl
* 注：待安装的whl文件必须放在当前命令执行路径下

## 安装Twisted报错
* Requirement 'D:/Downloads/Twisted?19.10.0?cp38?cp38?win_amd64.whl' looks like a filename, but the file does not exist
Twisted?19.10.0?cp38?cp38?win_amd64.whl is not a valid wheel filename.
### 解决方法
* pip3 install wheel
* 修改pip3 install Twisted-19.10.0-cp38-cp38-win_amd64.whl命令为python3 -m pip install .\Twisted-19.10.0-cp38-cp38-win_amd64.whl

## 安装Twisted报错
* Twisted-19.10.0-cp38-cp38-win_amd64.whl is not a supported wheel on this platform.
### 解决方法
* 查看pip支持版本，选择合适的版本

## 查看pip支持版本方法报错
* module 'pip' has no attribute 'pep425tags'
### 解决方法
[参考本页'查看pip支持版本方法'](#view_version, "查看pip支持版本方法")

## 升级pip失败
* The 'pip==19.3.1' distribution was not found and is required by the application
### 错误原因
* 在windows下使用了pip install -U pip命令进行升级
### 解决方法
* 使用windows升级pip命令
* python -m pip install -U pip

# 资料
## 参考资料
* [flask](http://docs.jinkan.org/docs/flask/index.html)