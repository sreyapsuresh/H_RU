init python:
    config.debug_sound = True
# adding the click-to-continue button in textbox -- creds: CheeryMoya
image ctc_anchored:
       "gui/arrow.png"
       yalign 0.96 xalign 0.85 #Adjust these numbers to fit your own textbox
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat

# defining characters

define you = Character("[playername]", window_background="gui/characterbox.png", ctc="ctc_anchored",
        ctc_position="fixed")
define mom = Character(_('Mom'), window_background="gui/characterbox.png", ctc="ctc_anchored",
        ctc_position="fixed")
define narrator = Character(_(''), ctc="ctc_anchored",
        ctc_position="fixed")
define haru = Character(_('Haruka'), window_background="gui/characterbox.png", ctc="ctc_anchored",
        ctc_position="fixed")
define em = Character(_('Emily'), window_background="gui/characterbox.png", ctc="ctc_anchored",
        ctc_position="fixed")

# parameters

transform evenlefter:
    xalign 0.0
    yalign 1.0

transform slightleft:
    xalign 0.25
    yalign 1.0

image em = im.Scale("em.png", 500, 700)
image haru = im.Scale("haru.png", 500, 700)

# pronouns <3 -- creds: deskbot

default Their = "Their"
default their = "their"
default Theirs = "Theirs"
default theirs = "theirs"
default They = "They"
default they = "they"
default Themself = "Themself"
default themself = "themself"
default Them = "Them"
default them = "them"
default Theyre = "They're"
default theyre = "they're"
default TheyWere = "They were"
default theyWere = "they were"

# The game starts here.

label start:

stop music fadeout 3.0

label choosename:
$ playername = renpy.input("What is your name?", length = 12)
$ playername = playername.strip()
if playername == "" :
  $playername = "Sam"
  narrator "Your name has been defaulted to Sam."

  jump choosepronoun

label choosepronoun:
    menu:
        "What pronouns do you use?"

        "He/Him":
            $ Their = "His"
            $ their = "his"
            $ Theirs = "His"
            $ theirs = "his"
            $ They = "He"
            $ they = "he"
            $ Themself = "Himself"
            $ themself = "himself"
            $ Them = "Him"
            $ them = "him"
            $ Theyre = "He's"
            $ theyre = "he's"
            $ TheyWere = "He was"
            $ theyWere = "he was"
        "She/Her":
            $ Their = "Her"
            $ their = "her"
            $ Theirs = "Her"
            $ theirs = "her"
            $ They = "She"
            $ they = "she"
            $ Themself = "Herself"
            $ themself = "herself"
            $ Them = "Her"
            $ them = "her"
            $ Theyre = "She's"
            $ theyre = "she's"
            $ TheyWere = "She was"
            $ theyWere = "she was"
        "They/Them":
            pass

    "'[Their] name is [playername] and [theyre] going to play H_RU.'"

    menu:

        "Is this right? This can't be changed later."

        "Yes.":
            jump intro

        "No, let's try something else.":
            jump choosepronoun

label intro:
scene bedroom evening
play music "music/Shenanigans!.mp3" loop fadein 1.0 volume 0.1

narrator "The evening light filters through the dusty window blinds, shining directly on a recently-made bed. You plop down on the bed, rumpling the sheets."

you "*sigh*"

you "My arms are killing me... I definitely lifted 5 boxes too many."

narrator "You hear a polite knock at the half-open door to your room"

mom "Sorry sweetie, I didn’t think the movers would bail so suddenly. Think on the bright side though, at least you're getting in the exercise that you wanted!"

narrator "You grumble in mild annoyance"

you "Moooom..."

mom "I know, I know. I'll be downstairs preparing dinner, but it's probably going to take a while."

you "Do you think I could take a break from moving boxes?"

narrator "Your mom thinks for a second, and then nods her head"

mom "Sure, just be down by 7. We're having Pasta tonight!"

you "Thanks mom! You're the best!"

narrator "You have the next hour all to yourself, and you can spend that time doing whatever you want..."

menu:
 "What do you want to do?"
 "Stay home and help mom with dinner.":
  jump soon
 "Go explore the new neighborhood.":
  jump later

label soon:
you "first"
jump cont

label later:
you "second"
jump cont

label cont:
scene hall day
show haru at center

haru "It's nice to meet you [playername]  ... I'm Haruka."

show em at right

em "Hey new kid! Wait up!"

## This ends the replay mode segment. Doesn't affect normal gameplay.
$ renpy.end_replay()

label credits:

    # End Credits

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ quick_menu = False

    ## We hide the textbox as well so it doesn't mess with things
    window hide

    scene black with fade

    ## Find "End Credits Scroll" in extras.rpy to change text.
    call screen credits

    $ persistent.credits_seen = True

    scene black with fade

    # Players can skip the credits in subsequent playthroughs of the game.
    label skip_credits:

        pass

    ## We re-enable the quickscreen as the credits are over.

    $ quick_menu = True

    centered "Thank you for playing H_RU."
