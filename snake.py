import curses
import random

screen = curses.initscr()
curses.curs_set(0)
curses.start_color()
curses.use_default_colors()
sh, sw = screen.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
#set speed here, greater is slower
w.timeout(110)

headX = sh/2
headY= sw/2


snake = [[headX,headY],[headX-1,headY]]

food = [sh/4,sw/4]
w.addch(food[0],food[1],curses.ACS_DIAMOND)

key = curses.KEY_RIGHT

while True:
    #gets key
    next_key = w.getch()
    if next_key == -1:
        key = key
    else:
        key = next_key
    #only changes key if input is added
    new_head = [snake[0][0],snake[0][1]]
    #if snake is overlapping on itself or outside bounds, end game
    if new_head[0] in [0,sh-1] or new_head[1] in [0,sw-1] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    #create a new head where the snake is moving
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    snake.insert(0, new_head)
    #if snake is eating food, remove the tail but replace with block
    if (new_head == food):
        tail = snake.pop()
        snake.append([tail[0],tail[1]])
        food = [random.randint(0,sh), random.randint(0,sw)]
        w.addch(food[0],food[1],curses.ACS_DIAMOND)
    #just remove tail, but advance snake
    else:
        tail = snake.pop()
        w.addch(tail[0],tail[1], ' ')
    #print out whole snake array
    for i in snake:
        w.addch(i[0], i[1], curses.ACS_CKBOARD)
