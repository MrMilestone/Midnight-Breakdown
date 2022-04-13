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
label A4:
    scene black
    #ACT 3
        # good ending
    m "so do you wanna come to my place?"
    p "i am sorry but i really have to get going now"
    m "i really don't think that you should"
    p "well it's not your choice now is it"
    m "i don't think you understand how much effort i put into this"
    p "what?"
    n "you suddenly feel miska grabing tightly onto your arm"
    m "open the door paul"
        #knife drawing effect
    n "before you can protest, you can feel a knife being held tigthly to your throat"
    n "fear paralyzes you unable to move miska reaches her hand through the window to pull the door open"
    n "at this point you have accepted your fate when you suddenly see headlights in the distance"
        #car honking noise
    n "the moment this happens the presure on your arm is gone as miska has run off into the forest"
    b "hey paul what's going on, who was that woman standing next to your car"
    p "i will explain later let's get home for now"

        #epiloge
    p "that night i ended up calling the police to make a report, but in the end they were never able to find a suspect"
    p "i do wonder sometimes what they would have done if they had managed to get inside my car"
    p "she has seen my license plate, hopefully she doesn't come back to finish the job"
    p "one thing is for sure, i am never driving alone at night again"



        # bad ending
    m "so do you wanna come to my place?"
    p "you know what at this point we have been talking for so long that all the food has probably been eaten already"
    p "so sure why not"
    m "i'm so happy right now, let me get in this is gonna be a very short drive"
    n "you unlock the car door and she gets into the passanger seat on your left"
        #engine starts
    n "after a few minutes of following her directions you notice that the road seems to go deeper and deeper into the forest"
    n "while glancing from the road she seems to be  figeting a lot with her hands"
    n "after a while the road stops and you hit a dead end"
    p "uhm... miska what exactly is this place?"
    m "paul i'm sorry but i haven't been enterily honest with you"
        #knife drawing effect
    n "before you can even say a word you can feel a knife enter your arm"
    n "you try to get out of the car but as you do you can feel the knife going through your back paralyzing you"
    n "your vision goes dark as the repeated stabbing in your back starts to feel faint"
        #epiloge
    n "after not showing up to the christmas dinner the family reported you missing in the early morning"
    n "a search and resque team was sent out finding you 7 hours later laying right outside of your car in a pool of blood"
    n "after a medical examination you were detirmend to have past away from your injuries 12 hours ago"
    n "with no finger prints or witnesses the trail quickly ran cold and no one suspect was ever found"





    return
