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
    scene black


    play sound engineon
    show elieen happy
    show povcar

    # These display lines of dialogue.

    p "Wow time sure flies when you are working, looks like it's already dark, I guess I better get home quick."

    #play audio Radio on
    #play sound Driving

    p "I wonder if there is still anything left to cook with in the fridge"

    p "Maybe I should stop by the store to pick up some extra stuff"

    p "Actually nevermind, I will just order something when I get there"

    #hide povcar

    #show road block

    #play sound Break noises

    #show dark forest road

    p "I wonder if there is still anything left to coock with in the fridge"

    p "What the hell I don't remember this road being worked on I just drove through here this morning"

    p "I guess I will just have to take a detour"
    hide elieen happy

    show ladygaga

    p "This road looks pretty poorly made, I can't imagine anybody ever going through here"

    #play engine stalling

    #hide ladygaga
    #show smoke coming from car

    p "Awh god dammit! Just my luck, hopefully my friend is available to pic me up. Better send him a message."

    #play sound radio off
    #play audio radio

    #show x2 phone pulled up infront with message (Video)

    p "what was that?"

    #show looking out of back window

    p "I swear I just saw something pass by"

    p "I must be seeing shapes in the dark, hopefully my friend gets here soon"

    #play jumpscare
    #show front view with woman

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
