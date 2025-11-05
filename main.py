#PyGame with PyPong

# Modules
from pygame import *
from random import choice
import sys




#Game Class
class PongGame:
    #Constant Game Variables
    WIDTH, HEIGHT = 800, 600
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PADDLE_WIDTH = 15
    PADDLE_HEIGHT = 100
    PADDLE_SPEED = 15
    BALL_RADIUS = 15
    BALL_SPEED_X = 10
    BALL_SPEED_Y = 10

    # Initialize PyGame w/ Game Variables
    def __init__(self):
        # Game Settings
        font.init()
        mixer.init() # for the audio

        self.screen = display.set_mode((self.WIDTH, self.HEIGHT)) 
        self.clock = time.Clock() # allows for fps, comes from pygame not time module
        display.set_caption("PyPong") # sets title of game

        mixer.music.load("background.mp3") # loads background music
        mixer.music.play(-1) # allows music to loop indefinitely

        #Game Variables
        # x and y positions for player 1 and 2
        self.player1 = [50, (self.HEIGHT - self.PADDLE_HEIGHT)/2]
        self.player2 = [self.WIDTH - 50 - self.PADDLE_WIDTH, (self.HEIGHT - self.PADDLE_HEIGHT)/2]
        self.ball_pos = [self.WIDTH//2, self.HEIGHT//2] # sets starting ball location
        self.ball_speed = [self.BALL_SPEED_X, self.BALL_SPEED_Y] #determines ball speed
        self.p1_score = 0
        self.p2_score = 0
        self.font = font.Font(None, 45)

    # Make the Paddles
    def paddle(self, pos): #pos refers to the player
        #make rectangle in pygame
        draw.rect(self.screen, self.WHITE, (pos[0], pos[1], self.PADDLE_WIDTH, self.PADDLE_HEIGHT)) # draws the paddle, can be google on pygame site

    # Make the Ball
    def ball(self, pos):
        draw.circle(self.screen, self.WHITE, pos, self.BALL_RADIUS)

    # Check if ball hits a paddle
    def hit_paddle(self, ball_pos, paddle_pos) -> bool:
        return (paddle_pos[0] < ball_pos[0] < paddle_pos[0] + self.PADDLE_WIDTH) and (paddle_pos[1] < ball_pos[1] < paddle_pos[1] + self.PADDLE_HEIGHT) #returns a boolean value of whether the ball hits the paddle or if it doesnt.
    


    # Move the Ball
    def update_ball(self):
        self.ball_pos[0] += self.ball_speed[0]
        self.ball_pos[1] += self.ball_speed[1]

        if self.ball_pos[1] - self.BALL_RADIUS <= 0 or self.ball_pos[1] + self.BALL_RADIUS >= self.HEIGHT - self.BALL_RADIUS:
            self.ball_speed[1] = -self.ball_speed[1]

        if self.hit_paddle(self.ball_pos, self.player1) or self.hit_paddle(self.ball_pos, self.player2): #reverses the ball speed on hit
            self.ball_speed[0] = -self.ball_speed[0]

        if self.ball_pos[0] <= 0: #adds a point to player 2's score if the ball moves past the paddle of player 1
            self.p2_score += 1
            self.reset()

        if self.ball_pos[0] >= self.WIDTH:
            self.p1_score += 1
            self.reset()

    # Reset the Game
    def reset(self):
        self.ball_pos = [self.WIDTH//2, self.HEIGHT//2]
        random_direction = choice([-1, 1]) #tells the ball to move in a random direction once the game starts again
        self.ball_speed = [self.BALL_SPEED_X * random_direction, self.BALL_SPEED_Y]


    # Run the Game
    def run_game(self):
        run = True
        while run:
            for e in event.get(): #allows program to be quit without having it crash and wait for a response.
                if e.type == QUIT: #checking to see if we need to quit the game
                    run = False # takes variable of run and switches value to false
                    sys.exit()

            keys = key.get_pressed() #acts as an event listener for when a key gets pressed
            if keys[K_w] and self.player1[1] > 0: #takes the key down event and says if the keys are pressed and p1's y position is greater than 0 which is the top of the window
                self.player1[1] -= self.PADDLE_SPEED #moves the paddle down at the rate of the paddle speed variable from above
            elif keys[K_s] and self.player1[1] < self.HEIGHT-self.PADDLE_HEIGHT:
                self.player1[1] += self.PADDLE_SPEED

            if keys[K_UP] and self.player2[1] > 0:
                self.player2[1] -= self.PADDLE_SPEED
            elif keys[K_DOWN] and self.player2[1] < self.HEIGHT-self.PADDLE_HEIGHT:
                self.player2[1] += self.PADDLE_SPEED

            
            self.update_ball()
            self.screen.fill(self.BLACK)
            self.paddle(self.player1)
            self.paddle(self.player2)
            self.ball(self.ball_pos)

            p1_text = self.font.render(str(self.p1_score), True, self.WHITE)
            p2_text = self.font.render(str(self.p2_score), True, self.WHITE)

            self.screen.blit(p1_text, (self.WIDTH/4, 20))
            self.screen.blit(p2_text, (self.WIDTH * 3 / 4, 20))

            #Winning condition
            if self.p1_score >=5 or self.p2_score >= 5:
                run = False

            display.update()
            self.clock.tick(40)

if __name__ == "__main__":
    game =  PongGame()
    game.run_game()