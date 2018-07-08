from items import *

interactionList = ['take', 'punch', 'kick', 'break', 'drop', 'climb', 'open', 'attack', 'shoot']
communicationList = ['speak', 'communicate', 'talk']
attackList = ['punch' ,'punch the', 'kick', 'kick the', 'attack', 'attack the']
for i in range(len(communicationList)):
    communicationList.append(communicationList[i] + ' with')
    communicationList.append(communicationList[i] + ' to')

class interactable(object):
    def __init__(self):
        pass

    def interactWithObject(self, UI):
        self.ui = UI.rsplit(' ', 1)[0]

    def getUI(self):
        return self.ui.lower()

class character(interactable):
    def __init__(self):
        interactable.__init__(self)
        self.dead = False
        self.handBroken = False

    def killed(self):
        self.dead = True

    def isDead(self):
        return self.dead

    def breakHand(self):
        self.handBroken = True
    def handBroken(self):
        return self.handBroken

class player(character):
    def revived(self):
        self.dead = False


class robot(character):

    def __init__(self):
        character.__init__(self)
        self.awake = False
        self.canBeCommanded = False
        self.robotFollowsPlayer = False

    def engageRobot(self, UI, object_dictionary):
        if self.isDead():
            print("The robot doesn't seem responsive...")
        else:
            self.interactWithObject(UI)
            if self.getUI() in communicationList and self.isAwake():
                self.RobotConv()
            elif self.getUI() in communicationList and not self.isAwake():
                print("The robot doesn't seem to be... on.")
            elif (self.getUI() == 'punch' or self.getUI() == 'punch the') and object_dictionary['p'].handBroken:
                print("Maybe one broken hand is enough....")
            elif self.getUI() in attackList or self.getUI() == 'attack robot with lamp' or self.getUI() == 'attack robot with pistol':
                self.RobotBattle(object_dictionary)
            else:
                error()

    def RobotBattle(self, object_dictionary):
        if self.getUI() != 'attack robot with pistol':
            if (self.getUI() == 'punch' or self.getUI() == 'punch the') and not object_dictionary['p'].handBroken:
                print("You swing at the robot!")
                input("...")
                print("You broke your hand...")
                object_dictionary['p'].breakHand()
            elif self.getUI() == 'kick' or self.getUI() == 'kick the':
                print("You give the metallic robot the boot!")
                input("...")
                print("It has virtually no effect...")
            elif self.getUI() == 'attack' or self.getUI() == 'attack the':
                print("You pounce at the robot like a leapord!")
                input("...")
                print("It seems you have zero combat skills... so you mostly just flop on top of it...")
                input("...")
            elif self.getUI() == 'attack robot with lamp':
                print("You throw the lamp at the robot!")
                input("...")
                print("It shatters on impact...")
                object_dictionary['l'].breaks(object_dictionary)
                input("...")
                print("It seems to have no effect...")
                input("...")
            if self.isAwake():
                print("'Please.. you aren't yourself.', the robot sounds concerned.")
                input("...")
                print("'If you need to we can talk, but for now we can't go anywhere....please be patient'")

            else:
                object_dictionary['r'].awaken()
                print("The robot opens its eyes as if waking up from a deep slumber...")
                input("...")
                print("'Oh... dear. How long have you been awake?', it says in an almost fatherly tone.")
                input("...")
                print("'You must have no idea what's going on... please... let's talk'")

        elif self.getUI() == 'attack robot with pistol':
            print("You take aim and blast away at the robots head!")
            input("...")
            print("Out of nervousness you empty the entire clip!")
            for i in range(object_dictionary['g'].getBulletCount() + 1):
                object_dictionary['g'].shootGun()
                print("BANG!")
            input("...")
            print("The head shatters into pieces leaving fragments of its human, metallic face scattered across the floor.")
            object_dictionary['r'].killed()
        else:
            error()

    def RobotConv(self):
        print("'Yes...yes. I am sure you are very confused.' the robot sighs.")
        input("...")
        print("'Please, ask me anything...'")
        input("...")
        question = input("<ASK QUESTION>")

        if "where am i" in question.lower():
            print("'Well... you are...here. To be honest, I don't really know quite myself.'")
        elif "what am i" in question.lower() or "who am i" in question.lower():
            print("'There was an....accident. I am not sure how much you...actually want to know. For right now, let's focus on surving.'")
        elif "who are you" in question.lower():
            print("'Well...you can call me... Mr. Robot.', it chuckles.")
            input("...")
            print("'Yes... Call me Mr.Robot.'")
        elif "can we leave" in question.lower() or "open" in question.lower() or "outside" in question.lower():
            print("'No... I am so sorry. We can't go outside. Honestly... I think we are done for. Out there are countless dangers...' the robot apologetically explains.")
            input("...")
            print("'... and in here... we aren't going to last much longer.'")
        elif "help" in question.lower():
            print("'I am trying to help you! Though.... I am out of ideas...' the robot sighs.")
            input("...")
            print("'Look... I've given up, but this situation isn't your fault...' the robot says.")
            input("...")
            print("'Command me... I will do what you ask.' the robot says.")
            input("...")
            print("You can now command the robot: COMMAND ROBOT <COMMAND> ... EXAMPLE: COMMAND ROBOT KICK DOOR")
            self.canBeCommanded = True
        else:
            print("'Sorry... I don't understand your question, but we may both be a little...off.', it says apologetically.")

    def robotCommand(self, command, object_dictionary):
        if self.getCanBeCommanded() and not self.isDead():
            if "door" in command.lower():
                if not object_dictionary['d'].getBrokenBarricade():
                    if "kick door" in command.lower():
                        print("Mr. Robot kicks down the door!")
                        object_dictionary['d'].breaks()
                    elif "punch door" in command.lower():
                        print("Mr. Robot punches the door!")
                        input("...")
                        print("It smashes to bits!")
                        object_dictionary['d'].breaks()
                    elif "break door" in command.lower():
                        print("Mr. Robot smashes the door to bits!")
                        object_dictionary['d'].breaks()

                else:
                    print("'Not much I can do to the door at this point...' says the robot.")

            elif "window" in command.lower():
                if not object_dictionary['w'].isBroken():
                    if "kick window" in command.lower():
                        print("'I don't think I can reach the window with my foot...', the robot apologizes.")
                        object_dictionary['w'].breaks()
                    elif "punch window" in command.lower():
                        print("Mr. Robot punches the window!")
                        input("...")
                        print("It smashes to bits!")
                        object_dictionary['w'].breaks()
                    elif "break door" in command.lower():
                        print("Mr. Robot smashes the window to bits!")
                        object_dictionary['w'].breaks()

                else:
                    print("'Not much to do to the window now...' says the robot.")

            else:
                print("'I don't think I can... or should do that.', the robot says.")
                input("...")
                print("'There are limits to my service...'")



        else:
            error()

    def awaken(self):
        self.awake = True

    def isAwake(self):
        return self.awake

    def getCanBeCommanded(self):
        return self.canBeCommanded

    def killsPlayer(self, object_dictionary):
        print("The robot jumps up while screaming 'INTRUDER!', and blasts at the door with the pistol!")
        input("...")
        print("You were in the way! Everything fades to black...")
        input("...")
        print("'No....no. I thought you were an intruder... I didn't...', the robot sounds so human...")
        input("...")
        object_dictionary['p'].killed()

    def robotFollows(self):
        self.robotFollowsPlayer = True

    def getRobotFollows(self):
        return self.robotFollowsPlayer



class window(interactable):
    windowInteractionList = ['open', 'punch', 'kick', 'break']
    for i in range(len(windowInteractionList)):
        windowInteractionList.append(windowInteractionList[i] + ' the')

    def __init__(self):
        interactable.__init__(self)
        self.exit = False
        self.broken = False

    def breaks(self):
        self.broken = True

    def isBroken(self):
        return self.broken

    def engageWindow(self, UI, object_dictionary):
        self.interactWithObject(UI)
        if self.getUI() in self.windowInteractionList and not object_dictionary['r'].isAwake() and self.isBroken() == False and not object_dictionary['r'].isDead():
            print("You walk towards the window and reach over the robot.")
            input("...")
            print("The robot's eyes jerk open and it jolts to its feet.")
            input("...")
            print("'You musn't leave!!!', it screams in an electronic, desperate voice.")
            object_dictionary['r'].awaken()

        elif self.getUI() in self.windowInteractionList and object_dictionary['r'].isAwake() and self.isBroken() == False and not (object_dictionary['r'].isDead() or object_dictionary['r'].getCanBeCommanded()):
            print("'NO! You must stop!', the robot screams.")

        elif self.getUI() in self.windowInteractionList and not self.isBroken() and not (self.getUI() == 'open' or self.getUI() == 'open the') and (object_dictionary['r'].getCanBeCommanded() or object_dictionary['r'].isDead()):
            print("You walk over and smash the window.")
            input("...")
            print("There is glass everywhere now.")

        elif (self.getUI() == 'open the' or self.getUI() == 'open') and (object_dictionary['r'].getCanBeCommanded() or object_dictionary['r'].isDead()):
            print("You walk over and open the window.")
            input("...")

        elif self.getUI() == 'exit' or self.getUI() == 'exit the':
            if object_dictionary['r'].getCanBeCommanded() or object_dictionary['r'].isDead():
                print("You climb up and out the window.")
                self.exitThrough()
                input("...")
                if not object_dictionary['r'].isDead():
                    print("The robot follows without saying a word...")
                    object_dictionary['r'].robotFollows()
            else:
                print("'No... don't go out there.' says the robot.")
        elif self.getUI() == 'break window with lamp' and self.isBroken() == False:
            print("You throw the lamp at the window with ferocious intensity!")
            object_dictionary['l'].breaks(object_dictionary)
            input("...")
            print("The window shatters instantly.")
            self.breaks()
            input("...")


            if not object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead():
                object_dictionary['r'].killsPlayer(object_dictionary)

            elif object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead():
                print("'Why would you do that?', the robot asks.")
                input("...")
                print("'What a bother', it complains.")



        elif self.getUI() == 'shoot window with pistol' and self.isBroken() == False:

            print("You blast away at the window!")
            print("It shatters spreading glass all over the floor!")
            self.breaks()
            input("...")
            if not object_dictionary['r'].isAwake():
                object_dictionary['r'].awaken()
                print("The robot jerks up to its feet!")
                input("...")
                print("'Oh. You are awake.... please... let's speak... don't do anything...drastic.', the robot pleads.")
                input("...")
                print("You have " + str(object_dictionary['g'].getBulletCount()) + " bullets left.")
            else:
                print("'Great! Now there's glass everywhere!', the robot's sarcasm rings through the room...")
                input("...")

        elif (self.getUI() == 'shoot window with pistol' or self.getUI() == 'break window with lamp' or self.getUI() in self.windowInteractionList) and self.isBroken() == True:
            print("The window is already shattered....")
            input("...")

        else:
            error()
    def exitThrough(self):
        self.exit = True

    def getHasBeenExitThrough(self):
        return self.exit

class door(interactable):
    def __init__(self):
        interactable.__init__(self)
        self.exit = False
        self.brokenBarricade = False

    def engageDoor(self, UI, object_dictionary):
        self.interactWithObject(UI)

        if self.getUI() == 'open' or self.getUI() == 'open the':
            if not self.getBrokenBarricade():
                print("The door is barricaded shut! You will have to be more crafty.")
            else:
                if object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead() and not object_dictionary['r'].canBeCommanded():
                    print("'No! Don't try to go out there!' the robot screams.")
                else:
                    print("You walk over and open the door...")
                    input("...")

        elif self.getUI() == 'exit' or self.getUI() == 'exit the':
            if self.getBrokenBarricade() and (object_dictionary['r'].getCanBeCommanded() or object_dictionary['r'].isDead()):
                print("You exit through the door.")
                self.exitThrough()
                input("...")
                if not object_dictionary['r'].isDead() and object_dictionary['r'].getCanBeCommanded():
                    print("The robot follows behind you.")
                    object_dictionary['r'].robotFollows()
            else:
                print("The door is barricaded!")



        elif (self.getUI() == 'punch' or self.getUI() == 'punch the') and object_dictionary['p'].handBroken:
            print("Maybe one broken hand is enough...")
        elif (self.getUI() == 'punch' or self.getUI() == 'punch the') and not object_dictionary['p'].handBroken:
            print("You punch the door! What masculinity! What prowess!")
            input('...')
            print("You broke your hand...")
            object_dictionary['p'].breakHand()
        elif self.getUI() == 'kick' or self.getUI() == 'kick the':
            print("You kick the door! A loud thud rings through the air.")
            input('...')
            if object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead():
                print("'What are you doing?!', screams the robot behind you.")
                input('...')
                print("'There is nothing for you out there.', it says in a tired tone.")
                input('...')
            elif not object_dictionary['r'].isAwake() and not object_dictionary['r'].isDead():
                object_dictionary['r'].killsPlayer(object_dictionary)

        elif self.getUI() == 'break door with lamp':
            object_dictionary['l'].breaks(object_dictionary)
            print("You throw the lamp at the door! It shatters to pieces.")
            input('...')
            if not object_dictionary['r'].isDead():
                if object_dictionary['r'].isAwake():
                    print("'My God, what is wrong with your head!', the robot screams from behind you.")
                    input('...')
                    print("'I don't know what I am going to do with you..', the robot sighs.")
                    input('...')
                    print("'You poor soul'... the electronic voice drips with regret.")
                else:
                    object_dictionary['r'].awaken()
                    object_dictionary['r'].killsPlayer(object_dictionary)


        elif self.getUI() == 'shoot door with pistol':
            print("You shoot at the door with high precision!")
            input("...")
            print("The bullet splinters the wood, but seems to have little effect....")
            input("...")
            if not object_dictionary['r'].isDead():
                if object_dictionary['r'].isAwake():
                    print("'Please stop... don't stress out..', the robot pleads.")
                else:
                    print("The robot awakens!")
                    object_dictionary['r'].awaken()
                    input("...")
                    print("'What are you doing?!', it screams!")
            print("You have " + str(object_dictionary['g'].getBulletCount()) + " bullets left.")
        else:
            error()

    def getBrokenBarricade(self):
        return self.brokenBarricade
    def breaks(self):
        self.brokenBarricade = True
    def exitThrough(self):
        if self.getBrokenBarricade():
            self.exit = True

    def getHasBeenExitThrough(self):
        return self.exit

def error():
    print("*You can't do that*")
    print("type HELP if confused.")
