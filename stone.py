import pygame
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
dir = 0
dir2 = 0
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos = pygame.Vector2(400, screen.get_height() / 2)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    def move_up(m) :
        player_pos.y += m 

    def move_down(m):
        player_pos.y -= m 

    def move_left(m) :
        player_pos.x -= m 

    def move_right(m):
        player_pos.x += m 
    
    def border_x_check(dir):
        if(player_pos.x <= 40 ): 
            return 1
        elif(player_pos.x >= 1240):
            return 0
        else:
            return dir 
    
    def border_y_check(dir2):
        if(player_pos.y <= 40 ): 
            return 0
        elif(player_pos.y >= 680):
            return 1
        else:
            return dir2     

    def s_2_s(dir):
        if dir == 0 :
            move_left(10)
        else:
            move_right(10)
        return border_x_check(dir)
    
    def u_2_d(dir2):
        print(player_pos.y)
        if dir2 == 0 :
            move_up(10)
        else:
            move_down(10)
        return border_y_check(dir2)

    dir = s_2_s(dir)
    dir2 = u_2_d(dir2)    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()