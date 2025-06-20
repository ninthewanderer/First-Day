# The script of the game goes in this file.

###### NOTE TO SELF ON MODIFIED FILES: ######
# - created characters.rpy and therapy.rpy
# - modified screens.rpy and gui.rpy
# - backups for screens.rpy and gui.rpy are in my downloads folder


###### VARIABLES ######
# annoyance tracks gosfrid's annoyance with lao based on player choices.
# at the end of the game, the amount of annoyance determines the ending received.
define annoyance = 0


###### START OF STORY ######
label start:
    play audio "bacon_sizzling.mp3"
    lao "({i}As my groggy mind starts to wake, the first thing I hear is the sound of bacon sizzling.{/i})"
    
    play audio "cup_stirring.mp3"
    lao "({i}The delicious smell of fresh bacon and coffee drift into my nostrils, waking me up almost instantly.{/i})"

    play music "morning_song.mp3"
    scene bedroom with fade
    show lao tired_mopen at center with dissolve
    
    play sound "man_yawning.mp3"
    lao "({i}I let out a quiet yawn as I stretch out in bed.{/i})"

    show lao exhausted_mclosed at center

    lao "({i}I force my eyes open, trying my best to ignore the harsh sunlight beaming down on my face.{/i})"
    lao "({i}It's a bit difficult to get out of bed in the morning, but the promise of a good breakfast is my motivator for today.{/i})"

    scene kitchen with fade
    show lao exhausted_mclosed at left with moveinleft
    show gosfrid neutral_mclosed at right with moveinright

    lao "({i}As I suspected, my roommate and best friend Gosfrid is making breakfast for us this morning.{/i})"

    menu breakfastThoughts:
        "Thank you.":
            show lao exhausted_mopen at left
            lao "It smells good. Thank you for the breakfast."
            show lao exhausted_mclosed at left

            show gosfrid smile_mopen at right
            gosfrid "You can thank me after you verify it's edible."
            show gosfrid smile_mclosed at right

            show lao exhausted_mopen at left
            lao "Even if it's not, I appreciate it."
            show lao exhausted_mclosed at left

        "Bacon again?":
            show lao exhausted_mopen at left
            lao "Bacon again?"
            show lao exhausted_mclosed at left

            show gosfrid annoyed_mopen at right
            gosfrid "Oh, I see. I didn't realize I had to ask what you wanted before preparing a thoughtful surprise 
            breakfast for us on your first day."
            show gosfrid annoyed_mclosed at right
            $ annoyance += 1

            lao "({i}I was trying to be silly but I guess that didn't land very well.{/i})"
    
    lao "({i}I sit down at the counter and watch as Gosfrid plates the food for us.{/i})"
    lao "({i}He grabs our mugs out of the cabinet and pours the coffee he made into each.{/i})"
    lao "({i}He gingerly prepares each cup according to our indiviudal preferences, ensuring he adds just the right amount of milk and sugar.{/i})"
    lao "({i}Once done, he gently slides my favorite Ghostbusters mug next to my plate.{/i})"
    lao "({i}Desperate for caffeine to wake me up, I immediately take a big gulp.{/i})"

    menu coffeeThoughts:
        "It's too sweet.":
            show lao exhausted_mopen at left
            lao "Oh jeez. I think this might be too sweet for me."
            show lao exhausted_mclosed at left

            show gosfrid annoyed_mclosed at right
            lao "({i}Gosfrid's brow visibly creases in annoyance. Before he even opens his mouth, I regret speaking.{/i})"

            show gosfrid annoyed_mopen at right
            if annoyance == 1:
                gosfrid "What's your problem this morning? Just say thank you for once."
                gosfrid "Ugh, anyway..."
                $ annoyance += 1
            else:
                gosfrid "Okay, then you can make it yourself next time. I can't make it perfectly every time, yeah?"
                gosfrid "Anyway..."
                $ annoyance += 1

        "It's too bitter.":
            show lao exhausted_mopen at left
            lao "Oh jeez. I think this might be too bitter for me."
            show lao exhausted_mclosed at left

            show gosfrid annoyed_mclosed at right
            lao "({i}Gosfrid's brow visibly creases in annoyance. Before he even opens his mouth, I regret speaking.{/i})"

            show gosfrid annoyed_mopen at right
            if annoyance == 1:
                gosfrid "What's your problem this morning? Just say thank you for once."
                gosfrid "Ugh, anyway..."
                $ annoyance += 1
            else:
                gosfrid "Okay, then you can make it yourself next time. I can't make it perfectly every time, yeah?"
                gosfrid "Anyway..."
                $ annoyance += 1

        "It's perfect.":
            show lao exhausted_mopen at left
            lao "Ahh, thank you. This is just what I needed to wake me up."
            show lao exhausted_mclosed at left

            show gosfrid smile_mopen at right
            gosfrid "Yeah? Trust me, I feel the same way."
            show gosfrid annoyed_mopen at right
            gosfrid "Not excited for the coffee jitters later, though."
            show gosfrid neutral_mclosed at right

            show lao tired_mopen at left
            lao "Ugh, yeah, me neither. Especially with the Vyvanse."
            show lao tired_mclosed at left

            show gosfrid neutral_mopen at right
            gosfrid "Right, that does make it worse... Sorry."
            show gosfrid neutral_mclosed at right

            show lao exhausted_mopen at left
            lao "No, it's alright. I wouldn't be able to focus today without it. I think it's a fair trade-off."
            show lao exhausted_mclosed at left

            show gosfrid neutral_mopen at right
            gosfrid "Speaking of today..."

    show gosfrid neutral_mopen
    gosfrid "How are you feeling about today? You know that if you need anything I'll be right next door, yeah?"
    show gosfrid neutral_mclosed at right

    menu dayThoughts:
        "I don't need your help.":
            show lao exhausted_mopen at left
            lao "I think I can manage on my own. I'm not sure how much you'd be able to help considering you're 
            a detective and not a psychologist."
            show lao exhausted_mclosed at left

            show gosfrid annoyed_mopen at right
            if annoyance <= 1:
                gosfrid "I'm not saying I can help with the more technical stuff, I'm just saying I'm
                there for emotional support or if you want to talk or want to get lunch or something."
            
            $ annoyance += 1

        "I'm anxious.":
            show lao exhausted_mopen at left
            lao "Honestly, I'm anxious. I'm not fully confident in my ability to be a good therapist. 
            What if I say the wrong thing?"
            show lao exhausted_mclosed at left

            lao "({i}Gosfrid puts his gloved hand over mine.{/i})"

            show gosfrid neutral_mopen at right
            gosfrid "You know it's impossible to say the right thing all the time, love. The best thing you can do is
            be sincere and try your best. I know you'll do great."
            show gosfrid neutral_mclosed at right

            show lao tired_mopen at left
            lao "(Sigh.) I know logically that it's impossible to be a perfect therapist on the first day."
            show lao exhausted_mopen at left
            lao "I just can't help but worry I'll be another bad therapist someone complains to their friends and
            other therapists about."
            show lao exhausted_mclosed at left

            show gosfrid neutral_mopen at right
            gosfrid "I know, love. I feel pretty much the exact same about today."

    if annoyance <= 1:
        gosfrid "If you'd like, we can both practice a bit before we open for the day."
        show gosfrid neutral_mclosed at right

        show lao exhausted_mopen at left
        lao "That sounds nice. I could use a bit of a warm-up."
        lao "I finished breakfast, so I'll go get ready for us to head out. Thanks again for the breakfast,
        it was edible and very good."
        show lao exhausted_mclosed at left

        show gosfrid smile_mopen at right
        gosfrid "You're welcome. I'll wait for you here and get this cleaned up."
        show gosfrid smile_mclosed at right

        hide lao exhausted_mclosed with easeoutleft  

        scene black with dissolve
        "Good Ending: Gosfrid isn't upset with you."
        return
    elif annoyance == 2:
        show gosfrid annoyed_mopen at right
        gosfrid "Look, I'm a little upset with you. I'm going to go because I need space,
        but let's talk about it later."
        hide gosfrid neutral_mclosed with easeoutright  

        play sound "door_shutting.mp3"
        lao "({i}Before I even have a chance to say anything, Gosfrid goes to his room and closes the door.{/i})"
        lao "({i}Although I'm left wondering about what I did to upset him, I have no choice but to go get ready
        and give him the space he needs.{/i})"
        lao "({i}I'm upset too, of course, but I can't force him to talk to me about it if he doesn't want to right now.{/i})"

        scene black with dissolve
        "Neutral Ending: Gosfrid is upset with you, but you don't talk about it."
        return
    elif annoyance == 3:
        show gosfrid annoyed_mopen at right
        gosfrid "Seriously, what's wrong with you today? Are you taking your anxiety out on me?"
        show gosfrid annoyed_mclosed at right

        show lao exhausted_mopen at left
        lao "I'm sorry. You're right, I'm anxious and I'm also tired. I'm not trying to be a pain,
        really."
        show lao exhausted_mclosed at left
        
        show gosfrid annoyed_mopen at right
        gosfrid "Well, you're being one and it's upsetting me. I've been trying to support you all morning
        and you've been pushing me away and insulting me. It really hurts when you do that, Lao."
        gosfrid "You know what? I'm just going to leave. I don't want to have this conversation with you right now.
        I might say something I regret."
        hide gosfrid neutral_mclosed with easeoutright 

        play sound "door_slam.mp3"
        lao "({i}Before I even have a chance to say anything, Gosfrid goes to his room and shuts the door with moderate force.{/i})"
        lao "({i}Although I'm left holding back a slew of apologies, I have no choice but to go get ready
        and give him the space he needs.{/i})"
        lao "({i}I'm upset too, of course, but I can't force him to talk to me about it if he doesn't want to right now.{/i})"

        scene black with dissolve
        "Bad Ending: Gosfrid is really upset with you."
        return


###### THERAPY TUTORIAL SECTION ######
label tutorial:
    call screen therapy