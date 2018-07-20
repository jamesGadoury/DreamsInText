#AUTHOR : James Gadoury
#CONTACT: gadouryjames@gmail.com
#GUI application developed using Tkinter and Python3
#Dreams in Text : Text game with a fantastical setting
#relies on playgame.py, game.py, interactables.py, and items.py

from interactables import *
from items import *
import time

#since all objects rely on eachother, the data of all objects must be sent to most of them
#object dictionary maps keys to these objects to provide accessibility

p = player()
r = robot()
i = inventory()
w = window()
d = door()
l = lamp()
g = gun()
object_dictionary = {'p': p, 'r': r, 'i': i, 'w': w, 'd': d, 'l': l, 'g':g}

#game over instance is created to change how playTurn() function is experienced by user if self.gameOver is True
class GameOverStatus(object):
    def __init__(self):
        self.gameOver = False
    def GameOver(self, victory):
        if victory:
            print("\nCongratulations! You have won the game... for now.")

        print("\nGame OVER! (TYPE RESET to reset game at beginning)")
        self.gameOver = True
    def printGameOver(self):
        print("Game OVER! (TYPE RESET to reset game at beginning)")
    def getGameOver(self):
        return self.gameOver

gameoverstatus = GameOverStatus()

#monster instance is created to introduce the monster if 15 turns have been played without gameoverstatus.getGameOver() returning True
class monsterAttack(object):

    count = 0

    def __init__(self, object_dictionary, gameoverstatus):
        self.object_dictionary = object_dictionary
        self.gameoverstatus = gameoverstatus
        self.monsterAttacked = False

    def monsterAttackCount(self):
        self.count += 1
        if self.count == 7:
            print("\nYou hear a roar in the distance...")
            print("It probably would be a good idea to get out of here soon...")

        if self.count == 12:
            print("\nYou hear a roar again... but much, much louder...")
            print("It sounds closer...")

        if self.count == 15:
            print("\n*ROOOAARR*")
            print("It sounds close...")

        if self.count == 19:
            print("\n*ROOOOOOOOOAAAAAAAAARRR*")
            print("You can tell that whatever is roaring is right outside the door.")

        if self.count == 20:
            self.monsterAttacks()
            self.monsterAttacked = True


    def monsterAttacks(self):
        print("\nYou suddenly hear a terrifying roar that echoes through the entire room!")

        if self.object_dictionary['d'].getBrokenBarricade():
            print("A terrifying monster emerges through the door.")
        else:
            print("A terrifying monster breaks through the door sending chunks of wood throughout the room!")
            self.object_dictionary['d'].breaks()

        if not self.object_dictionary['r'].isDead():
            print("'Well... we probably wouldn't of survived much longer anyway' the robot says without any emotion.")

        print("The sight of it sends terror down your spine and you pass out....")
        print("\nIt would seem your journey has ended it its beginning...")
        gameoverstatus.GameOver(victory = False)

    def getMonsterAttacked(self):
        return self.monsterAttacked

monster = monsterAttack(object_dictionary, gameoverstatus)

# help function is called when HELP (not case-sensitive) is typed into command line (ENTRY widget -  Tkinter - playgame.py)
# provides examples of acceptable user inputs to user
def help():
    print("Try typing simple commands mixed with objects/entities that you see.")

    print("Examples (Not case sensitive): ")
    print("OPEN DOOR")
    print("EXIT WINDOW")
    print("SPEAK ROBOT")
    print("TALK TO ROBOT")
    print("BREAK WINDOW")
    print("TAKE LAMP")

    print("Other possible commands: ")
    print("INVENTORY")
    print("LOOK")
    print()

    print("You can also use objects: ")
    print("BREAK WINDOW WITH LAMP")
    print("SHOOT DOOR WITH PISTOL")

# look function is called when LOOK (not case-sensitive) is typed into command line (ENTRY widget - Tkinter - playgame.py)
# updates user on descriptions of different object instances in the room - these descriptions are updated based on instance variables of each object
def look():
    global object_dictionary
    if not object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead():
        print("You are facing a human like robot sitting with its legs crossed and eyes closed.")
        print("Looking at its metallic face fills you with melancholy.")
    elif object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead():
        print("You are facing the robot who now stares at you intently with concern while smiling like a crazed lunatic...")
    else:
        print("You are facing the metallic remains of the robot's face scattered over its non-responsive body...")
    if 'pistol' not in object_dictionary['i'].getInventory():
        print("There is a pistol by its side.")



    if not object_dictionary['w'].isBroken():
        print("Light is beeming into the room through a solitary window above the robot.")
        print("It must be early in the morning.")
    else:
        print("The robot is covered in shattered glass from the window.")


    if 'lamp' not in object_dictionary['i'].getInventory() and object_dictionary['l'].getIsUsable():
        print("You look to the left and see a medium-sized lamp on top of a flat desk.")
    else:
        print("You see an empty flat desk on the left.")



    if not object_dictionary['d'].getBrokenBarricade():
        print("Behind you is a large wooden door.")
        print("There are six 2x4 blocks of wood screwed and fastened across it.")
        print("Something doesn't want you to leave here.")
    else:
        print("Behind you is the smashed remains of the door.")

# begins game - called when app (Tkinter -- playgame.py) is created and after user_input == 'reset' during gameover (gameoverstatus.getGameOver() == True)
def beginGame():


    print("You wake up in a cold sweat... lying on a hardwood floor.")
    print("You are in an odd room and have no recollection of who you are or how you got there.")
    print("You sit up and get a handle on your environment.")

    look()

# called every time text is entered into ENTRY widget (Tkinter -- playgame.py)
# if gameoverstatus.getGameOver() == False and 15 turns have passed - monster attacks - returns True to allow playTurn to keep being called
# if gameoverstatus.getGameOver() == True - user is prompted to type RESET (not case-sensitive), when reset is typed - new instance of each object is created
#    - returns False to prompt app to delete all text in textbox and call beginGame()
#if none of these conditions are satisfied - then functions within relevant instances are called to interact with user or user is told the input was not acceptable
#    - returns True to allow playTurn to keep being called until reset is called
def playTurn(UI):
    global gameoverstatus
    global monster
    global object_dictionary
    if gameoverstatus.getGameOver():
        if UI.lower() == 'reset':
            p = player()
            r = robot()
            i = inventory()
            w = window()
            d = door()
            l = lamp()
            g = gun()
            object_dictionary = {'p': p, 'r': r, 'i': i, 'w': w, 'd': d, 'l': l, 'g':g}

            gameoverstatus = GameOverStatus()
            monster = monsterAttack(object_dictionary, gameoverstatus)

            return False
        else:
            gameoverstatus.printGameOver()
            return True

    print()
    if 'with' in UI.lower():
        if 'lamp' in UI.lower():
            object_dictionary['l'].useLamp(UI, object_dictionary)
        elif 'pistol' in UI.lower() or 'gun' in UI.lower():
            object_dictionary['g'].usePistol(UI, object_dictionary)
        elif 'robot' in UI.lower():
            object_dictionary['r'].engageRobot(UI, object_dictionary)
        else:
            error()
    elif "robot" in UI.lower():
        if "command" in UI.lower():
            object_dictionary['r'].robotCommand(UI, object_dictionary)
        else:
            object_dictionary['r'].engageRobot(UI, object_dictionary)
    elif "?" in UI:
        if object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead():
            object_dictionary['r'].robotQuestion(UI)
        else:
            print("Who are you talking to?")
    elif "window" in UI.lower():
            object_dictionary['w'].engageWindow(UI, object_dictionary)
    elif "door" in UI.lower():
        object_dictionary['d'].engageDoor(UI, object_dictionary)
    elif "lamp" in UI.lower():
        object_dictionary['l'].engageLamp(UI, object_dictionary)
    elif "pistol" in UI.lower() or 'gun' in UI.lower():
        object_dictionary['g'].engagePistol(UI, object_dictionary)

    elif "help" == UI.lower():
        help()
    elif "inventory" == UI.lower():
        object_dictionary['i'].showInventory()
    elif "look" == UI.lower():
        look()
    else:
        error()


    # if player is dead - then game over is triggered
    if object_dictionary['p'].isDead():
        gameoverstatus.GameOver(victory = False)



    # if window has been exit through - game over is triggered
    if object_dictionary['w'].getHasBeenExitThrough():
        print("You land in a field by the house...")

        if object_dictionary['r'].getRobotFollows():
            print("The robot lands behind you..")

            print("'Well... I guess we weren't going to be safe in there for much longer any way.")
        gameoverstatus.GameOver(victory = True)

    # if door has been exited through - then game over is triggered
    if object_dictionary['d'].getHasBeenExitThrough():
        print("You walk through the door and instantly fill dread pull into your stomach...")

        print("As you look up, you see directly into the eyes of a giant monster.")
        print("Rows of teeth fill a giant snarl breathing the smell of blood and dispair directly into your nose.")

        if object_dictionary['r'].getRobotFollows():
            print("'Well... I guess it was only a matter of time until it caught up with us.' Mr. Robot sighs.")
        print("I will spare you the details of the horrifying manner in which this beast eats.")
        gameoverstatus.GameOver(victory = False)

    monster.monsterAttackCount()
    if monster.getMonsterAttacked():
        return True

    return True
