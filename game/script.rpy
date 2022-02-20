# defining characters

define you = Character("[playername]")
define mom = Character(_('Mom'))
define narrator = Character(_(''), window_background="gui/narratorbox.png")
define haru = Character(_('Haruka'))
define em = Character(_('Emily'))

# parameters

transform evenlefter:
    xalign 0.0
    yalign 1.0

transform slightleft:
    xalign 0.25
    yalign 1.0

image em = im.Scale("em.png", 500, 700)
image haru = im.Scale("haru.png", 500, 700)

# The game starts here.

label start:

$ playername = renpy.input("What is your name?")
$ playername = playername.strip()

if playername == "" :
  $playername = "Sam"
  narrator "Your name has been defaulted to Sam."

scene bedroom evening

narrator "The evening light filters through the dusty window blinds, shining directly on a recently-made bed. You plop down on the bed, rumpling the sheets."

you "*sigh*"

you "My arms are killing me… I definitely lifted 5 boxes too many."

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

return