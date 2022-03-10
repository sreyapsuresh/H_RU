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

define you = Character("[name]", window_background="gui/characterbox.png", ctc="ctc_anchored",
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
default child = "child"

# The game starts here.

label start:

stop music fadeout 3.0

label choosename:
$ name = renpy.input("What is your name?", length = 12)
$ name = name.strip()
$ name = name.title()

if name == "" :
  $ name = "Sam"
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
            $ child = "son"
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
            $ child = "daughter"
        "They/Them":
            pass

    menu:

        "'[Their] name is [name] and [theyre] going to play H_RU'. \n Is this right? This can't be changed later."

        "Yes.":
            jump day1start
        "No, let's try something else.":
            jump choosepronoun

#-------------------------------------------------S T O R Y---------------------------------------------
label day1start:

scene bedroom day
with fade
play music "music/Shenanigans!.mp3" loop fadein 1.0 volume 0.1

narrator "A heavy box slams onto the floor with a thud."
you "And that's the last of them!"
narrator "You heave a sigh of relief while stretching your now-sore arms."

menu:
 "Looking around the boxes that are neatly stacked in the otherwise empty room, you feel..."
 "Hopeful":
  jump day1hopeful
 "Anxious":
  jump day1anxious

#--------------------------------------------------------------------------------------------------------
label day1hopeful:
$ feeling = "hopeful"
narrator "You look forward to what this new town holds for you."
narrator "It isn't the big city life you were used to, but you're sure you'll fit right in."
narrator "Your thoughts are interrupted by your mom yelling from downstairs."
mom "[name], make sure you unpack soon!"
narrator "You look forward to tackling everything head-on. But for now, you have some unpacking to do."
scene black
with fade
jump day1unpack
#--------------------------------------------------------------------------------------------------------
label day1anxious:
$ feeling = "anxious"
narrator "You're afraid of what the future holds for you."
narrator "Would you get used to the new school? What if no one liked you?"
narrator "Your worries are interrupted by your mom yelling from downstairs."
mom "[name], make sure you unpack soon!"
narrator "You shake your thoughts away and decide to take your mind off of it by setting up your new room."
scene black
with fade
jump day1unpack
#--------------------------------------------------------------------------------------------------------
label day1unpack:

scene bedroom evening
with fade

narrator "You plop down on your recently-made bed, rumpling the sheets."
narrator "Looking around the room, now illuminated by the evening glow, you can't help but think of your old home."
narrator "It was much larger, and with more memories..."
if feeling == "hopeful":
 narrator "But you're sure that this new place would soon feel like home."
if feeling == "anxious":
 narrator "You're not so sure this place will ever be the same."
narrator "Your thoughts are one again interrupted, this time by a polite knock at your door."
you "Come in!"
narrator "Your mom pokes her head through the door, seemingly impressed that you had unpacked all of the boxes."
mom "Look at you, all set up in your new room... Everything okay?"
you "Yeah mom, I'm fine. Just thinking about the old place."
narrator "Her gaze softens in understanding."
mom "I understand kiddo, but I'm sure you'll fit right in here."
you "I hope so."
narrator "Your mom gives you a warm smile."
mom "Of course you will, you're my [child] after all."
narrator "Your mom's cheery optimism rubs off on you, and you return her smile with one of your own."
mom "Anyways, I came up to let you know that I'll be downstairs preparing dinner."
mom "It'll take a while, so if you want to explore the neighborhood, now might be the time."
you "Are you sure? By myself?"
mom "Yes, but I expect you back home in an hour."
narrator "With that, your mom leaves you alone in your new room."
narrator "You glance down at the phone by your side and it's screen flashes the numbers 6:02."

menu:
 "With an hour to spare, you decide to..."
 "Stay Home":
  jump day1stayhome
 "Explore":
  jump day1explore
#--------------------------------------------------------------------------------------------------------
label day1stayhome:

you "stays home"

label day1explore:

you "explores"
#------------------------------------------G A M E  O V E R----------------------------------------------
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

    centered "Thank you for playing the demo of H_RU."
