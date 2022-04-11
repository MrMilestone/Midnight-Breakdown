# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define m = Character("Miska")




label start:

    $ Chances = 0
    $ Time = False



    #SCENE 1
    scene black


    play sound engineon
    show elieen happy

    # These display lines of dialogue.

    n "Wow time sure flies when you are working, looks like it's already dark, I guess I better get home quick."

    #play audio Radio on
    #play sound Driving

    n "I wonder if there is still anything left to coock with in the fridge"

    n "Maybe I should stop by the store to pick up some extra stuff"

    n "Actually nevermind, I will just order something when I get there"

    #hide povcar

    #show road block

    #play sound Break noises

    #show dark forest road

    n "I wonder if there is still anything left to coock with in the fridge"

    n "What the hell I don't remember this road being worked on I just drove through here this morning"

    n "I guess I will just have to take a detour"
    hide elieen happy

    show ladygaga

    n "This road looks pretty poorly made, I can't imagine anybody ever going through here"

    #play engine stalling

    #hide ladygaga
    #show smoke coming from car

    n "Awh god dammit! Just my luck, hopefully my friend is available to pic me up. Better send him a message."

    #play sound radio off
    #play audio radio

    #show x2 phone pulled up infront with message (Video)

    n "what was that?"

    #show looking out of back window

    n "I swear I just saw something pass by"

    n "I must be seeing shapes in the dark, hopefully my friend gets here soon"

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



    return
