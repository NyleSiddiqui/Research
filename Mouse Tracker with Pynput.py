from pynput import mouse
import pygame
import sys
import time
global start
global start_location
global start_switch
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
global count

def on_move(x, y):
	global count
	global start_switch
	global start_location
	if start_switch == 0:
		start_location = (x, y)
		start_switch += 1
	print((x, y), ';', -1, ';', -1, ';', (start_location[0] - x, start_location[1] - y), ';', 0)

def on_click(x, y, button, pressed):
	global start
	if not pressed:                                                                                                     # Drag times?
		pass
	else:
		end = time.time()
		formatted_time = "{:.5f}".format(end-start)
		print((x, y), ';', button, ';', formatted_time, ';', (start_location[0] - x, start_location[1] - y), ';', 0)
		start = time.time()


def on_scroll(x, y, dx, dy):
	if dy > 0:
		print((x, y), ';', "scroll up", ';', -1, ';', (-1, -1),';', 0)
	else:
		print((x, y), ';', "scroll down", ';', -1, ';', (-1, -1),';', 0)
		
def start_screen():
	running = True
	pygame.init()
	while running:
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		font = pygame.font.SysFont('Arial', 25)
		text = font.render('Click \'START\' to begin', True, (255, 255, 255), (0, 0, 0))
		text2 = font.render('START', True, (255, 255, 255), (0, 0, 0))
		textRect2 = text2.get_rect()
		textRect = text.get_rect()
		textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//4)
		textRect2.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//1.5)
		screen.fill((0, 0, 0))
		screen.blit(text, textRect)
		screen.blit(text2, textRect2)
		pygame.display.update()
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			running = False
			pygame.quit()
if __name__ == '__main__':
	count = 0
	start_screen()
	sys.stdout = open("Subject0.txt", 'w')
	print("(X, Y); Button Pressed; Time; Distance From Start Point; Subject ID")
	start_switch = 0
	start = time.time()
	now = time.time()
	future = now + 2
	listener = mouse.Listener(
		on_move=on_move,
		on_click=on_click,
		on_scroll=on_scroll)
	listener.start()
	while time.time() < future:
		continue
	listener.stop()
	sys.stdout.close()

