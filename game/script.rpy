# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define m = Character("Miska")


# The game starts here.

label start:

    $ Chances = 0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    #SCENE 1
    scene black


    play sound engineon
    show eileen happy

    # These display lines of dialogue.

    n "Wow time sure flies when you are working, looks like it's already dark, I guess I better get home quick."

    n ""
    #play sound Radio on - Driving sound

    n "I wonder if there is still anything left to coock with in the fridge"

    n "Maybe I should stop by the store to pick up some extra stuff"

    n "Actually nevermind, I will just order something when I get there"

    #play sound Break noises
    show eileen happy

    n "I wonder if there is still anything left to coock with in the fridge"

    n "What the hell I don't remember this road being worked on I just drove through here this morning"

    n "I guess I will just have to take a detour"
    hide eileen happy

    show ladygaga

    n "This road looks pretty poorly made, I can't imagine anybody ever going through here"



    #play engine stalling






    return
