# -*- coding: cp936 -*-
import urllib  
import urllib2  

url = 'http://electsys.sjtu.edu.cn/edu/index.aspx'  
  
values = {'txtUserName' : '51203g09244',  
          'txtPwd' : '527woaibamayxt',  
          'rbtnLst' : '1' }  

data = urllib.urlencode(values) # ���빤��
req = urllib2.Request(url, data)  # ��������ͬʱ��data��
response = urllib2.urlopen(req)  #���ܷ�������Ϣ
the_page = response.read()  #��ȡ����������
