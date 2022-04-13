# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define p = Character("Paul")
define m = Character("Miska")
define f = Character("Friend")


#A1 Branching to different Scene
#A2 Branching to different Scene
#A3 Branching to different Scene
#A4 is End Scene


label start:

    $ Chances = 0
    $ Time = False



    #SCENE 1
    #phone ping sound
    #image phone
    f "are you coming over already, we have already preparing the food and i haven't heard a word from you"

    p "ugh friend always gets so impatient during the holidays, most of the family probably isn't going to be on time anyways"

    p "probably shouldn't complain to much though, their christmas dinners always taste the best"

    #car engine noise starts
    #radio turns on
    #image driving
    #after a few seconds of driving
    #phone ping

    f "hello... do you even have your phone turned on, if you don't respond we are just gonna start without you"

    menu:
        "phone text: give me 5 minutes, i literally just got inside the car":

        "don't respond":

    f "why is it that you can never show up on time anyways, i messaged you serveral times before hand when to be here"

    menu:
        "turn off phone":

        "phone text: i'm sorry i will try better next time":
    #hard break noises
    #image road block
    "as you were fiddeling with your phone you suddenly see a large barrier blocking the road"

    p "oh darn it just my luck, now i am gonna be late for sure"

    p "maybe i can cut through a forest pathway to take a short cut"

    p "it does look pretty sketchy though, hopefully it actually leads back to the main road"

    #SCENE2

    m "Hello"

    menu:
        "Uhm...Hello...?":
            jump A1
        "Who are you?":
            jump A2
        "What are you doing infront of my car?":
            jump A3

label A1:

    scene black
        #show
    m "What's up?"
    menu:
         "Well, my car has broken down.":
            m "Yeah I noticed. Can you let me inside? My dad ws a mechanic I can probably figure out what is wrong"

            p "No, I would rather not"
            m "Ahw, why not? I just want to help" #Skip to next Dialogue?
            jump A4

         "I am pretty tired":
            m "hehe, you look very cute when you are tired"
            $ Chances += 1
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
            jump A4



label A3:
    scene black
    m "excuse me, I was just looking to help you since you seem to have broken down"
    jump A4


label A4:

    scene black
        #play Distant car
    p "Oh thank god he is here"
        #Woman runs into the distance
        #friend appears infornt of car

    f "Hey man who was that person standing by your car?"
    p "Don't worry about it, let's get out of here I will explain later"

    n "[Chances!t]"
        #play car engine Driving






    return
