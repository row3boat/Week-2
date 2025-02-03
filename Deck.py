import time
import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600, 1000))
running = True
my_font = pygame.font.SysFont('Comic Sans MS', 30)
out_of_cards = my_font.render('Out of cards', False, (255, 255, 255))


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
    cards.remove(cards[index])
    return card

def display_card(card):
    image_name = f"{card[0]}_of_{card[1]}"
    if (card[1] in ["J","Q","K","A"]):
        image_name += "2"
    card_png = pygame.image.load(f"Week-2\PNG-CARDS-1.3\{image_name}.png").convert()
    return card_png

cards = build_deck()
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (len(cards)) > 0:
                card = deal(cards)
                screen.blit(display_card(card),(100,100))
            else:
                screen.fill("black") 
                screen.blit(out_of_cards,(100,100))
            
        if event.type == pygame.KEYDOWN:
            cards = build_deck()
            
    pygame.display.flip()
    clock.tick(60)