default blink_timer = renpy.random.random()
init python:
    config.debug_sound = True
    def blink(trans, st, at):
        global blink_timer
        if(st > blink_timer):
            blink_timer = renpy.random.randint(2,4)
            return None
        else:
            return 0
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
define n = Character(_(''), ctc="ctc_anchored",
        ctc_position="fixed")
define haru = Character(_('Haruka'), window_background="gui/characterbox.png", ctc="ctc_anchored",
        ctc_position="fixed")
define nan = Character(_('Nandini'), window_background="gui/characterbox.png", ctc="ctc_anchored",
        ctc_position="fixed")

# parameters

transform evenlefter:
    xalign 0.0
    yalign 1.0

transform slightleft:
    xalign 0.25
    yalign 1.0

image nan = im.Scale("em.png", 500, 700)
image haru = im.Scale("haru.png", 500, 700)

# sprites

image haru_A_blink:
    "harueyesopen.png"
    function blink
    "harueyesclosed.png"
    .15
    repeat

# variables
default feeling = ""
default outside = ""

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
  n "Your name has been defaulted to Sam."

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

show haru_A_blink at right

n "A heavy box slams onto the floor with a thud."
you "And that's the last of them!"
n "You heave a sigh of relief while stretching your now-sore arms."

menu:
 "Looking around the boxes that are neatly stacked in the otherwise empty room, you feel..."
 "Hopeful":
  jump day1hopeful
 "Anxious":
  jump day1anxious
#--------------------------------------------------------------------------------------------------------
label day1hopeful:
$ feeling = "hopeful"

n "You look forward to what this new town holds for you."
n "It isn't the big city life you were used to, but you're sure you'll fit right in."
n "Your thoughts are interrupted by your mom yelling from downstairs."
mom "[name], make sure you unpack soon!"
n "You look forward to tackling everything head-on. But for now, you have some unpacking to do."

scene black
with fade
jump day1unpack
#--------------------------------------------------------------------------------------------------------
label day1anxious:
$ feeling = "anxious"

n "You're afraid of what the future holds for you."
n "Would you get used to the new school? What if no one liked you?"
n "Your worries are interrupted by your mom yelling from downstairs."
mom "[name], make sure you unpack soon!"
n "You shake your thoughts away and decide to take your mind off of it by setting up your new room."

scene black
with fade
jump day1unpack
#--------------------------------------------------------------------------------------------------------
label day1unpack:

scene bedroom evening
with fade

n "You plop down on your recently-made bed, rumpling the sheets."
n "Looking around the room, now illuminated by the evening glow, you can't help but think of your old home."
n "It was much larger, and with more memories..."
if feeling == "hopeful":
 n "But you're sure that this new place would soon feel like home."
elif feeling == "anxious":
 n "You're not so sure this place will ever be the same."
n "Your thoughts are one again interrupted, this time by a polite knock at your door."
you "Come in!"
n "Your mom pokes her head through the door, seemingly impressed that you had unpacked all of the boxes."
mom "Look at you, all set up in your new room... Everything okay?"
you "Yeah mom, I'm fine. Just thinking about the old place."
n "Her gaze softens in understanding."
mom "I understand kiddo, but I'm sure you'll fit right in here."
you "I hope so."
n "Your mom gives you a warm smile."
mom "Of course you will, you're my [child] after all."
n "Your mom's cheery optimism rubs off on you, and you return her smile with one of your own."
mom "Anyways, I came up to let you know that I'll be downstairs preparing dinner."
mom "It'll take a while, so if you want to explore the neighborhood, now might be the time."
you "Are you sure? By myself?"
mom "Yes, but I expect you back home in an hour."
n "With that, your mom leaves you alone in your new room."
n "You glance down at the phone by your side and it's screen flashes the numbers 6:02."

menu:
 "With an hour to spare, you decide to..."
 "Stay home":
  jump day1stayhome
 "Explore":
  jump day1explore
#--------------------------------------------------------------------------------------------------------
label day1explore:

scene livingroom night
with fade

n "If you want to explore as much of the new neighborhood as possible, you have to get going."
n "You run down the stairs of your new house, slightly sliding as your socks glide against the wooden floor."
n "Before stepping out the front door, you reach for a pair of sneakers and quickly slip them on."

menu:
 you "Should I leave now?"
 "Go outside":
  jump day1outside
 "Stay home":
  jump day1stayhome
#--------------------------------------------------------------------------------------------------------
label day1stayhome:

scene kitchen day
with fade

$ outside = "no"

n "You decide to stay home after all and help out your mom with her cooking.
Exploring an unfamiliar neighborhood by yourself seemed like a recipe for disaster."
n "You walk down the stairs and greet your mom with a smile, slipping on a nearby apron while you're at it."
mom "Thanks for coming down to help [name]. We're making pasta today, do you mind handing me the sauce in the fridge?"
n "You open the door to the shiny, new fridge and grab an unopened jar of alfredo sauce."
n "You look forward to cooking your first dinner in the new house, and soon your worries drift away to the sound of boiling water and chopping against a cuttingboard."

jump day1dinner
#--------------------------------------------------------------------------------------------------------
label day1outside:

scene street evening
with fade

$outside = "yes"

n "You waste no time in turning the doorknob and finally exploring your neighborhood."
n "As soon as you open the door, you are greeted by a blast of fresh air and a brilliantly orange sky."
if feeling == "hopeful":
 n "You walk down the street excitedly. You can't wait to meet your neighbors and learn more about your new town."
elif feeling == "anxious":
 n "You walk down the street warily, keeping your eyes peeled for any suspicious behavior."
n "You finally had the chance to look at your new neighborhood and couldn't help but be in awe of your surroundings."
n "Your new house was perfectly framed by two majestic oak trees that were showing the tell-tale signs of Autumn."
n "Bright streetlights illuminated the red-brick sidewalk, and you decide to follow the path as far as it extended."
n "After spending a few minutes walking down the street and taking in the sights around you, you eventually reach a giant tree that marks the end of the path."
you "Well, I guess I should start heading back now..."
n "As you prepare to turn around, your attention is drawn to soft mews in the distance."
you "Huh? That sounds like... a cat?"
n "Finally, after a few seconds of searching, your eyes land on the barely-visible figure of a black cat that stood in the distance."
n "From this distance, you can barely make out its features, but as it starts moving again, you hear the faint ringing of a bell after its every step."
n "You stand there in a trance, staring at the cat. However, it doesn't stay in your line of sigh for long and turns the corner."
n "Your curiosity is piqued by the appearance of the mysterious black cat and you pick up your pace to follow the cat's route."
n "While you don't immediately see it again, you follow the faint jingling of bells and eventually find it turning another corner."
n "This continues down several streets until finally, the black cat walks out of the neighborhood's bounds, into the relatively empty road. It looks like there's a park further down the road."
n "You throw a quick glance at your phone to check the time."
you "5:37. Looks like I followed that cat for longer than I expected..."

menu:
 n "Though you want to continue following the cat, you aren't sure if leaving the neighborhood is the best idea right now. You decide to..."
 "Follow the cat":
  jump day1follow
 "Go back home":
  jump day1goback
#--------------------------------------------------------------------------------------------------------
label day1follow:

scene street evening
with fade

n "You're this far already, surely leaving the neighborhood for a while won't hurt."
n "With a quick glance behind you, you prepare to cross the street to follow the cat."

scene black
with fade

scene park evening
with fade

n "After crossing the street, you finally make it into the park that the cat had disappeared into."
n "The park ends up being more of a mini-playground, with a swingset, a jungle gym, and a multitude of benches and oak trees surrounding it all."
n "Taking in your surroundings, you wonder if parks are normally empty at this time of day. Shrugging off the thought, you continue forward."
n "You walk further inside the playground, trying to find the cat you had followed."
n "Eventually you gave up on looking for the cat that seemed to have disappeared in thin air."
n "You instead decide to take a seat on the nearby swingset, taking extra care to dust off the fallen leaves."
n "After kicking yourself back and forth for a few minutes, you get lost in your own thoughts."
you "I wonder if I'll see that cat again..."

scene black
with fade

jump day1goback
#--------------------------------------------------------------------------------------------------------
label day1goback:

n "Wiping the sweat off your brow, you turn to walk back home."
you "I think home was back this way... or was it that road?"

scene black
with fade

scene street evening
with fade

n "After several minutes of walking down the streets and taking in the houses that surrounded yours, you finally
make your way back to your front door."
n "You turn the doorknob and the door opens."
you "I should probably ask mom for a copy of the keys later, I don't think leaving the house unlocked is safe."

jump day1dinner
#--------------------------------------------------------------------------------------------------------
label day1dinner:

scene livingroom night
with fade

if outside == "yes":
    mom "[name], you're here just in time. Food's on the table."
    n "You run to the bathroom to wash your hands before getting ready to devour the delectable plate of pasta in front of you."
elif outside == "no":
    mom "[name], thank you for helping me today."
    you "Of course!"
    n "You waste no time in washing your hands and getting ready to devour the delectable plate of pasta in front of you."
you "Ahhh... I must be in heaven."
n "Your mom observes your changing facial expression with a smile on her face."
mom "I'm glad you're liking the food, it's a thanks for being such an amazing kid throughout this entire move."
you "Of course! "
n "You turn your focus back to polishing off the plate of pasta in front of you when your mom asks you a question."
mom "How are you feeling?"

menu:
 n "You felt..."
 "Excited":
  jump day1excited
 "Nervous":
  jump day1nervous
#--------------------------------------------------------------------------------------------------------
label day1excited:

$ feeling = "excited"

n "Your mom had recently been transferred to this town for her job, and you were excited for what this change would bring."
mom "You'll be starting school in this week, I really hope you'll enjoy it."
you "Mom, I know that moving here will be great for you. I'm just happy that you're happy. I'm sure I'll fit right in."
n "Your mom flashes you a grateful smile."
mom "Thank you sweetie."

jump day1dinnercont
#--------------------------------------------------------------------------------------------------------
label day1nervous:

$ feeling = "nervous"

n "Your mom had recently been transferred to this town for her job, and while you were excited for her you were
still slightly worried about how this new situation would turn out."
mom "You'll be starting school in this week, I really hope you'll enjoy it."
you "To be honest, I am a little worried about making new friends. I'm not sure how I'll fit in here."
n "Your mom reaches over and reassuredly rubbed the back of your hand."
mom "You'll be great sweetie, don't worry. I know it'll be hard at first but I'll always be here for you."
n "Her encouragement lifts your spirits and you feel more confident."

jump day1dinnercont
#--------------------------------------------------------------------------------------------------------
label day1dinnercont:

n "After finishing your meal, you help your mom wash up and your eyelids start feeling heavy."
you "I think I'm going to head to bed for the night."
mom "Okay [name], thank you for the help. Sweetdreams kiddo."
n "You throw a tired smile her way before crawling your way up the stairs to your room."

scene bedroom night dark
with fade

n "Too sleepy to even change out of the clothes you were in earlier, you fall onto your bed and drift to sleep while thinking about the new school you would have to attend in 2 days."
you "I hope I'll meet someone interesting..."
#--------------------------------------------------------------------------------------------------------
label day2start:

scene bedroom day
with fade

n "You wake up to the sounds of birds chirping outside your windowsill."
you "(I could get used to this every morning.)"
n "Stifling a yawn, you get ready for the day."

scene black
with fade

scene bedroom day
with fade

you "(I should probably go downstairs and talk to Mom.)"

scene livingroom day
with fade

n "After making your way downstairs, you heard your mom talking to someone over the phone."
you "Good morning."
n "Your mom turns to face you, surprised at your appearance."
mom "Hey kiddo, you can fix yourself some breakfast. I'm just going to be cleaning today"
you "Sounds good!"

scene kitchen day
with fade

n "You take a long look over the recently-stocked pantry and eeventually settle on your favorite brand of cereal and waste no time in scarfing it down."

scene black
with fade

scene livingroom day
with fade

you "Hey mom, do you need me to do anything today?"
n "Your mom straightens her back, turning away from the boxes on the living room floor."
mom "Well. if you don't mind, I would love some help unpacking these boxes."
n "She gestures at the large boxes sloppily labelled."
you "Sure."

scene black
with fade

scene livingroom evening
with fade

n "Unpacking the remaining boxes ended up taking longer than you expected, and by the time you were done the sun had already begun to set."
mom "Thanks [name], I think we're officiall all moved in now!"
n "You look around the fully furnished room and heave a sigh of relief."
you "Finally! I don't think I could hold another box for the rest of my life."
n "Your mom rolls her eyes at your exclamation and stands up."
mom "First day of school tomorrow. I'll drop you off for your first day."
n "You groan at the reminder of school tomorrow."
you "Okay... Are you sure I have to go?"
n "You put on your best attempt at puppy-dog eyes, but your efforts prove futile as your mom laughs in your face."
mom "Yes, I'm sure."
n "Now its your turn to roll your eyes, throwing your hands up in defeat."
you "Fineeeeee."
mom "Did you check out the school's website yet?"
you "No, not yet."

menu:
 mom "[name]... do you even know what school you're going to starting tomorrow?"
 "Of course":
  jump day2careful
 "Uh...":
  jump day2careless
#--------------------------------------------------------------------------------------------------------
label day2careful:

you "Of course I have, Southview is the only highschool for miles."
mom "I knew I could rely on you for being on top of things."

jump day2end
#--------------------------------------------------------------------------------------------------------
label day2careless:

you "Uh... Yeah of course?"
n "Your statement ends up coming out more as a question."
n "Your mom simply sighs in repsponse."
mom "You know, it would do you some good to stop procrastinating all the time. You'll be going to Southview High. It's the only school around for miles."

jump day2end
#--------------------------------------------------------------------------------------------------------
label day2end:


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
