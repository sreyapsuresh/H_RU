## End Credits Scroll ############################################################
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

## Code Source: https://lemmasoft.renai.us/forums/viewtopic.php?t=42667

transform credits_scroll(speed):
    ypos 3250
    linear speed ypos -3250
    ## Adjust these numbers to be the height of your end credits. Both numbers
    ## should be the same.

## Credits screen.

screen credits():

    ## Ensure that the game_menu screens don't appear and interrupt the credits.
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    ## If a player has seen the end credits before, this button appears.
    if persistent.credits_seen:

        textbutton _("Skip End Credits") action Jump("skip_credits") xalign 0.99 yalign .95

    timer 25.0 action Return()
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.
    ## Ideally, there is some wait time after the the credits reaches the end.

    frame at credits_scroll(15.0):
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            label "Credits" xalign 0.5

            null height 200

            text "Lead Developer" size 100
            null height 50
            text "Sreya Suresh"

            null height 200

            text "Script" size 100
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "Sreya Suresh"

                text "Kunal Jain"

            null height 200

            text "Programming" size 100
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "Sreya Suresh"

                text "Kunal Jain"

            null height 200

            text "Art" size 100
            null height 50

            text "Sprites by Sreya Suresh"

            null height 50

            text "Backgrounds by Noraneko Games"

            null height 200

            text "Composer and Sound Designer" size 100
            null height 50

            text "Tim Reichert"

            null height 200

            text "Special Thanks" size 100
            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "BaiYu"

                text "bobcgames"

                text "CheeryMoya"

            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "minute"

                text "npckc"

                text "deskbot"

            null height 50

            hbox:

                xalign 0.5
                spacing 200

                text "Hannah Lee"

                text "3B ISM"

            null height 50

            hbox:

                xalign 0.5

                text "and Rita Landells"

            null height 200

            text "Made with Ren'Py [renpy.version_only]." size 100

style credits_hbox:
    spacing 40
    ysize 20

style credits_label_text:
    xalign 0.5
    size 200
    text_align 0.5

style credits_text:
    xalign 0.5
    size 80
    justify True
    text_align 0.5
    color "#ffffff"

style backercredits_text:
    xalign 0.5
    size 50
    justify True
    text_align 0.5
    color "#ffffff"
