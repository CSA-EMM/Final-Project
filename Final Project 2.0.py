# Elijah Mitchell
# 4/19/17
# period 2
import time
import random

y = 0
x = 0

STR = 0
END = 0
AGL = 0
MAG = 0
HEALTH = 100
th = 5

lvl = 1
exp = 0

mon = ""

meleebase = 2
magicbase = 2

mh = 0

rs = ''
xdown = random.randrange(50, 101)
ydown = random.randrange(50, 101)
print(xdown, ydown)


def youwin():
    print("Well... that was faster than I thought it would be... any way you did it! Here's your pay check!")
    print("You got 10 gold coins....")
    time.sleep(3)
    quit()


def gameover():
    print('You have been killed... oh well time to send in the next sucker...')
    time.sleep(3)
    quit()


def mt(m):
    global AGL
    global HEALTH
    global END
    dc = AGL + 1
    mhc = random.randrange(0, int(dc))
    if m == 1:
        mn = 'Goblin'
        print('The ' + mn + ' is attacking you!')
        md = 10
        if mhc == 0:
            rd = md/END
            HEALTH -= rd
            print("The " + mn + " did " + str(md) + " to you!")
            time.sleep(3)
            combat(m)
            if HEALTH <= 0:
                print("You died!")
                time.sleep(3)
                gameover()
        else:
            print("The " + str(mn) + " missed!")
            combat(m)
    elif m == 2:
        mn = 'Ogre'
        print('The ' + mn + ' is attacking you!')
        md = 20
        if mhc == 0:
            rd = md/END
            HEALTH -= rd
            print("The " + mn + " did " + str(md) + " to you!")
            time.sleep(3)
            combat(m)
            if HEALTH <= 0:
                print("You died!")
                time.sleep(3)
                gameover()
        else:
            print("The " + str(mn) + " missed!")
            combat(m)
    elif m == 3:
        mn = 'Troll'
        print('The ' + mn + ' is attacking you!')
        md = 15
        if mhc == 0:
            rd = md/END
            HEALTH -= rd
            print("The " + mn + " did " + str(md) + " to you!")
            time.sleep(3)
            combat(m)
            if HEALTH <= 0:
                print("You died!")
                time.sleep(3)
                gameover()
        else:
            print("The " + str(mn) + " missed!")
            combat(m)
    elif m == 4:
        mn = 'Rabid Flying and Flailing Squid'
        print('The ' + mn + ' is attacking you!')
        md = 30
        if mhc == 0:
            rd = md/END
            HEALTH -= rd
            print("The " + mn + " did " + str(md) + " to you!")
            time.sleep(3)
            combat(m)
            if HEALTH <= 0:
                print("You died!")
                time.sleep(3)
                gameover()
        else:
            print("The " + str(mn) + " missed!")
            combat(m)
    elif m == 5:
        mn = 'Evil Overlord of Chaos'
        print('The ' + mn + ' is attacking you!')
        md = 70
        if mhc == 0:
            rd = md/END
            HEALTH -= rd
            print("The " + mn + " did " + str(md) + " to you!")
            time.sleep(3)
            combat(m)
            if HEALTH <= 0:
                print("You died!")
                time.sleep(3)
                gameover()
        else:
            print("The " + str(mn) + " missed!")
            combat(m)


def monsterspawner():
    global mon
    global mh
    global lvl
    cm = random.randrange(1, 5)
    if cm == 1:
        mon = 'Goblin'
        mh = 50
    elif cm == 2:
        mon = 'Ogre'
        mh = 10*lvl
        combat(cm)
    elif cm == 3:
        mon = 'Troll'
        mh = 8*lvl
        combat(cm)
    elif cm == 4:
        if y >= 50:
            if x >= 50:
                mon = 'Rabid Flying and Flailing Squid'
                mh = 20*lvl
                combat(cm)
            else:
                monsterspawner()
        else:
            monsterspawner()


def combat(cm):
    global mon
    global mh
    global HEALTH
    global rs
    global exp
    global AGL

    print("There is a " + str(mon) + " standing in your way!")
    cc = int(input("What would you like to do?\n"
                   "1. Fight\n"
                   "2. Magic\n"
                   "3. RUN!\n"))
    if cc == 1:
        print("You swing at the " + str(mon) + " with all your might!")
        hc = AGL + 5
        hc = random.randrange(0, int(hc))
        if hc == 0:
            print("You missed!")
            mt(cm)
        else:
            print("The hit connected!")
            age = STR + 1
            damage = meleebase * age
            print('You did ' + str(damage) + ' damage!')
            mh -= damage
            if mh <= 0:
                print('You killed the Monster!')
                exp += 10
                time.sleep(3)
                if cm == 5:
                    youwin()
                menu()
            else:
                mt(cm)
    if cc == 2:
        mm = MAG / 10
        if rs == '2':
            print("You have the FIRE spell along with the HEAL spell thanks to your heritage!")
            s = input("What spell do you want to use?\n"
                      "1. HEAL\n"
                      "2. FIRE\n"
                      "3. Never mind")
            if s == '1':
                HEALTH += 10 * mm
                mt(cm)
            elif s == '2':
                mh -= 10 * mm
                if mh <= 0:
                    print('You killed the Monster!')
                    exp += 10
                    time.sleep(3)
                    if cm == 5:
                        youwin()
                    menu()
                else:
                    mt(cm)
            elif s == 3:
                combat(cm)
            else:
                print("Invalid.")
                combat(cm)

        else:
            print("You have the HEAL spell.")
            s = input("Do you want to use a spell?\n"
                      "1. HEAL\n"
                      "2. Never mind")
            if s == '1':
                HEALTH += 10 * mm
                mt(cm)
            elif s == '2':
                combat(cm)
            else:
                print("Invalid.")
                combat(cm)
    elif cc == '3':
        print("You try to run away...")
        time.sleep(3)
        rc = AGL + 1
        run = random.randrange(0, int(rc))
        if run == 0:
            print('You failed to escape.')
            mt(m)
        else:
            print('You got away!')
            menu()


def movement(m):
    global y
    global x
    if m == "north":
        y += 1
        if y > 100:
            print("This is the edge of the world...")
            y -= 1
        cyn = random.randrange(1, 3)
        if cyn == 1:
            print("No enemies appeared.")
            time.sleep(3)
            menu()
        if cyn == 2:
            print("An enemy stands in you way!")
            monsterspawner()

    elif m == "south":
        y -= 1
        if y <= -100:
            print("This is the edge of the world...")
            y += 1
        cyn = random.randrange(1, 3)
        if cyn == 1:
            print("No enemies appeared.")
            time.sleep(3)
            menu()
        if cyn == 2:
            print("An enemy stands in you way!")
            monsterspawner()

    elif m == "east":
        x += 1
        if x >= 100:
            print("This is the edge of the world...")
            x -= 1
        cyn = random.randrange(1, 3)
        if cyn == 1:
            print("No enemies appeared.")
            time.sleep(3)
            menu()
        if cyn == 2:
            print("An enemy stands in you way!")
            monsterspawner()

    elif m == "west":
        x -= 1
        if x <= -100:
            print("This is the edge of the world...")
            x += 1
        cyn = random.randrange(1, 3)
        if cyn == 1:
            print("No enemies appeared.")
            time.sleep(3)
            menu()
        if cyn == 2:
            print("An enemy stands in you way!")
            monsterspawner()
    else:
        print("That is not a valid movement!")
        menu()


def statpoints():
    global STR
    global END
    global AGL
    global MAG
    print("You have gotten a stat point!")
    sp = int(input("Where would you like to assign it?\n"
                   "1. STRENGTH\n"
                   "2. ENDURANCE\n"
                   "3. AGILITY\n"
                   "4. MAGIC\n"))
    if sp == 1:
        STR += 1
        print("Here is your final stats: STRENGTH = " + str(STR) + ", ENDURANCE = " + str(END) + ", AGILITY = " + str(
            AGL) + ", MAGIC = " + str(MAG))
        time.sleep(3)
        menu()
    elif sp == 2:
        END += 1
        print("Here is your final stats: STRENGTH = " + str(STR) + ", ENDURANCE = " + str(END) + ", AGILITY = " + str(
            AGL) + ", MAGIC = " + str(MAG))
        time.sleep(3)
        menu()
    elif sp == 3:
        AGL += 1
        print("Here is your final stats: STRENGTH = " + str(STR) + ", ENDURANCE = " + str(END) + ", AGILITY = " + str(
            AGL) + ", MAGIC = " + str(MAG))
        time.sleep(3)
        menu()
    elif sp == 4:
        MAG += 1
        print("Here is your final stats: STRENGTH = " + str(STR) + ", ENDURANCE = " + str(END) + ", AGILITY = " + str(
            AGL) + ", MAGIC = " + str(MAG))
        time.sleep(3)
        menu()
    else:
        print("THAT IS NOT A VALID INPUT!!!!!1!")
        time.sleep(3)
        statpoints()


def level_up():
    global lvl
    global exp
    exp = 0
    lvl += 1

    statpoints()


def boss():
    global mh
    print("Umm... looks like you found the boss...")
    time.sleep(3)
    mh = 10000
    print("Bosses Health: " + str(mh))
    time.sleep(3)
    combat(5)


def stairs():
    print('You travel down the steps in to the dark, foreboding mist...')
    time.sleep(3)
    boss()


def menu():
    global x
    global y
    global th
    global HEALTH
    global exp
    global lvl
    global xdown
    global ydown
    global END
    if x == xdown:
        if y == ydown:
            sw = input("You have found a Stairwell! Would you like to go down it?\n"
                       "yes/no\n")
            if sw == 'yes':
                print("You walk down the stair well...")
                time.sleep(3)
                stairs()
            else:
                print('You walk past the Stairwell.')
                time.sleep(3)
                x += 1
                menu()
    if exp >= 10 * lvl:
        print("You level upped!")
        time.sleep(3)
        level_up()
        print('                            \n')
    print("Welcome to the menu!")
    print("Your current coordinates: " + str(x) + ", " + str(y))

    print("Health: " + str(HEALTH) + " LVL:" + str(lvl) + " EXP: " + str(exp))
    o = input("What do you want to do?\n"
              "1. Movement\n"
              "2. Heal\n"
              "3. Quit\n")
    if o == '1':
        m = input("Which way do you want to move?\n"
                  "North, East, South or West?\n")
        movement(m)
    elif o == '2':
        print("You have " + str(th) + " heals left.")
        th -= 1
        HEALTH += 10
        menu()
    elif o == '3':
        q = input("Do you really want to quit?\n"
                  "Yes / No\n")
        if q == 'yes':
            print("Quiting...")
            time.sleep(3)
            quit()
        else:
            print("Okay then! Let's continue!")
            menu()
    else:
        print("That is not a valid input!")
        menu()


def finish():
    global rs
    global STR
    global END
    global AGL
    global MAG
    if rs == '1':
        STR += 1
        END += 1
        AGL += 1
        MAG += 1
        print("Here is your final stats: STRENGTH = " + str(STR) + ", ENDURANCE = " + str(END) + ", AGILITY = " + str(
            AGL) + ", MAGIC = " + str(MAG))
        time.sleep(3)
        print("                                        ")
        menu()
    elif rs == '2':
        STR -= 1
        END -= 0
        AGL += 2
        MAG += 3
        print("Here is your final stats: STRENGTH = " + str(STR) + ", ENDURANCE = " + str(END) + ", AGILITY = " + str(
            AGL) + ", MAGIC = " + str(MAG))
        time.sleep(3)
        print("                                        ")

        menu()
    elif rs == '3':
        STR += 2
        END += 3
        # no stat bonus for agl
        MAG -= 1
        print("Here is your final stats: STRENGTH = " + str(STR) + ", ENDURANCE = " + str(END) + ", AGILITY = " + str(
            AGL) + ", MAGIC = " + str(MAG))
        time.sleep(3)
        print("                                        ")

        menu()
    else:
        print("You broke the system.. great job now you have to do this all over again...\n"
              "RESTARTING IS A GO!")
        time.sleep(3)
        startup()


def stats():
    global STR
    global END
    global AGL
    global MAG

    print("Okay now that you have picked your race we can start buffing you up.")
    print("You start with 5 different points to use to buff up your new body."
          "The main places you can put those points into are STRENGTH, ENDURANCE, AGILITY, and MAGIC...\n"
          "  I'm certain i don't need to explain what they do...")
    try:
        STR = int(input("How many points would you like to put into STRENGTH?\n"))
        END = int(input("How many points would you like to put into ENDURANCE?\n"))
        AGL = int(input("How many points would you like to put into AGILITY?\n"))
        MAG = int(input("How many points would you like to put into MAGIC?\n"))
    except ValueError:
        print("THAT'S NOT A VALID INPUT!")
        time.sleep(3)
        stats()

    if STR < 0:
        print("YOU CAN'T DO THAT!!!!")
        time.sleep(3)
        stats()
    if END < 0:
        print("YOU CAN'T DO THAT!!!!")
        time.sleep(3)
        stats()
    if AGL < 0:
        print("YOU CAN'T DO THAT!!!!")
        time.sleep(3)
        stats()
    if MAG < 0:
        print("YOU CAN'T DO THAT!!!!")
        time.sleep(3)
        stats()
    total = STR + END + AGL + MAG
    if total > 5:
        print("THAT'S TOO MANY POINTS! SAVE SOME FOR THE OTHERS!")
        time.sleep(3)
        stats()
    else:
        print("Great now to show you the finished product!")
        finish()


def new():
    global rs
    print("As per usual you can't look the same as you do now. So, pick a new race, or, stay human, we"
          " just have to make you look different.")
    time.sleep(3)
    race = input("Here is the list of races you can be in the world we'll be sending you to:\n"
                 "1. Human\n"
                 "2. Elf\n"
                 "3. Orc\n")
    if race == '1':
        print("So you're still a human... kinda boring...")
        time.sleep(3)
        rs = race
        stats()
    elif race == '2':
        print("Ah, so you chose to be a graceful elf... and as fragile as a twig.")
        time.sleep(3)
        rs = race
        stats()
    elif race == '3':
        print("You chose to be a... dumb, smelly, brute... to live as for at LEAST a month..."
              " oh well, at least you won't die easily.")
        time.sleep(3)
        rs = race
        stats()
    else:
        print("THAT IS NOT A VALID RACE!")
        new()


def intro():
    print("Welcome to the reincarnation building! You've been chosen to be reincarnated into a new world! Once there, "
          "you must try to survive and make it to the EVIL WIZARD"
          " and slay him... or else you won't get your pay check!")
    time.sleep(3)
    new()


def mainmenu():
    m = input("Please pick an option, using the number by said option:\n"
              "1. New game\n"
              "2. Exit Game\n")
    if m == '1':
        print("New Game")
        time.sleep(3)
        intro()
    elif m == '2':
        print("Exiting Game.")
        time.sleep(3)
        quit()
    else:
        print("This is not a viable choice.")
        mainmenu()


def startup():
    print("Hello and welcome to the Wanderer.")
    time.sleep(3)
    mainmenu()


startup()
