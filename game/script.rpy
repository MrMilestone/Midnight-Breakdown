# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("") #narrator
define p = Character("Paul") #Main Character
define m = Character("Miska") #Girl NPC
define b = Character("Brother") #No longer used

$ Name = _return


image fr = "forestroad.png"
image frb = "background forest road busstop.png"
image miska i = "mikaidlemclosed.png"
image miska it = "Miska Idle talking.png"

#A1 Branching to different Scene
#A2 Branching to different Scene
#A3 Branching to different Scene
#A4 is End Scene


label start:

    $ Chances = 0
    $ Time = False



    #ACT 1
    scene black
    show povroff
    #phone ping sound
    #image phone

    n "it is a late cold night, lights of various christmas decorations are hanging in peoples gardens"

    n "just as you enter your car to head over to the family dinner you hear your phone ring."
    b "are you coming over already, we have already preparing the food and i haven't heard a word from you"

    p "ugh friend always gets so impatient during the holidays, most of the family probably isn't going to be on time anyways"



    p "probably shouldn't complain to much though, their christmas dinners always taste the best"


    b "hello... do you even have your phone turned on, if you don't respond we are just gonna start without you"


    menu:
        "phone text: give me 5 minutes, i literally just got inside the car":
            n "..."

        "don't respond":
            n "..."

    b "why is it that you can never show up on time anyways, I messaged you serveral times before hand when to be here"

    menu:
        "turn off phone":
            n "beep"

        "phone text: i'm sorry i will try better next time":
            b "you better..."

    #image road block
    "as you were fiddeling with your phone you suddenly see a large barrier blocking the road"

    p "oh darn it just my luck, now i am gonna be late for sure"

    n "After some time driving you come to the conclution: You are lost."

    #ACT2
    scene fr
    show povroff

    n "You have been driving for a few hours"

    n "The road splits into two."
    n "The left path looks more used. The right road looks wider"

    menu:
        "I choose right. The wider the better":
            n "You spot a light at the horizon"

        "I choose to go left. I think more people use this road":
            n "You spot a light at the horizon"


    n "You come to a stop where the light is:"
    hide povroff
    show frb
    show povroff

    n "There is an old bus stop and a what looks to be a girl sitting a the bustop."

    n "Maybe she knows the way around"
    menu:
        "I stop infront and lower my car window":
            jump A1

label A1:

    scene frb


    p "Excuse me, miss"

    m "What's up?"
    menu:
         "I believe Im lost.":
            m "Yeah I noticed."

            p "Do you know a way out of the forest?"
            m "Ofcourse!"


         "Do you know where I am?":
            m "hehe, you lost cutie?"
            p "I believe I am. Do you know a way out of the forest?"
            $ Chances += 1
    hide miska imc
    show miska it
    m "What is your name?"



    menu:
        "Paul":
            m "What a lovely name"
            $ Name = "Paul"

        "I rather not say it":
            m "Ohh. I understand cutie"
            $ Name = "cutie"

        #$ Nanem False

    m "Well [Name], I am Miska. What about an deal?"
    m "If you take me home, I will guide you out of the forest aaaand maybe something more."
    m "How does it sound?"

    menu:
        "Why don't you take the bus?":
            m "I have been waiting for ever for the last bus!"
            m "I think there is no more buses"

        "Im not so sure about that":
            m "Come on [Name], you are not going to leave a girl alone in christmas eve, are you?"


    n "At this point the girl called Miska, is close enough for you to notice how beautiful she is"
    n "Blue eyes, blond hair and amazing lips. She even in a red dress, probably for Christmas eve."


    m "Are you sure I cannot change your mind?"
    m "I dont live that far"

    menu:
        "Can you not call some one up?":
            m "test test"

        "teste test":
            m "test test"

        #m "Since looks like we are both in a rare situation I propose a deal."

    jump A4


label A2:
    scene black
        #show pov view with woman
    m "Ohh! My name is Miska, nice to meet you!"
    menu p:
        "Hi my name is Paul.":
            m "Paul Anderson right?"
            p "How do you know my name?"
            m "well uhh... I heard it from your workplace"

        "That's a very nice name":
            m "Oh! You like it? thank you so much<3"
            $ Chances += 1
            jump A3



label A3:
    scene black
    m "excuse me, I was just looking to help you since you seem to have broken down"
    jump A3

    #ACT 3

label A4:

    scene black
        #play Distant car
    p "Oh thank god he is here"
        #Woman runs into the distance
        #friend appears infornt of car

    b "Hey man who was that person standing by your car?"
    p "Don't worry about it, let's get out of here I will explain later"

    n "[Chances!t]" #print Chances count
        #play car engine Driving






    return
