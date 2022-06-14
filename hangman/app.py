import pygame, time, random
from pygame.locals import *
from words import Words


# COLORS
WHITE = '#ffffff'
BLACK = '#000000'

# DIMENSIONS
WIDTH = 700
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

class Man():

    def __init__(self, screen):

        self.parent_screen = screen

    def check_mistakes(self,mistakes):
                
        if mistakes == 1:
            self.draw_head()
        if mistakes == 2:
            self.draw_body()
        if mistakes == 3:
            self.draw_hands()

        if mistakes == 4:
            self.draw_legs()
            return True
        

    def draw_head(self):

        pygame.draw.circle(self.parent_screen, WHITE, (WIDTH/4, HEIGHT/4+30), 30)
        pygame.draw.circle(self.parent_screen, BLACK, (WIDTH/4, HEIGHT/4+30), 28)
        pygame.display.flip()

    def draw_body(self):

        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4, HEIGHT/4+60), (WIDTH/4, HEIGHT/2-10), 2)
        pygame.display.flip()

    def draw_hands(self):

        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4, HEIGHT/4+60), (WIDTH/4-30, HEIGHT/4+100), 2)
        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4, HEIGHT/4+60), (WIDTH/4+30, HEIGHT/4+100), 2)
        pygame.display.flip()

    def draw_legs(self):

        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4, HEIGHT/2-10), (WIDTH/4-30, HEIGHT/2+30), 2)
        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4, HEIGHT/2-10), (WIDTH/4+30, HEIGHT/2+30), 2)
        pygame.display.flip()


class Hanger():

    def __init__(self, screen):

        self.parent_screen = screen

    def draw(self):

        self.draw_stand()
        self.draw_pole()
        self.draw_beam()
        self.draw_rope()
            
    def draw_pole(self):

        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4-60, HEIGHT/6), (WIDTH/4-60, HEIGHT/2+80), 3)
        pygame.display.flip()
        
    def draw_stand(self):

        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4-80, HEIGHT/2+80), (WIDTH/4-40, HEIGHT/2+80), 3)
        pygame.display.flip()

    def draw_beam(self):

        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4-60, HEIGHT/6), (WIDTH/4, HEIGHT/6), 3)
        pygame.display.flip()

    def draw_rope(self):

        pygame.draw.line(self.parent_screen, WHITE, (WIDTH/4, HEIGHT/6), (WIDTH/4, HEIGHT/4), 1)
        pygame.display.flip()

class Text():
    
    def __init__(self, screen, word):

        self.parent_screen = screen
        self.word = word
        self.letters = []
        self.display_text = ''
        self.wrong_letters = 'Wrong Letters:'

    def get_text(self):

        # capitalises the word
        self.word = self.word.upper()

        # chooses a random letter from the word
        num = random.randint(0, len(self.word)-1)
        letter = self.word[num]

        # converts the word into blanks and fills in all instances of the above letter
        for i in range(len(self.word)):

            if self.word[i] == letter:
                self.display_text += letter

            elif self.word[i] == ' ':
                self.display_text += ' '

            else:
                self.display_text += '_'

        print(self.display_text)

    def display(self):

        self.get_text()

        font = pygame.font.SysFont('arial', 40) 

        text = font.render(self.display_text, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH* 3/4, HEIGHT/4))
        self.parent_screen.blit(text, text_rect)
        pygame.display.flip()

    def update_display(self):
        
        pygame.draw.rect(self.parent_screen, BLACK, (WIDTH/2 , 0, WIDTH/2, HEIGHT/2))

        font = pygame.font.SysFont('arial', 40) 

        text = font.render(self.display_text, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH* 3/4, HEIGHT/4))
        self.parent_screen.blit(text, text_rect)

        print('display updated')

        pygame.display.flip()

    def check_letter_match(self, input):

        # fills the blank with the correct input letter if match + discards the input if no match

        text = ''
        filled = False
        match = False
        self.mistake = False
        
        for i in range(0, len(self.display_text)):
        
            if self.display_text[i] == '_':

                if input == self.word[i]:
                    print('match')
                    text += input
                    match = True
                
                else:
                    text += '_'

            elif self.display_text[i] == ' ':
                text += ' '

            elif self.display_text[i] == input:   
                text += self.word[i]
                filled = True

            elif self.display_text[i] == self.word[i]:
                text += self.word[i]
        
        self.display_text = text

        if filled == True:
            print('alr filled')
            return

        if match == True:
            self.update_display()
            return
        
        else:
            self.display_wrong_letter(input)
            self.mistake = True

    def display_wrong_letter(self, letter):
        
        pygame.draw.rect(self.parent_screen, BLACK, (WIDTH/2 , HEIGHT/2, WIDTH/2, HEIGHT/2))
        
        self.wrong_letters += letter + ' '

        font = pygame.font.SysFont('arial', 30)

        text = font.render(self.wrong_letters, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH* 3/4, HEIGHT * 3/4))
        self.parent_screen.blit(text, text_rect)

        pygame.display.flip()


class Game():

    def __init__(self):

        pygame.init()       
        self.screen = pygame.display.set_mode(SIZE)

        self.mistakes = 0

        self.man = Man(self.screen)
        self.hanger = Hanger(self.screen)
        self.words = Words()
        
        self.selected_word = self.words.get_word()

        self.text = Text(self.screen, self.selected_word)
        
    def cut(self):

        pygame.draw.line(self.screen, WHITE, (WIDTH/4-10, HEIGHT/6+20), (WIDTH/4+10, HEIGHT/6+30), 1)
        pygame.display.flip()

    def check_if_complete(self):

        return self.text.display_text == self.text.word
    
    def display_gameover(self):

        font = pygame.font.SysFont('arial', 50)

        text = font.render("GAME OVER!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    
    def display_category(self):

        font = pygame.font.SysFont('arial', 30)

        text = font.render('Category: ' + self.words.category, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH* 3/4, 20))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

        
    def display_complete(self):

        font = pygame.font.SysFont('arial', 50)

        text = font.render("WORD COMPLETE!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()


    def run(self):

        self.hanger.draw()

        self.text.display()


        self.running = True
        last_chance = False

        while self.running:
            
            self.display_category()

            for event in pygame.event.get():

                if event.type == KEYDOWN:
                    
                    # quit on ESC
                    if event.key == K_ESCAPE:
                        self.running = False
                        time.sleep(2)

                # input letters
                if event.type == KEYUP:

                    try:
                        user_input = chr(event.key).upper()
                        value = ord(user_input)

                        if value >= ord('A') and value<= ord('Z'):
                            self.text.check_letter_match(user_input)
                        
                            if self.text.mistake == False:

                                if self.check_if_complete():
                                    self.display_complete()
                                    time.sleep(2)
                                    self.running = False

                    
                            else:
                                self.mistakes += 1
                                if last_chance == True:
                                    self.cut()
                                    self.display_gameover()
                                    time.sleep(2)
                                    self.running = False

                                else: 
                                    last_chance = self.man.check_mistakes(self.mistakes)
                                    print(self.mistakes)

                    except ValueError as val:
                        print(val)

                elif event.type == pygame.QUIT:                 
                    pygame.quit()
            

if __name__ == '__main__':

    game = Game()
    game.run()