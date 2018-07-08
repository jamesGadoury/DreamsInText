from interactables import *
from items import *
import time



def help():
    print("Try typing simple commands mixed with objects/entities that you see.")
    input("...")
    print("Examples (Not case sensitive): ")
    print("OPEN DOOR")
    print("EXIT WINDOW")
    print("SPEAK ROBOT")
    print("TALK TO ROBOT")
    print("BREAK WINDOW")
    print("TAKE LAMP")
    input("...")
    print("Other possible commands: ")
    print("INVENTORY")
    print("LOOK")
    print()
    input("...")
    print("You can also use objects: ")
    print("BREAK WINDOW WITH LAMP")
    print("SHOOT DOOR WITH PISTOL")


def look():
    print("You are facing a human like robot sitting with its legs crossed and eyes closed.")
    print("Looking at its metallic face fills you with melancholy.")
    print("There is a pistol by its side.")
    input("...")
    print("Light is beeming into the room through a solitary window above the robot.")
    print("It must be early in the morning.")
    input("...")
    print("You look to the left and see a medium-sized lamp on top of a flat desk.")
    input("...")
    print("To your right is a smashed computer with cables draped over and around it, wrapping it like a cobra around its prey.")
    input("...")
    print("Behind you is a large wooden door.")
    print("There are six 2x4 blocks of wood screwed and fastened across it.")
    print("Something doesn't want you to leave here.")
    input("...")

def beginGame():
    print("You wake up in a cold sweat... lying on a hardwood floor.")
    print("You are in an odd room and have no recollection of who you are or how you got there.")
    print("You sit up and get a handle on your environment.")
    input("...")
    look()
    playStartingRoom()

def playStartingRoom():
    p = player()
    r = robot()
    i = inventory()
    w = window()
    d = door()
    l = lamp()
    g = gun()

    object_dictionary = {'p': p, 'r': r, 'i': i, 'w': w, 'd': d, 'l': l, 'g':g}
    while not p.isDead() and not w.getHasBeenExitThrough() and not d.getHasBeenExitThrough():
        UI = input("\n<Type Command>")
        if 'with' in UI.lower():
            if 'lamp' in UI.lower():
                l.useLamp(UI, object_dictionary)
            elif 'pistol' in UI.lower() or 'gun' in UI.lower():
                g.usePistol(UI, object_dictionary)
            elif 'robot' in UI.lower():
                r.engageRobot(UI, object_dictionary)
            else:
                error()
        elif "robot" in UI.lower():
            if "command" in UI.lower():
                r.robotCommand(UI, object_dictionary)
            else:
                r.engageRobot(UI, object_dictionary)
        elif "window" in UI.lower():
            w.engageWindow(UI, object_dictionary)
        elif "door" in UI.lower():
            d.engageDoor(UI, object_dictionary)
        elif "lamp" in UI.lower():
            l.engageLamp(UI, object_dictionary)
        elif "pistol" in UI.lower() or 'gun' in UI.lower():
            g.engagePistol(UI, object_dictionary)
        elif "help" == UI.lower():
            help()
        elif "inventory" == UI.lower():
            i.showInventory()
        elif "look" == UI.lower():
            look()
        else:
            error()

    if p.isDead():
        GameOver(victory = False)

    if w.getHasBeenExitThrough():
        print("You land in a field by the house...")
        input("...")
        if r.getRobotFollows():
            print("The robot lands behind you..")
            input("...")
            print("'Well... I guess we weren't going to be safe in there for much longer any way.")
        GameOver(victory = True)

    if d.getHasBeenExitThrough():
        print("You walk through the door and instantly fill dread pull into your stomach...")
        input("...")
        print("As you look up, you see directly into the eyes of a giant monster. Rows of teeth fill a giant snarl breathing the smell of blood and dispair directly into your nose.")
        input("...")
        if r.getRobotFollows():
            print("'Well... I guess it was only a matter of time until it caught up with us.' Mr. Robot sighs.")
        print("I will spare you the details of the horrifying manner in which this beast eats.")
        GameOver(victory = False)



def GameOver(victory):
    if victory:
        print("Congratulations! You have won the game... for now.")

    retry = input("Game OVER! Play Again? (TYPE Yes or No)")
    if retry.lower() == 'yes':
        print()
        beginGame()
