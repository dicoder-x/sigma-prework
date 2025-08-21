import curses

brush = ["#", "*", "@", "+", "-", "|", "/", "\\", "o", "0", "."]


def save():
    pass


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    print("\033[?1003h\n")  # Enables capturing mouse movement
    dragging = False
    loop = True
    current_brush = brush[0]

    while loop:
        char = stdscr.getch()
        screen_size = stdscr.getmaxyx()
        stdscr.addstr(
            0, 0, "Brushes: # * @ + - | / \\ o 0 . [ERASER]       Press q to quit")
        stdscr.addstr(1, 0, "="*screen_size[1])
        stdscr.addstr(
            1, screen_size[1]-len(str(screen_size)), str(screen_size))
        if char == curses.KEY_MOUSE:
            try:
                mouse_event = curses.getmouse()  # Returns tuple (id, y, x, z, button_state)
                x = mouse_event[2]
                y = mouse_event[1]
                stdscr.addstr(1, 0, str(mouse_event))
                # Brush selection
                if mouse_event[2] == 0 and mouse_event[4] == 2:
                    if mouse_event[1] == 9:
                        current_brush = brush[0]
                    elif mouse_event[1] == 11:
                        current_brush = brush[1]
                    elif mouse_event[1] == 13:
                        current_brush = brush[2]
                    elif mouse_event[1] == 15:
                        current_brush = brush[3]
                    elif mouse_event[1] == 17:
                        current_brush = brush[4]
                    elif mouse_event[1] == 19:
                        current_brush = brush[5]
                    elif mouse_event[1] == 21:
                        current_brush = brush[6]
                    elif mouse_event[1] == 23:
                        current_brush = brush[7]
                    elif mouse_event[1] == 25:
                        current_brush = brush[8]
                    elif mouse_event[1] == 27:
                        current_brush = brush[9]
                    elif mouse_event[1] == 29:
                        current_brush = brush[10]
                    elif 39 > mouse_event[1] > 30:
                        current_brush = ' '
                ######
                if mouse_event[4] == 2:
                    dragging = True
                elif mouse_event[4] == 1:
                    dragging = False
                ######
                if dragging:
                    stdscr.addstr(x, y, current_brush)
                else:
                    # stdscr.addstr(x, y, "*")
                    pass
            except:
                pass
        elif char == ord("q"):  # Quit loop condition is press q
            loop = False
        stdscr.refresh()


curses.wrapper(main)
