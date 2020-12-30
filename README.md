# 基于PN532的信息管理系统

```
├─main.spec （pyinstaller打包时会自动生成的配置文件）
├─README.md (部署说明)
├─main  (源程序文件夹)
|  ├─ComboBox.py
|  ├─icon.py
|  ├─main.py
|  ├─rfid.db
|  ├─rfid.py
|  ├─sql.py
|  ├─src
|  |  ├─database.py
|  |  ├─database.ui （数据库显示界面）
|  |  ├─dialog.py
|  |  ├─dialog.ui （录入卡号数据的弹窗）
|  |  ├─SLmge.py
|  |  ├─SLmge.ui （主程序ui）
|  |  ├─tool.py
├─icon （程序的logo）
|  ├─icon.ico
|  ├─icon.qrc
|  └icon.svg
├─dist （pyinstaller打包成功后生成的exe）
|  ├─main.exe 
├─build （pyinstaller打包时生成的依赖文件夹）

```

## 使用方法以及说明

### 运行

- 程序的入口为`main.py`;
- 打开项目文件夹执行`python ./main/main.py`。
- 使用IDE打开

### 打包

- `pip install pyinstaller`
- `pyinstaller -F -w ./main/main.py -i ./icon/icon.ico`
- 如需要显示终端可去除`-w`

### 项目说明

1. main文件夹

   该文件夹存放了所有的项目源代码

    - **src文件夹**

      存放了使用`QtDesign`设计的三个页面。

        - 运行`tool.py`能够自动将当前目录下的所有`ui`文件转换为`.py`

    - `main.py`做为主程序的入口，继承了`src`文件夹中的三个图形界面的类。

    - `rfid.py`中存放了与`PN532模块`进行串口通信的源码。

    - `sql.py`中存放了对`sqlite`数据库进行增删改查的源码。

    - `main.py`中还有一个QT的线程类，专门用来处理用户打开串口后与`PN532`进行交互通信。防止串口通信阻塞图形界面的正常工作。

    - 线程和主程序之间实现了信号槽通信。

2. icon文件夹

    - 存放了程序的运行时显示的logo,打包为exe时用的到。

    - 如要替换logo请在项目根目录下执行

      `pyrcc5 -o ./main/icon.py ./icon/icon.qrc`



