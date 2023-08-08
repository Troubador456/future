import random
condition = input("Welcome to the world of Crylon, a medieval land with many mysteries to explore. Do you dare to explore them all?: ")
condition = condition.lower()
if condition == "yes" or condition == "yeah":
    player_name = input("What is your name? ")
    print("Welcome,", player_name ," to the land of Crylon. Make sure to read the choices that are in parantheses. Write the choices excactly as shown. Thank you and enjoy the game.")
    print("Father: 'Why are you still in bed? The crops aren't going to harvest themselves'")
    print("You:...")
    print("Father:'now get a move on then'")
    print("*walks outside*")
    farmin_explorin = input("Do (farming) or ignore your father and go (exploring): ")
    farmin_explorin = farmin_explorin.lower()
    if farmin_explorin == "exploring":
        print("*runs away*")
        hope_live = input("Oh no, you ran out of food and the next village in a few tens of miles What do you do? (Hope you make it there) (live off the wild): ")
        hope_live = hope_live.lower()
        if hope_live == "hope you make it there":
            print("You faint as you try walking in the burning sun")
            print("As you awake you see a mysterious merchant looking at you")
            print("Merchant: My name is Rubron, a local merchant and who may you be?")
            print("You:...")
            look_bye = input(f"'Ah, {player_name}, welcome to my humble abode. You may leave anytime you want.' What do you do? (Look around and stay) (Say bye and leave): ")
            look_bye = look_bye.lower()
            if look_bye == "look around and stay":
                print("You chat with him and eventually he sees your potential and he offers you a job as an assistant")
                confron_job = input("You sense something off about his behavior immediatly. What do you do? (Confront him) (Take the job): ")
                confront_job = confron_job.lower()
                if confront_job == "take the job":
                    print("You live a wealthy life and have kids but the merchant reveals his true identity and kills you. (0 mysteries found)")
                if confront_job == "confront him":
                    r_f = input("He feels offended and pulls out a knife on you. What do you do? (Retreat) (Fight him): ")
                    r_f = r_f.lower()
                    if r_f == "fight him":
                        print("He strikes you with a blade and you bleed to death as you see him turn into a huge serpent (0 mysteries found)") 
                    if r_f == "retreat":
                       print("He chases you with a knife")
                       print("He shows his true form as a serpent (mystery found)")
                       print("He challenges you to a duel")
                       result = random.randint(0,2)
                       results = ["win", "lose", "draw" ]
                       print("The result is: ", results[result])
                       if results[result] == "win":
                           print("Good job")
                       elif results[result] == "lose":
                           print("Too bad")
                       else:
                           print("Merchant:Hmm, I will spare you now, leave")
                           print("You go back home and live the rest of your life. (1 mystery found)")
            if look_bye == "say bye and leave":
                print("You leave his abode and see that the town is taken under siege (mystery found)")
                yes_no = input("Recruitsman: (Hey, kid would you like to join the force to rebel against the people who are sieging the town.) What do you do? (Yes) (No): ")
                yes_no = yes_no.lower()
                if yes_no == "no":
                    print(" Recruitsman: Wasn't a choice.")
                    print("You die(1 mystery found)")
                if yes_no == "yes":
                    print("Recruitsman: Follow me soldier")
                    print("A few minutes later, Recruitsman: Take a sword and shield. Take the armor and be ready in 5 minutes.")
                    print("The commander walks in as you leave the dressing room, Commander: Troops, I am your commander and we are going into battle")
                    print("Commander:", player_name, ", you are selected as a soldier going to the center to distract the forces.")
                    print("As you walk outside, you see the commander of the siegers... Your FATHER! (mystery found)")
                    print("You charge as the commanders start the battle.")
                    print("Your father sees your face and scolds you. He calls you up to do a 5v5.")
                    results2 = ["win","loss","draw"]
                    result2 = random.randint(0,2)
                    print("The result of the 5v5 battle was a: ", results2[result2])
                    if results2[result2] == "win":
                        ("Good job!")
                    elif results2[result2] == "loss":
                        ("Too bad")
                    else:
                        go_fight = input("Father: Oh a draw, well I will let you surrender and we go back to our house. (Yes) (No): ")
                        go_fight = go_fight.lower()
                        if go_fight == "no":
                            print("You get pulled by the ear back home on a horse. Father: Next time you run away dont leave your plans in the open.")
                        if go_fight == "yes":
                            print("As he reaches his arm out, you stab him in the heart. Father: How could you? As the enemies heard the news, they retreated.")
                            print("You are the hero of the town, but at what cost?(2 mysteries found)")
        if hope_live == "live off the wild":
            fight_run = input("You find some berries and stay alive enough, while looking for more berries you see a venomous snake. What do you do? (Fight it) (Run into a mysterious cave): ")
            fight_run = fight_run.lower()
            if fight_run == "fight it":
                print("It bites you bad and you die. (0 mysteries found)")
            if fight_run == "run into a mysterious cave":
                print("As you walk in you find a treasure chest (mystery found)")
                treasure = random.randint(0,3)
                in_treasure_chest = ["gold", "silver", "copper", "monster"]
                print("You found", in_treasure_chest[treasure])
                if in_treasure_chest[treasure] == "monster":
                    print("The moster bit you and you died")
                else:
                    print("Good Job!")
                      
    if farmin_explorin == "farming":
        print("You do the same routine and die farming (mysteries found: 0)")
    print("Well, this the end of your story. Farewell,", player_name, ".")

else:
    print("see ya later")
    exit()            
       