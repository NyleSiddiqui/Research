from pynput import mouse
import sys
import time
global start
global start_location
global start_switch

def on_move(x, y):
	global start_switch
	global start_location
	if start_switch == 0:
		start_location = (x, y)
		start_switch += 1
	print((x, y), -1, -1, (start_location[0] - x, start_location[1] - y))

def on_click(x, y, button, pressed):
	global start
	if not pressed:                                                                                                     # Drag times?
		pass
	else:
		end = time.time()
		print((x, y), button, end-start, (start_location[0] - x, start_location[1] - y))
		start = time.time()
	

def on_scroll(x, y, dx, dy):
	if dy > 0:
		print((x, y), "up", -1, (-1, -1))
	else:
		print((x, y), "down", -1, (-1, -1))

if __name__ == '__main__':
	sys.stdout = open("Subject0.txt", 'w')
	start_switch = 0
	start = time.time()
	now = time.time()
	future = now + 3
	listener = mouse.Listener(
		on_move=on_move,
		on_click=on_click,
		on_scroll=on_scroll)
	listener.start()
	while time.time() < future:
		continue
	listener.stop()
	sys.stdout.close()

