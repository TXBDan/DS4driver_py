# Dan Durusky
# Connect Sony DS4 controller via bluetooth using bluetoothctl
# hacked together from stuff on the internet
# For reference, see linux/input.h
import os, struct


# Iterate over the joystick devices.
print('Available devices:')

for fn in os.listdir('/dev/input'):
    if fn.startswith('event'):
        print('  /dev/input/%s' % (fn))


FORMAT = 'llHHi'
EVENT_SIZE = struct.calcsize(FORMAT)


# Open the joystick device.
fn = '/dev/input/event0'
print('Opening %s...' % fn)
event = open(fn, 'rb')


# Main event loop
while True:
    evbuf = event.read(EVENT_SIZE)
    if evbuf:
		
		(time_s, time_us, type, code, value) = struct.unpack(FORMAT, evbuf)
		
		#if type != 0 or code != 0 or value != 0:
		#	print("Event type %u, code %u, value %u at %d.%d" % \
		#		(type, code, value, time_s, time_us))
        
		if type == 0x01: #EV_KEY: (EV_ABS is 0x03
			
			if code == 0x130: #BTN_A
				#btn_square = ev.value;
				if value == 1:
					print("Square")
				
			if code == 0x131: #BTN_B:
				#btn_cross = ev.value;
				if value == 1:
					print("Cross")
				
			if code == 0x132: #BTN_C: 
				#btn_circle = ev.value;
				if value == 1:
					print("Circle")
				
			if code == 0x133: #BTN_X:
				#btn_triangle = ev.value;
				if value == 1:
					print("Triangle")
					
			if code == 0x134: #BTN_Y
				#btn_L1 = ev.value;
				if value == 1:
					print("L1")
			
			if code == 0x135: #BTN_Z
				#btn_R1 = ev.value;
				if value == 1:
					print("R1")
			
			if code == 0x136: #BTN_TL
				#btn_L2 = ev.value;
				if value == 1:
					print("L2")
			
			if code == 0x137: #BTN_TR
				#btn_R2 = ev.value;
				if value == 1:
					print("R2")
			
			if code == 0x13a: #BTN_SELECT
				#btn_L3 = ev.value;
				if value == 1:
					print("L3")
			
			if code == 0x13b: #BTN_START
				#btn_R3 = ev.value;
				if value == 1:
					print("R3")
			
			if code == 0x13d: #BTN_THUMBL
				#btn_touchpad = ev.value;
				if value == 1:
					print("Touchpad")
			
			if code == 0x139: #BTN_TR2
				#btn_options = ev.value;
				if value == 1:
					print("Options")
			
			if code == 0x13c: #BTN_MODE
				#btn_ps = ev.value;
				if value == 1:
					print("Playstation")
			
			if code == 0x138: #BTN_TL2
				#btn_share = ev.value;
				if value == 1:
					print("Share")
		
		if type == 0x03: #EV_ABS
						
			if code == 0x10: #ABS_HAT0X
				#btn_dleft = btn_dright = false;
				if value == -1:
					#btn_dleft = true;
					print("LEFT")
				if value == 1:
					#btn_dright = true;
					print("RIGHT")
			
			if code == 0x11: #ABS_HAT0Y
				#btn_dup = btn_ddown = false;
				if value == -1:
					#btn_dup = true;
					print("UP")
				if value == 1:
					#btn_ddown = true;
					print("DOWN")
					
			if code == 0x00: #ABS_X
				#leftH = value;	// 0 to 255, left to right
				print("leftH: %u" % value)
			
			if code == 0x01: #ABS_Y
				#leftV = value; // 0 to 255, top to bottom
				print("leftV: %u" % value)
			
			if code == 0x02: #ABS_Z 
				#rightH = value;	// 0 to 255, left to right
				print("rightH: %u" % value)
			
			if code == 0x05: #ABS_RZ
				#rightV = value; // 0 to 255, top to bottom
				print("rightV: %u" % value)
			
			if code == 0x03: #ABS_RX 
				#L2analog = value;	// 0 to 255, left to right
				print("L2analog: %u" % value)
			
			if code == 0x04: #ABS_RY
				#R2analog = value; // 0 to 255, top to bottom
				print("R2analog: %u" % value)
			
