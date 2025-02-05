import time
import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 1000))
screen_aspect_ratio = screen.get_height() / screen.get_width()
running = True
my_font = pygame.font.SysFont('Comic Sans MS', 30)
out_of_cards = my_font.render('Out of cards', False, (255, 255, 255))
hand_text = my_font.render('Hand', False, (255, 255, 255))
hit_text = my_font.render('Hit',False, (255,255,255))
hit_pos = (screen.get_width()-hit_text.get_width()*4-60,screen.get_height()-hit_text.get_height()*2-30)
hit_button = pygame.Rect(hit_pos, (hit_text.get_width()*4, hit_text.get_height()*2))
hand = []
discard = []

def scaled_size(image:pygame.Surface,width)->pygame.Surface:
    aspect_ratio = image.get_width() / image.get_height()
    scaled_height = width/aspect_ratio
    return pygame.transform.scale(image,(width,scaled_height))

def build_deck()->[]:
    suit = ["clubs","spades","hearts","diamonds"]
    rank = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
    cards = []
    
    for s in suit:
        for r in rank:
            card = [r,s]
            cards.append(card)
            
            
    return cards

def deal(cards)->[]:
    index = random.randint(0,len(cards)-1)
    card = cards[index]
    discard.insert(cards[index])
    cards.remove(cards[index])
    return card

def display_card(card):
    image_name = f"{card[0]}_of_{card[1]}"
    if (card[1] in ["J","Q","K","A"]):
        image_name += "2"
    card_png = pygame.image.load(f"Week-2\PNG-CARDS-1.3\{image_name}.png").convert()
    return card_png

def renderHand():
    
    return

deck = build_deck()
while running:
    
    mouse = pygame.mouse.get_pos()
    #draw the hit button
    screen.blit(hit_text,hit_pos)
    pygame.draw.rect(screen, (255,255,255), hit_button, 1)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (len(deck)) > 0 and hit_pos[0] <= mouse[0] <= hit_pos[0] + hit_button.width and hit_pos[1] <= mouse[1] <= hit_pos[1] + hit_button.height:
                hand.insert(deal(deck))
                renderHand()
                
                card = deal(deck)
                card_surface = scaled_size(display_card(card),screen.get_width()/10)
                card_pos = screen.get_width()/2-card_surface.get_width(), screen.get_height() - card_surface.get_height()
                screen.blit(card_surface,card_pos)
                screen.blit(hand_text,(card_pos[0]+card_surface.get_width()*3/4-hand_text.get_width(),card_pos[1]-hand_text.get_height()))
            elif (len(deck) <= 0):
                screen.fill("black") 
                screen.blit(out_of_cards,card_pos)
            
        if event.type == pygame.KEYDOWN:
            deck = build_deck()
            
    pygame.display.flip()
    clock.tick(60)