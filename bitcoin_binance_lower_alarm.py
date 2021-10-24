import ccxt
import pprint
import requests
import threading
import time
import os, sys, subprocess
from pythonpancakes import PancakeSwapAPI
import datetime


### this part is for binance api

with open("api.txt") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret  = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

def getTradePrice():

	with open("api.txt") as f:
		lines = f.readlines()
		api_key = lines[0].strip()
		secret  = lines[1].strip()

	binance = ccxt.binance(config={
		'apiKey': api_key,
		'secret': secret,
		'enableRateLimit': True,
		'options': {
			'defaultType': 'future'
		}
	})

	btc = binance.fetch_ticker("BTC/USDT")
	return btc['close']


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
		threading.Timer(3,self.TaskA).start()

global targetprice
targetprice = float(input("알람가격을 설정하세요: "))
def	main():
	print ("알람설정가격 = " + str(targetprice))
	print ('Start Alarm')
	at = AsyncTask()
	at.TaskA()


if __name__ == '__main__':
	main()

