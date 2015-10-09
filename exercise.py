# -*- coding: cp936 -*-
import urllib  
import urllib2  

url = 'http://electsys.sjtu.edu.cn/edu/index.aspx'  
  
values = {'txtUserName' : '51203g09244',  
          'txtPwd' : '527woaibamayxt',  
          'rbtnLst' : '1' }  

data = urllib.urlencode(values) # 编码工作
req = urllib2.Request(url, data)  # 发送请求同时传data表单
response = urllib2.urlopen(req)  #接受反馈的信息
the_page = response.read()  #读取反馈的内容
