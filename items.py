#AUTHOR : James Gadoury
#CONTACT: gadouryjames@gmail.com
#GUI application developed using Tkinter and Python3
#Dreams in Text : Text game with a fantastical setting
#relies on playgame.py, game.py, interactables.py, and items.py

from interactables import *
interactionList = ['take', 'punch', 'kick', 'break', 'drop', 'climb', 'open', 'attack', 'shoot', 'pick up']
i = 0
for i in range(len(interactionList)):
    interactionList.append(interactionList[i] + ' the')
import time
class inventory(object):
    def __init__(self):
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)
    def removeItem(self, item):
        self.inventory.remove(item)

    def getInventory(self):
        inventoryList = []
        for item in self.inventory:
            inventoryList.append(item)
        return inventoryList

    def showInventory(self):
        if len(self.getInventory()) > 0:
            print("You are currently holding: ")
            i = 1
            for item in self.getInventory():
                print('['+ str(i) +'] '+item)
                i += 1
        else:
            print("You don't have anything!")

class interactable(object):
    def __init__(self):
        pass

    def interactWithObject(self, UI):
        self.ui = UI.rsplit(' ', 1)[0]

    def getUI(self):
        return self.ui.lower()


class lamp(interactable):
    lampInteractionList = ['take', 'break', 'punch', 'kick', 'drop', 'pick up']
    for i in range(len(lampInteractionList)):
        lampInteractionList.append(lampInteractionList[i] + ' the')

    def __init__(self):
        interactable.__init__(self)
        self.isUsable = True

    def getIsUsable(self):
        return self.isUsable

    def breaks(self, object_dictionary):
        self.isUsable = False
        object_dictionary['i'].removeItem('lamp')


    def engageLamp(self, UI, object_dictionary):
        self.interactWithObject(UI)
        if self.getUI() in self.lampInteractionList:
            if self.getUI() =='take' or self.getUI() == 'take the' or self.getUI() == 'pick up' or self.getUI() == 'pick up the':
                if 'lamp' not in object_dictionary['i'].getInventory():
                    if self.getIsUsable() == True:
                        print("You pick up the lamp.")
                        object_dictionary['i'].addItem('lamp')
                    else:
                        print("The lamp is broken. It is useless now.")
                else:
                    print("You are currently holding the lamp!")
            elif self.getUI() == 'drop' or self.getUI() == 'drop the':
                if 'lamp' in object_dictionary['i'].getInventory():
                    print("You drop the lamp.")
                    print("It shatters on the ground.")
                    self.breaks()
                    object_dictionary['i'].removeItem('lamp')
                else:
                    print("You are not holding the lamp!")
            elif self.getUI() == 'break' or self.getUI() == 'break the':
                if 'lamp' in object_dictionary['i'].getInventory():
                    print("You break the lamp.")
                    self.breaks()
                    object_dictionary['i'].removeItem('lamp')
                else:
                    print("You are not holding the lamp!")
            else:
                error()

        else:
            error()

    def useLamp(self, UI, object_dictionary):

        self.interactWithObject(UI)

        if 'lamp' not in object_dictionary['i'].getInventory():
            print("You are not holding the lamp!")
        else:
            if self.getUI() == 'break window with' or self.getUI() == 'break the window with':
                object_dictionary['w'].engageWindow('break window with lamp x', object_dictionary)
            elif self.getUI() == 'break door with' or self.getUI() == 'break the door with':
                object_dictionary['d'].engageDoor('break door with lamp x', object_dictionary)
            elif self.getUI() == 'attack robot with' or self.getUI() == 'attack the robot with':
                object_dictionary['r'].engageRobot('attack robot with lamp x', object_dictionary)
            else:
                error()


class gun(interactable):

    def __init__(self):
        interactable.__init__(self)
        self.isUsable = True
        self.bulletCount = 3

    def getIsUsable(self):
        return self.isUsable

    def shootGun(self):
        self.bulletCount += -1
        if self.bulletCount == 0:
            self.isUsable = False
        return self.bulletCount

    def getBulletCount(self):
        return self.bulletCount

    def engagePistol(self, UI, object_dictionary):
        self.interactWithObject(UI)
        if self.getUI() in interactionList:
            if self.getUI() =='take' or self.getUI() == 'take the' or self.getUI() == 'pick up' or self.getUI() == 'pick up the':
                if object_dictionary['r'].isAwake == True:
                    print("You reach to take the pistol from the robot's side...")

                    if not object_dictionary['r'].getCanBeCommanded():
                        print("The robot covers the pistol with its large hand.")

                        print("'No...no. I can't let you take this. I may need it.', the robot patronizes.")
                    else:
                        self.takePistol(object_dictionary)
                elif 'gun' not in object_dictionary['i'].getInventory():
                    self.takePistol(object_dictionary)
                else:
                    print("You are currently holding the pistol!")
            elif self.getUI() == 'drop' or self.getUI() == 'drop the':
                if 'pistol' in object_dictionary['i'].getInventory():
                    print("You drop the pistol.")
                    object_dictionary['i'].removeItem('pistol')
                else:
                    print("You are not holding the pistol!")
            elif self.getUI() == 'break' or self.getUI() == 'break the':
                if 'pistol' in object_dictionary['i'].getInventory():
                    print("You can't break the pistol.")
                else:
                    print("You are not holding the pistol!")
            else:
                error()

        else:
            error()

    def takePistol(self, object_dictionary):
        if self.getIsUsable() == True:
            print("You pick up the pistol.")

            print("It has two bullets in the clip and one in the chamber.")
            object_dictionary['i'].addItem('pistol')
        else:
            print("The pistol is out of bullets. It is useless now.")

    def usePistol(self, UI, object_dictionary):

        self.interactWithObject(UI)

        if 'pistol' not in object_dictionary['i'].getInventory():
            print("You are not holding the pistol!")
        elif self.getIsUsable() == False:
            print("The pistol is out of bullets. It is useless now.")
        else:
            if self.getUI() == 'break window with' or self.getUI() == 'break the window with' or self.getUI() == 'shoot window with' or self.getUI() == 'shoot the window with':
                self.shootGun()
                object_dictionary['w'].engageWindow('shoot window with pistol x', object_dictionary)
            elif self.getUI() == 'break door with' or self.getUI() == 'break the door with' or self.getUI() == 'shoot door with' or self.getUI() == 'shoot the door with':
                self.shootGun()
                object_dictionary['d'].engageDoor('shoot door with pistol x', object_dictionary)
            elif self.getUI() == 'attack robot with' or self.getUI() == 'attack the robot with' or self.getUI() == 'shoot robot with' or self.getUI() == 'shoot the robot with':
                self.shootGun()
                object_dictionary['r'].engageRobot('attack robot with pistol x', object_dictionary)
            else:
                error()

def error():
        print("*You can't do that*")
        print("type HELP if confused.")
