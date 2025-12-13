# Game script

define anon = Character("???")
define ia = Character("Iris", color="11380C")
define tbr = Character("Player", color="F22C2C") # railroading to be replaced with player choice

label start:

    scene bg pc_house_front

    "Well, here it is. Home sweet home, for at least the next few months."

    "A black cat peeks out the window. Your Aunt Sylvie said the black one is named Ginger."

    anon "Excuse me."

    show  ia neutral

    ia "Hi. I'm Iris. I just wanted to welcome you to the neighborhood."

    "She makes intense eye contact."

    menu:

        "(Have a staring contest.)":
            jump choice1_stare

        "So you live nearby?":
            jump choice1_nearby

    label choice1_stare:

        $ ia_stare = True
        $ ia_nearby = False

        "Her eyes bore into yours. You eventually have to blink."

        jump choice1_done

    label choice1_nearby:

        $ ia_nearby = True
        $ ia_stare = False

        ia "Not really."

        jump choice1_done

    label choice1_done:

        show ia scrutinizing
        
        ia "..."

    show ia neutral

    ia "Here's my contact info. When weird stuff starts happening, give me a call."

    hide ia neutral

    "She walks away."

    tbr "That was \"weird stuff\" already."

    scene bg pc_house_interior

    show shadow curious

    "You recall that the orange cat's name is Shadow."

    return
