from pynput import mouse
import sys
import time
global start
running = True

def on_move(x, y):
	print((x, y), -1, -1, (-1, -1))

def on_click(x, y, button, pressed):
	global start
	if not pressed:
		pass
	else:
		end = time.time()
		print((x, y), button, end-start)
		start = time.time()
	

def on_scroll(x, y, dx, dy):
	if dy > 0:
		print((x, y), "up", -1, (-1, -1))
	else:
		print((x, y), "down", -1, (-1, -1))

if __name__ == '__main__':
	start = time.time()
	now = time.time()
	future = now + 3
	listener = mouse.Listener(
		on_move=on_move,
		on_click=on_click,
		on_scroll=on_scroll)
	listener.start()
	# sys.stdout = open("Subject0.txt", 'w')
	while time.time() < future:
		continue
	# print("end")
	# sys.stdout.close()

