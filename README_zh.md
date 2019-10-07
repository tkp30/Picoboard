使用Python来控制PicoBoard。
需要安装pyserial作为依赖程序：
pip install pyserial
需要drewarnett的Picoboard扩展。
该程序只是提供了一个API，可以更方便的调用。例如，Api("COM4").getslider()返回的是像Scratch里的0-100，而不是0-1024。
使用方法：
from PicoBoardAPI import Api #导入他
p=Api("COM4") #端口号
p.getslider() #返回滑杆的值
p.getbutton() #返回按钮传感器的值，True或False
p.getsound() #返回声音传感器的值
p.getlight() #返回亮度传感器的值
p.getresistance("A") #参数：A，B，C或D。返回该电阻传感器的值
p.get() #以字典形式返回所有值
已知一个Bug：在Windows下（至少在我的电脑里是这样的），插入设备5秒后，将报出拒绝访问错误。
这可能是设备管理器后台进程以及安全中心的检测机制占用了调用权，导致进程无法访问。
我不知道在其它系统上是否会有错误，如果你是Mac或Linux的话，请向我提供txt数据，将Shell的结果放到里面。
