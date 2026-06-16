from graphics import *

def draw_line(win, point_one, point_two, colour):
    line = Line(point_one, point_two)
    line.setFill(colour)
    line.draw(win)

def draw_text(win, point, text, size, colour):
    text = Text(point, text)
    text.setSize(size)
    text.setFill(colour)
    text.draw(win)

def draw_square(win, x, y, colour, size_of_square):
    square = Rectangle(Point(x, y), Point(x + size_of_square, y + size_of_square))
    square.setFill(colour)
    square.draw(win)

def patchwork_final(win, top_left_x, top_left_y, colour):

    for i in range(20, 81, 20):
        draw_line(win, Point(i + top_left_x, top_left_y), Point(i + top_left_x, 100 + top_left_y), colour)
        draw_line(win, Point(top_left_x, i + top_left_y), Point(100 + top_left_x, i + top_left_y), colour)
        
    for i in range(10, 91, 20):
        for j in range(10, 91, 20):
            draw_text(win, Point(i + top_left_x, j + top_left_y), "hi!", 8, colour)

def patchwork_penultimate(win, top_left_x, top_left_y, colour):

    for x in range(0, 100, 20):
        for y in range(0, 100, 20):
            arrow = Polygon(Point((top_left_x) + x, (top_left_y) + y), Point((top_left_x + 10) + x, (top_left_y + 10) + y), Point((top_left_x + 20) + x, (top_left_y) + y), Point((top_left_x + 20) + x, (top_left_y + 10) + y), Point((top_left_x + 10) + x, (top_left_y + 20) + y), Point((top_left_x) + x, (top_left_y + 10) + y))
            arrow.setOutline(colour)

            if (x == 20 or x == 60) and (y == 20 or y == 60):
                arrow.setFill("White")
            else:
                arrow.setFill(colour)

            arrow.draw(win)

def window_size_decider(valid_sizes):
    user_window_choice = input("The following window sizes are available: \n1. 500 x 500 \n2. 700 x 700 \n3. 900 x 900 \nPlease pick the size of your window by clicking 5, 7 or 9: ")

    while True:
        if user_window_choice in valid_sizes:
            win_size = int(user_window_choice) * 100
            print(f"\nThe window size you have chosen is: {win_size} x {win_size}!")
            break
        else:
            print("\nInvalid input! Please try again \n")
            user_window_choice = input("The following window sizes are available: \n1. 500 x 500 \n2. 700 x 700 \n3. 900 x 900 \nPlease pick the size of your window by entering 5, 7 or 9:: ")
    
    return win_size

def user_colour_choice(valid_colours, chosen_colours):
    while True:
        user_colour_choice = input("\nValid colours are: \nRed \nGreen \nBlue \nMagenta \nOrange \nYellow \nCyan. \nPlease enter your colour of choice: ").lower()

        if user_colour_choice in valid_colours and user_colour_choice not in chosen_colours:
            chosen_colours.append(user_colour_choice)
            break
        elif user_colour_choice in valid_colours and user_colour_choice in chosen_colours:
            print("\nYou have already picked this colour! \n")
        else:
            print("\nInvalid Colour.")

def draw_patch_grid(win, win_size, chosen_colours):
    for x in range(0, win_size, 100):
        for y in range(0, win_size, 100):

            if x % 200 == 0 and x <= y:
                colour = chosen_colours[0]
            elif x > y:
                colour = chosen_colours[1]
            else:
                colour = chosen_colours[2]

            if 100 <= x < win_size-100 and 100 <= y < win_size-100 and colour != chosen_colours[1]:
                patchwork_penultimate(win, x, y, colour)
            elif (100 <= x < win_size and y == 0) or (x == win_size - 100 and  y < win_size - 100):
                patchwork_final(win, x, y, colour)
            else:
                draw_square(win, x, y, colour, 100)
            
            patchwork_border = Rectangle(Point(x, y), Point(x + 100, y + 100))
            
            click = win.getMouse()

            

def selection_mode(win, win_size):
    while True:
        draw_square(win, 0, 0, "black", 30)
        draw_text(win, Point(15, 15), "OK", 10, "white")

        draw_square(win, win_size - 30, 0, "black", 30)
        draw_text(win, Point(win_size - 15, 15), "Close", 9, "white")

        selected_click = win.getMouse()

        
        if win_size - 30 < selected_click.getX() <= win_size and 0 < selected_click.getY() <= 30:
            win.close()
            break
        elif 0 < selected_click.getX() <= 30 and 0 < selected_click.getY() <= 30:
            pass # enter edit mode here
        
        for x in range(0, win_size, 100):
            for y in range(0, win_size, 100):

                if selected_click.X() and selected_click.Y():
                    pass

def main():
    valid_sizes = ["5", "7", "9"]
    win_size = window_size_decider(valid_sizes)

    valid_colours = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    chosen_colours = []

    for i in range(3):
        user_colour_choice(valid_colours, chosen_colours)

    win = GraphWin("", win_size, win_size)
    win.setBackground("White")

    draw_patch_grid(win, win_size, chosen_colours)
    

    selection_mode(win, win_size)

    # win.getMouse()
    
main()