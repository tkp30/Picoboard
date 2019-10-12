import platform #内置
import zipfile #内置
import gzip #内置
import os #内置

import requests #pip install requests
from picoboard import * #pip install https://github.com/drewarnett/pypicoboard/archive/master.zip

class Api(object):
    def __init__(self,usbport="COM4"):
        '''初始化，相当于create(端口)'''
        self.usb=usbport
        self.createpico(self.usb)
    def installer():
        '''安装驱动安装包'''
        if platform.system()=="Windows":
            try:
                print("正在下载安装包")
                r=requests.get("http://www.picocricket.com/picoboard-drivers/Windows_CDM_2_06_00.zip")
                with open("installer.zip","wb") as f:
                    f.write(r.content)
                print("下载成功")
            except:
                print("网络不给力，请稍后再试")
                return None
            print("正在解压安装文件")
            fz = zipfile.ZipFile("installer.zip", 'r')
            for file in fz.namelist():
                fz.extract(file, "./installer/windows/")
            print("解压成功，正在安装......")
            os.popen("installer/CDM_2_06_00.exe").read()
            print("安装成功！")
        elif platform.system()=="Darwin":
            try:
                print("正在下载安装包")
                r=requests.get("http://www.picocricket.com/picoboard-drivers/FTDIUSBSerialDriver_v2_2_14.dmg")
                with open("installer.dmg","wb") as f:
                    f.write(r.content)
                print("下载成功")
            except:
                print("网络不给力，请稍后再试")
                return None
            print("请到目录下installer.dmg文件打开后运行其中的文件完成驱动安装。")
        elif "Linux" in platform.system():
            try:
                print("正在下载安装包")
                r=requests.get("http://www.picocricket.com/picoboard-drivers/USBLinux_1_5_0.gz")
                with open("installer.gz","wb") as f:
                    f.write(r.content)
                print("下载成功")
            except:
                print("网络不给力，请稍后再试")
                return None
            gfile=gzip.GzipFile("USBLinux_1_5_0.gz")
            open("./installer/linux/installer.exe","w+"),write(gfile.read())
            gfile.close()
        else:
            print("找不到你的系统所需要的驱动。如果你是虚拟机，请前往http://www.picocricket.com/picoboardsetupUSB.html查看适合你的虚拟机安装的系统的驱动程序。")    
    def createpico(self,USB):
        '''创建PicoBoard对象'''
        self.usb=USB
        self.pico=PicoBoard(USB)
    def getslider(self):
        '''获取滑杆数据'''
        try:
            return int(self.pico.read()["slider"]/10.23)
        except:
            self.pico.__init__(self.usb)
            return int(self.pico.read()["slider"]/10.23)
    def getlight(self):
        '''获取亮度数据'''
        try:
            return int(self.pico.read()["light"]/10.23)
        except:
            self.pico.__init__(self.usb)
            return int(self.pico.read()["light"]/10.23)
    def getsound(self):
        '''获取声音数据'''
        try:
            return int(self.pico.read()["sound"]/10.23)
        except:
           self.pico.__init__(self.usb)
           return int(self.pico.read()["sound"]/10.23)
    def getbutton(self):
        '''获取按钮数据'''
        try:
            return not bool(self.pico.read()["button"])
        except:
            self.pico.__init__(self.usb)
            return not bool(self.pico.read()["button"])
    def getresistance(self,port):
        '''获取电阻数据'''
        try:
            return int(self.pico.read()[port]/10.23)
        except:
            self.pico.__init__(self.usb)
            return int(self.pico.read()[port]/10.23)
    def get(self):
        '''以字典方式返回数据'''
        try:
            return self.pico.read()
        except:
            del self.pico
            self.pico=PicoBoard(self.usb)
            #self.pico.__init__(self.usb)
            return self.pico.read()
if __name__=="__main__":
    p=Api()
    print("======Test:on Windows 10 1903 Chinese version======")
    while True:
        if not p.get()["button"]:
            print("Button clicked")


        
        
        
            
            
        
