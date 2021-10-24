import ccxt
import pprint
import requests
import threading
import time
import os, sys, subprocess
from pythonpancakes import PancakeSwapAPI
import datetime



def getTradePrice():

	tokens = ps.tokens('0x8420ce3a82fd1518ed898ff83b9b0b6ad470ad02')
	data = float(tokens['data']['price']) * 1000000000000000000
	return data
import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = 'your key'
secret_key = 'your key'
server_url = 'https://api.upbit.com'

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)

print(res.json())


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

class	AsyncTask:
	def	__init__(self):
		pass

	def	TaskA(self):
		now = datetime.datetime.now()
		print("시세확인중 현재시각 : " + str(now))
		current_price = float(getTradePrice())
		print("현재시세 : " + str(current_price))
		if current_price < targetprice:
			print(current_price)
			print("알람 발동")
			open_file('1.m4a')
			time.sleep(55)
			open_file('1.m4a')
			time.sleep(55)
			open_file('1.m4a')
			time.sleep(55)
			open_file('1.m4a')
			time.sleep(55)
			open_file('1.m4a')
			time.sleep(55)
			open_file('1.m4a')
			time.sleep(55)
			open_file('1.m4a')
			exit()
		threading.Timer(30,self.TaskA).start()

global targetprice
targetprice = float(input("알람가격을 설정하세요: "))
def	main():
	print ("알람설정가격 = " + str(targetprice))
	print ('Start Alarm')
	at = AsyncTask()
	at.TaskA()


if __name__ == '__main__':
	main()

