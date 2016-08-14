# Dan Durusky - 2016
# Connect Sony DS4 controller via bluetooth using bluetoothctl
# For reference, see linux/input.h
import evdev

class DS4driver:
	
	def __init__(self,dev):
			self.dev = dev
			self.leftV = 0
			self.leftH = 0
			self.rightV = 0
			self.rightH = 0
			self.L2analog = 0
			self.R2analog = 0
			self.btn_dleft = False
			self.btn_dright = False
			self.btn_dup = False
			self.btn_ddown = False
			self.btn_cross = False
			self.btn_circle = False
			self.btn_triangle = False
			self.btn_square = False
			self.btn_L1 = False
			self.btn_L2 = False
			self.btn_L3 = False
			self.btn_R1 = False
			self.btn_R2 = False
			self.btn_R3 = False
			self.btn_touchpad = False
			self.btn_options = False
			self.btn_ps = False
			self.btn_share = False
			
			self.device = evdev.InputDevice(self.dev)
			print(self.device.fn, self.device.name, self.device.phys)
			if 'Wireless Controller' in self.device.name:
				print('Found DS4 controller as %s' % self.device.fn)
			else:
				print('DS4 not found!')
		

	# Update events, buttons
	def update(self):
		try:
			for event in self.device.read():
				
				if event.type == evdev.ecodes.EV_KEY:
					
					if event.code == 0x130: #BTN_A
						self.btn_square = event.value
						
					elif event.code == 0x131: #BTN_B:
						self.btn_cross = event.value
						
					elif event.code == 0x132: #BTN_C: 
						self.btn_circle = event.value
						
					elif event.code == 0x133: #BTN_X:
						self.btn_triangle = event.value
							
					elif event.code == 0x134: #BTN_Y
						self.btn_L1 = event.value
					
					elif event.code == 0x135: #BTN_Z
						self.btn_R1 = event.value;
					
					elif event.code == 0x136: #BTN_TL
						self.btn_L2 = event.value
					
					elif event.code == 0x137: #BTN_TR
						self.btn_R2 = event.value
					
					elif event.code == 0x13a: #BTN_SELECT
						self.btn_L3 = event.value
					
					elif event.code == 0x13b: #BTN_START
						self.btn_R3 = event.value
					
					elif event.code == 0x13d: #BTN_THUMBL
						self.btn_touchpad = event.value
					
					elif event.code == 0x139: #BTN_TR2
						self.btn_options = event.value
					
					elif event.code == 0x13c: #BTN_MODE
						self.btn_ps = event.value
					
					elif event.code == 0x138: #BTN_TL2
						self.btn_share = event.value
					
				if event.type == 0x03: #EV_ABS
									
					if event.code == 0x10: #ABS_HAT0X
						if event.value == -1:
							self.btn_dleft = True
						elif event.value == 1:
							self.btn_dright = True
						else:
							self.btn_dleft = False
							self.btn_dright = False
					elif event.code == 0x11: #ABS_HAT0Y				
						if event.value == -1:
							self.btn_dup = True
						elif event.value == 1:
							self.btn_ddown = True
						else:
							self.btn_dup = False
							self.btn_ddown = False
							
					elif event.code == 0x00: #ABS_X
						self.leftH = event.value	# 0 to 255, left to right
					
					elif event.code == 0x01: #ABS_Y
						self.leftV = event.value # 0 to 255, top to bottom
					
					elif event.code == 0x02: #ABS_Z 
						self.rightH = event.value	# 0 to 255, left to right
					
					elif event.code == 0x05: #ABS_RZ
						self.rightV = event.value # 0 to 255, top to bottom
					
					elif event.code == 0x03: #ABS_RX 
						self.L2analog = event.value	# 0 to 255, left to right
					
					elif event.code == 0x04: #ABS_RY
						self.R2analog = event.value # 0 to 255, top to bottom
						
		except IOError:
			pass
