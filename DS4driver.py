# Dan Durusky - 2016
# Connect Sony DS4 controller via bluetooth using bluetoothctl
# For reference, see linux/input.h
import evdev


# List available event devices.
print('Available devices:')
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
	print(device.fn, device.name, device.phys)
	if 'Wireless Controller' in device.name: #grabs first wireless controller
		print('Found DS4 controller as %s' % device.fn)
		break
		

# Loop forever waiting for events
for event in device.read_loop():
	
	if event.type == evdev.ecodes.EV_KEY:
       	
		if event.code == 0x130: #BTN_A
			#btn_square = event.value;
			if event.value == 1:
				print("Square")
			
		elif event.code == 0x131: #BTN_B:
			#btn_cross = event.value;
			if event.value == 1:
				print("Cross")
			
		elif event.code == 0x132: #BTN_C: 
			#btn_circle = event.value;
			if event.value == 1:
				print("Circle")
			
		elif event.code == 0x133: #BTN_X:
			#btn_triangle = event.value;
			if event.value == 1:
				print("Triangle")
				
		elif event.code == 0x134: #BTN_Y
			#btn_L1 = event.value;
			if event.value == 1:
				print("L1")
		
		elif event.code == 0x135: #BTN_Z
			#btn_R1 = event.value;
			if event.value == 1:
				print("R1")
		
		elif event.code == 0x136: #BTN_TL
			#btn_L2 = event.value;
			if event.value == 1:
				print("L2")
		
		elif event.code == 0x137: #BTN_TR
			#btn_R2 = event.value;
			if event.value == 1:
				print("R2")
		
		elif event.code == 0x13a: #BTN_SELECT
			#btn_L3 = event.value;
			if event.value == 1:
				print("L3")
		
		elif event.code == 0x13b: #BTN_START
			#btn_R3 = event.value;
			if event.value == 1:
				print("R3")
		
		elif event.code == 0x13d: #BTN_THUMBL
			#btn_touchpad = event.value;
			if event.value == 1:
				print("Touchpad")
		
		elif event.code == 0x139: #BTN_TR2
			#btn_options = event.value;
			if event.value == 1:
				print("Options")
		
		elif event.code == 0x13c: #BTN_MODE
			#btn_ps = event.value;
			if event.value == 1:
				print("Playstation")
		
		elif event.code == 0x138: #BTN_TL2
			#btn_share = event.value;
			if event.value == 1:
				print("Share")
		
	if event.type == 0x03: #EV_ABS
						
		if event.code == 0x10: #ABS_HAT0X
			#btn_dleft = btn_dright = false;
			if event.value == -1:
				#btn_dleft = true;
				print("LEFT")
			elif event.value == 1:
				#btn_dright = true;
				print("RIGHT")
		
		elif event.code == 0x11: #ABS_HAT0Y
			#btn_dup = btn_ddown = false;
			if event.value == -1:
				#btn_dup = true;
				print("UP")
			elif event.value == 1:
				#btn_ddown = true;
				print("DOWN")
				
		elif event.code == 0x00: #ABS_X
			#leftH = value;	// 0 to 255, left to right
			print("leftH: %u" % event.value)
		
		elif event.code == 0x01: #ABS_Y
			#leftV = value; // 0 to 255, top to bottom
			print("leftV: %u" % event.value)
		
		elif event.code == 0x02: #ABS_Z 
			#rightH = value;	// 0 to 255, left to right
			print("rightH: %u" % event.value)
		
		elif event.code == 0x05: #ABS_RZ
			#rightV = value; // 0 to 255, top to bottom
			print("rightV: %u" % event.value)
		
		elif event.code == 0x03: #ABS_RX 
			#L2analog = value;	// 0 to 255, left to right
			print("L2analog: %u" % event.value)
		
		elif event.code == 0x04: #ABS_RY
			#R2analog = value; // 0 to 255, top to bottom
			print("R2analog: %u" % event.value)
	
