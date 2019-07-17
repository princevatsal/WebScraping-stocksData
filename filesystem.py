import os,datetime
from datetime import date
def findingdate():
	r=os.listdir('realdata')
	data=[]
	for i in range (len(r)):
		if(r[i][0:13]=='EURUSD_Ticks_'):
			data.append(r[i][13:23])
	for i in range(len(data)):
		temp=date(int(data[i][6:10]),int(data[i][3:5]),int(data[i][0:2]))
		data[i]=temp
	if(len(data)==0):
		big='empty'
	else:
		big=data[0]
		for i in range(len(data)):
			if(data[i]>big):
				big=data[i]
	if(big=='empty'):
		reqdate=date(2019,1,1)
	else:
		big+=datetime.timedelta(days=1)
		reqdate=big
	return(reqdate)
print(findingdate())
print(findingdate())
print(findingdate())