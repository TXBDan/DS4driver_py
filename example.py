from DS4driver import DS4driver
import time

print("DS4driver Example")

myDS4 = DS4driver('/dev/input/event0')

leftV_p = 0
leftH_p = 0
rightV_p = 0
rightH_p = 0
R2analog_p = 0
L2analog_p = 0

while True:
	
	myDS4.update()

	if (myDS4.btn_square):
		print("Square")
	if (myDS4.btn_cross):
		print("Cross")
	if (myDS4.btn_circle):
		print("Circle")
	if (myDS4.btn_triangle):
		print("Triangle")
		
	if (myDS4.btn_dleft):
		print("Left")
	if (myDS4.btn_dright):
		print("Right")
	if (myDS4.btn_dup):
		print("Up")
	if (myDS4.btn_ddown):
		print("Down")
		
	if (myDS4.btn_L1):
		print("L1")
	#if (myDS4.btn_L2):
	#	print("L2")
	if (myDS4.btn_L3):
		print("L3")
	if (myDS4.btn_R1):
		print("R1")	
	#if (myDS4.btn_R2):
	#	print("R2")
	if (myDS4.btn_R3):
		print("R3")

	if (myDS4.btn_touchpad):
		print("Touchpad")
	if (myDS4.btn_options):
		print("Options")	
	if (myDS4.btn_ps):
		print("PS")
	if (myDS4.btn_share):
		print("Share")		
	
	if( abs(myDS4.leftV - leftV_p) > 1):
		print("LeftV: ", myDS4.leftV)
		leftV_p = myDS4.leftV
		
	if( abs(myDS4.leftH - leftH_p) > 1):
		print("LeftH: ", myDS4.leftH)
		leftH_p = myDS4.leftH
		
	if( abs(myDS4.rightV - rightV_p) > 1):
		print("RightV: ", myDS4.rightV)
		rightV_p = myDS4.rightV
		
	if( abs(myDS4.rightH - rightH_p) > 1):
		print("rightH: ", myDS4.rightH)
		rightH_p = myDS4.rightH

	if( abs(myDS4.L2analog - L2analog_p) > 1):
		print("L2analog: ", myDS4.L2analog)
		L2analog_p = myDS4.L2analog
		
	if( abs(myDS4.R2analog - R2analog_p) > 1):
		print("rightH: ", myDS4.R2analog)
		R2analog_p = myDS4.R2analog

	
	time.sleep(0.02)
	



