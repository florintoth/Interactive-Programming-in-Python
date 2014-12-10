# template for "Stopwatch: The Game"

import simplegui

# define global variables

interval = 100
count = 0
stop = True
total_stops = 0
hit_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    if count == 5999 :
        timer.stop()
    tenth_seconds = t % 10
    seconds = int(t / 10) % 10
    minutes = int(t / 600) % 600
    tens_minutes = int(t / 100) % 6
    string = str(minutes) + ":" + str(tens_minutes) + str(seconds) + "." + str(tenth_seconds)
    return string

# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global count, stop
    stop = False
    timer.start()

def stop():
    global total_stops, hit_stops, stop
    if stop == False :
        if count % 10 == 0 and count != 0 :
            hit_stops += 1
            total_stops += 1
        elif count != 0 :
            total_stops += 1
            stop = True
            timer.stop()
       
def reset():
    global count, hit_stops, total_stops
    count = 0
    stop = True
    total_stops = 0
    hit_stops = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval

def tick():
    global count
    count += 1

# define draw handler

def draw(canvas):
    text = format(count)
    canvas.draw_text(text, (100, 120), 50, "white")
    canvas.draw_text(str(hit_stops) + '/' + str(total_stops), (240,30), 30, "white")

# create a frame
frame = simplegui.create_frame("Stopwatch game", 300, 200)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()
reset()

# Please remember to review the grading rubric