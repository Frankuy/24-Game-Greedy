import pygame
import random
import os

#INIT GAME
pygame.init() #inisialisasi modul pygame

#GAME LIBRARY
green = (0, 204, 0)
white = (255,255,255) #(R,G,B)
black = (0,0,0)
tosca = (0, 255, 153)
red = (255,0,0)
display_width = 800
display_height = 600
card_width = 100
card_height = 150
#graphic
font = pygame.font.SysFont("raleway", 25, True)
card = pygame.image.load("card.png")
bg = pygame.image.load("table.jpg")
bgStart = pygame.image.load("bgStart.jpg")
hati = []
for i in range(13):
	hati.append(pygame.image.load(os.path.join("Hati",str(i+1) + "H.png")))
keriting = []
for i in range(13):
	keriting.append(pygame.image.load(os.path.join("Keriting", str(i+1) + "K.png")))
sekop = []
for i in range(13):
	sekop.append(pygame.image.load(os.path.join("Sekop", str(i+1) + "S.png")))
wajik = []
for i in range(13):
	wajik.append(pygame.image.load(os.path.join("Wajik", str(i+1) + "W.png")))


#SETTING SURFACE
gameDisplay = pygame.display.set_mode((display_width,display_height)) #surface
pygame.display.set_caption('24 Game') #judul

#USEFUL FUNCTION
def message(msg, color):
	screen_text = font.render(msg, True, color)
	gameDisplay.blit(screen_text, [display_width/4, display_height/4])

def animateDrawCard(location, final_location):
		n = len(location)-1
		same = True
		while (n >= 0 and same):
			if location[n][0] < final_location[n][0]:
				location[n][0]+=10
			elif location[n][0] > final_location[n][0]:
				location[n][0]-=10
			if location[n][1] < final_location[n][1]:
				location[n][1]+=10
			elif location[n][1] > final_location[n][1]:
				location[n][1]-=10

			if (location[n]==final_location[n]):
				n-=1
			else : 
				same = False

def AreaValid(mouseLocation,i):
	return mouseLocation[0] >= i[0] and mouseLocation[0] <= i[0]+100 and mouseLocation[1] >= i[1] and mouseLocation[1] <= i[1] + 150

def PickValid(choosenCard, idx):
	i = 0
	while(i < len(choosenCard)):
		if choosenCard[i] == idx:
			return False
		else:
			i+=1
	return True

def credits():
	gameDisplay.fill(black)
	text1 = font.render("Ashiaaap Team", True, white)
	text2 = font.render("Mgs. Muhammad Riandi Ramadhan 13517080", True, white)
	text3 = font.render("Muhamamad Fikri Hizbullah 13517104", True, white)
	text4 = font.render("M.Algah Fattah Illahi 13517122", True, white)
	
	gameDisplay.blit(text1, (250, 200))
	gameDisplay.blit(text2, (150, 250))
	gameDisplay.blit(text3, (150, 300))
	gameDisplay.blit(text4, (150, 350))

	pygame.display.update()
	pygame.time.delay(5000)




#MAIN LOOP
def gameLoop():
	gameExit = False
	location = []
	choose = 0
	choosenCard = []
	openedCard = []

	for i in range(11):
		location.append([300+i*10,500])
	final_location = [[300,600],[50,300],[200,300],[350,300],[500,300],[650,300],
						[50,100],[200,100],[350,100],[500,100],[650,100]]

	while not gameExit:
		cardOpen = 0
		mouseLocation = (0,0)
		#EVENT GETTER
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseLocation = event.pos


		#DRAWING SECTION
		gameDisplay.blit(bg, (0,0)) #background
		text = font.render("PICK 4 CARDS", True, white)
		gameDisplay.blit(text, (300,50))
		# gameDisplay.blit(card, (300,500))
		idx = 0
		for i in location:
			if choose < 4:
				if AreaValid(mouseLocation, i): #kalau ada daerah yang kepencet
					if PickValid(choosenCard, idx): #memastika kartu yang dipilih kartu yang belum dibuka
						choose+=1
						choosenCard.append(idx)
			idx+=1
			gameDisplay.blit(card, (i[0],i[1]))

		#flip card
		if (len(choosenCard) >= 1 and len(choosenCard) <= 4):
			while (len(openedCard) < len(choosenCard)):
				cardNumber = random.randint(1, 13)
				cardSymbol = random.randint(1, 4)
				while ((cardNumber,cardSymbol) in openedCard):
					cardNumber = random.randint(1, 13)
					cardSymbol = random.randint(1, 4)

				openedCard.append((cardNumber,cardSymbol))


			while (cardOpen < len(choosenCard)):
				if openedCard[cardOpen][1] == 1:
					gameDisplay.blit(hati[openedCard[cardOpen][0]-1], (location[choosenCard[cardOpen]][0],location[choosenCard[cardOpen]][1]))
				elif openedCard[cardOpen][1] == 2:
					gameDisplay.blit(keriting[openedCard[cardOpen][0]-1], (location[choosenCard[cardOpen]][0],location[choosenCard[cardOpen]][1]))
				elif openedCard[cardOpen][1] == 3:
					gameDisplay.blit(wajik[openedCard[cardOpen][0]-1], (location[choosenCard[cardOpen]][0],location[choosenCard[cardOpen]][1]))
				elif openedCard[cardOpen][1] == 4:
					gameDisplay.blit(sekop[openedCard[cardOpen][0]-1], (location[choosenCard[cardOpen]][0],location[choosenCard[cardOpen]][1]))
				cardOpen += 1

		animateDrawCard(location,final_location) #MENGUBAH LOKASI GAMBAR KARTU
		
		#UPDATE FRAME
		pygame.display.update()

		if len(openedCard) == 4:
			#solver
			pygame.time.delay(1000)
			gameExit = True


	credits()
	pygame.quit()

def gameStart():
	Start = False
	Quit = False
	while not Start:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				Start = True
				Quit = False
			if event.type == pygame.QUIT:
				Start = True
				Quit = True

		gameDisplay.blit(bgStart, (0,0))
		pygame.display.update()

	if not Quit:
		gameLoop()
	else:
		pygame.quit()

gameStart()