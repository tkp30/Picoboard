<h1>PicoboardAPI</h1>
<p>使用Python控制Scratch Picoboard</p>
<p></p>
<p>利用pyserial库，读取Scratch Picoboard的信息</p>
<p>下面是安装依赖项的代码（请在终端或CMD下运行）</p>
<code>pip install pyserial</code>
<p>如果报出错误，请尝试将pip改为pip3，或增加--user属性。<p>
<p>第二步（请在终端或CMD下运行）：</p>
<code>git clone https://github.com/XHG78999/Picoboard.git</code>
<p><em>注意：需要安装git。如果你没有安装，请安装git后再使用。安装方法自行百度，<strong>不要使用XX下载站的盗版！</strong></em></p>
<p>运行以上步骤后，将picoboard.py和PicoBoardAPI.py拷贝到项目目录中。</p>
<p>使用方法：</p>
<code>
"#-*- coding:utf-8 -*-"
<p></p>
"#!usr/bin/python3"
<p></p>
"from PicoBoardAPI import *"
<p></p>
"api=Api("COM4") #换成自己的端口，查看方法自行百度"
<p></p>
"api.getslider() #获取滑杆值"
<p></p>
"api.getlight() #获得亮度值"
<p></p>
"api.getsound() #获得声音值"
<p></p>
"api.getbutton() #获得按钮状态，True或False"
<p></p>
"api.getresistance("A") #参数A,B,C或D，返回该电阻传感器值"
<p></p>
"api.get() #以字典形式返回Picoboard值"
<p></p>
</code>
