# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define m = Character("Miska")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #play sound
    show eileen happy

    # These display lines of dialogue.

    n "Wow time sure flies when you are working, looks like it's already dark, I guess I better get home quick."

    scene bg black

    show eileen happy

    n "I wonder if there is still anything left to coock with in the fridge"



    # This ends the game.


    return
