import pyautogui
import time

def create_board():
    pyautogui.hotkey("win")
    time.sleep(1)
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write("https://excalidraw.com/")
    pyautogui.press("enter")

    time.sleep(1)
    pyautogui.hotkey("ctrl", "a", "backspace")
    time.sleep(1)

    reset_board()

def switch_tabs():
    pyautogui.hotkey("alt", "tab")

def instructions():
    print("1|2|3\n4|5|6\n7|8|9")

def play():
    gamestate = ["[", "]", "(", ")", "-", "=", "_", "+", ";"]

    comp = False
    players = input("how many players: ")
    if players == 1:
        comp = True

    while not gameover(gamestate):
        move = input("where do you want to play (give as location, shape ex: \"4, o\" for an o at middle left): ")
        gamestate[int(move[0]) - 1] = move[-1]
        draw(int(move[0]) - 1, move[-1]) 

        if comp:
            computer(gamestate)

    print("someone won")
    replay = input("replay y or n: ")
    if replay == "y":
        switch_tabs()
        pyautogui.moveTo(650, 450)
        pyautogui.dragTo(250, 450, 1, button = "middle")
        reset_board()
        play()

def gameover(gamestate):
    over = False

    for x in range(3):
        if gamestate[0 + 3 * x] == gamestate[1 + 3 * x] == gamestate[2 + 3 * x]:
            over = True
        if gamestate[0 + x] == gamestate[3 + x] == gamestate[6 + x]:
            over = True

    if gamestate[0] == gamestate[4] == gamestate[8]:
        over = True
    if gamestate[2] == gamestate[4] == gamestate[6]:
        over = True
    
    return over

def computer():
    pass

def draw(box, char):
    switch_tabs()
    boxcoordx = box % 3
    boxcoordy = int(box / 3)

    pyautogui.moveTo(520 + boxcoordx * 100, 320 + boxcoordy * 100)
    time.sleep(1)
    if pyautogui.pixel(520 + boxcoordx * 100, 320 + boxcoordy * 100)[0] != 255:
        print("spot taken", pyautogui.pixel(520 + boxcoordx * 100, 320 + boxcoordy * 100))
        switch_tabs()
        return

    if char.lower() == "x":
        pyautogui.dragTo(580 + boxcoordx * 100, 380 + boxcoordy * 100, .25, button = "left")
        pyautogui.moveTo(580 + boxcoordx * 100, 320 + boxcoordy * 100)
        pyautogui.dragTo(520 + boxcoordx * 100, 380 + boxcoordy * 100, .25, button = "left")
        switch_tabs()
    elif char.lower() == "o":
        pyautogui.dragTo(580 + boxcoordx * 100, 320 + boxcoordy * 100, .25, button = "left")
        time.sleep(.01)
        pyautogui.dragTo(580 + boxcoordx * 100, 380 + boxcoordy * 100, .25, button = "left")
        time.sleep(.01)
        pyautogui.dragTo(520 + boxcoordx * 100, 380 + boxcoordy * 100, .25, button = "left")
        time.sleep(.01)
        pyautogui.dragTo(520 + boxcoordx * 100, 320 + boxcoordy * 100, .25, button = "left")
        switch_tabs()
    else:
        switch_tabs()
        print("char must be x or o")
    
    pyautogui.click(640, 1045, 1, button = "left")

def reset_board():
    pyautogui.press("7")
    time.sleep(1)

    pyautogui.moveTo(500, 400)
    pyautogui.dragTo(800, 400, .5, button = "left")
    pyautogui.moveTo(500, 500)
    pyautogui.dragTo(800, 500, .5, button = "left")

    pyautogui.moveTo(600, 300)
    pyautogui.dragTo(600, 600, .5, button = "left")
    pyautogui.moveTo(700, 300)
    pyautogui.dragTo(700, 600, .5, button = "left")

    switch_tabs()
    pyautogui.click(640, 1045, 1, button = "left")

create_board()
instructions()
play()
