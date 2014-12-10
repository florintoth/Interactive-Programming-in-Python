# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [0.0, 0.0]
ball_vel = [0.0, 0.0]

paddle1_vel = 0
paddle2_vel = 0

paddle1_pos = 0
paddle2_pos = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
   
    ball_pos[0] = WIDTH / 2
    ball_pos[1] = HEIGHT / 2
    
    hor_vel = random.randrange(2, 4)
    vert_vel = random.randrange(1, 3)

    
    if (direction == LEFT):
        ball_vel[0] = -hor_vel
        ball_vel[1] = -vert_vel
    else:
        ball_vel[0] = hor_vel
        ball_vel[1] = -vert_vel


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    paddle1_vel = 0
    paddle2_vel = 0

    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    
    score1 = 0
    score2 = 0
    
    # Sprall at random
    if random.randint(0,10) % 2 == 0:
        direction = RIGHT
    else:
        direction = LEFT
        
    spawn_ball(direction)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas, increase
    # velocity by 10% for each strike to the paddle
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if (ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0] + (float(-ball_vel[0]) / 10)
        else:
            score2 += 1
            spawn_ball(RIGHT)

            
    # collide and reflect off of right hand side of canvas, increase
    # velocity by 10% for each strike to the paddle
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS - 1:
        if (ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0] - (float(ball_vel[0]) / 10) 
        else:
            score1 += 1
            spawn_ball(LEFT)


    # collide and reflect off of top and bottom side of canvas
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS - 1:
        ball_vel[1] = -ball_vel[1]

            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_new_pos = paddle1_pos + paddle1_vel
    paddle2_new_pos = paddle2_pos + paddle2_vel

    if (paddle1_new_pos >= 0) and (paddle1_new_pos <= HEIGHT - PAD_HEIGHT):
        paddle1_pos = paddle1_new_pos

    if (paddle2_new_pos >= 0) and (paddle2_new_pos <= HEIGHT - PAD_HEIGHT):
        paddle2_pos = paddle2_new_pos
    
    # draw paddles
    canvas.draw_line((HALF_PAD_WIDTH, paddle1_pos), (HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT), PAD_WIDTH, 'Red')
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos), (WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT), PAD_WIDTH, 'orange')
    
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH / 4, 50], 40, "Red")
    canvas.draw_text(str(score2), [WIDTH * 2 / 3, 50], 40, "Orange")

        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("Restart Game", new_game, 200)


# start frame
new_game()
frame.start()
