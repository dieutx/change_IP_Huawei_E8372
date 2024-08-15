#pip install huawei-modem-api-client
import requests
import time
import os
import huaweisms.api.user
import huaweisms.api.wlan
import huaweisms.api.sms
import huaweisms.api.dialup

ctx = huaweisms.api.user.quick_login("asd", "pass")
# print(ctx)
# output: <ApiCtx modem_host=192.168.8.1>
print('started. waiting .....')

resultBefore = requests.get('https://checkip.amazonaws.com').text.strip()

huaweisms.api.dialup.disconnect_mobile(ctx)
huaweisms.api.dialup.connect_mobile(ctx)

time.sleep(20)
resultAfter = None
while resultAfter is None:
	try:
		# connect
		resultAfter = requests.get('https://checkip.amazonaws.com').text.strip()
	except:
		time.sleep(3)
		pass

os.system('cmd.exe /c ipconfig/flushdns')
os.system('cmd.exe /c ipconfig/release')
os.system('cmd.exe /c ipconfig/renew')
time.sleep(1)

print('\x1b[6;30;42m' + 'IP before: {}\n'.format(resultBefore) + '\x1b[0m')
print('\x1b[6;30;42m' + 'IP after: {}'.format(resultAfter) + '\x1b[0m')

exit
