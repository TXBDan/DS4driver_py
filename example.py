from DS4driver import DS4driver
import time

myDS4 = DS4driver('/dev/input/event0')


while True:
	
	myDS4.update()

	print('btn_square: %u' % myDS4.btn_square)
	
	time.sleep(0.01)
	



