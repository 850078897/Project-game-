
def game():
    print("I wake up in a dim light...")
    print("Remember before you went to hospital, you fainted from overwork, and now...No one has.")
    print("You slowly get up and change your clothes and get out of the rest room.")
    print("Seems to hear a bit of human breathing?")
    print("    1. Chasing after")
    print("    2. Leave right away, down the stairs")
    newbee1 = int(input("What is your choice? "))
    if newbee1 ==1:
        game2()
    if newbee1 ==2:
        game100()
    
def game2():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("You find your voice in the corridor. Then you walk past.")
    print("You ran to the building and found a little boy in the corner, a thirteen-year-old boy, who saw you and suddenly raised an old handgun and buckled the board...")
    print("Bang!")
    print("Your left arm was bruised, though you were flashing.")
    print("You're angry, you're not easy to recover, and you're hurt again.Facing the boy, you're ready to...")
    print("    1. Show kindenss to the boy, but keep a certain distance.")
    print("    2. He has a gun, and you don't have anything, go downstairs!")
    newbee2 = int(input("What is your choice? "))
    if newbee2 == 1:
        game3()
    elif newbee2 ==2:
        game9()
def game3():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("The boy's answer makes you very different: originally you are human, I still think be a zombie...Uh, your wound, Im sorry. ")
    print("The wound doesn't care about you kids, you just said...Zombies?!You asked in surprise.")
    print("Well, you don't know yet?Yesterday, the city was infected by a word called 'brainless virus'. The infected human brain tissue will be destroyed and will continue to kill people...That is, zombies.The boy said.")
    print("'Er, er!Your eyes are wide.")
    print("I call it the LuBenWei. What's your name? Lets meet each other first.Said the boy.")
    print("Oh, my name is...(let's just call MaDiuRen, first you don't mind oh, a game ^ O ^) you said.")
    print("The MaDiuRen?What a strange name.Muttered the LuBenWei.")
    print("Suddenly, under the building, there was a terrible roar!")
    print("    1. It could be the zombie, just go down and fight him!")
    print("    2. Go back to the corridor, find the fire axe, and find a convenient and hidden room.")
    newbee3 = int(input("What is your choice? "))
    if newbee3 == 1:
        print("One is ok.. But... It's a hugh amount... Game over!!!")
    if newbee3 ==2:
        game4()
def game4():
    print("You found a fire ax, took out a dead zombie, and found a room to hide in.")
    print("Turn on the light!")
    print("You complain.")
    print("No, it will attract other zombies!")
    print("Replied the Lubenwei.")
    print("What a place!")
    print("Hey, there's a bed...")
    print("Oops, how did you hit the wall?")
    print("Pain T x T you covering her head said.")
    print("How did you shut the door?")
    print("Through asking.")
    print("No...")
    print("Hey, how's the door closed?")
    print("Suddenly you think of something, turn around and run toward the door: repair Lubenwei, the repair of you!")
    print("You fumble, you turn on the light...")
    print("A bed, a cupboard, a person...")
    print("Lubenwei!")
    print("Why didnt you answer? I was scared to death.")
    print("You are walking toward LuBenWei.")
    print("The face was pale, and it looked fainter.")
    print("Whats going on...You hold your head and your mind is confused, and suddenly you hear the Lubenwei saying, dont mind me, go, go, I have a heart attack, and there are zombies under the bed...Take this pistol...")
    print("    1.Pick up his pistol and run, even if he's still useful to you.")
    print("    2.Protect him with his pistol, even if the gunshot would attract a large group of zombies.")
    newbee100 = int(input("What is your choice "))
    if newbee100 == 1:
        newbee5()
    elif newbee100 ==2:
        newbee8()
def newbee5():
    print("You run away")
    print("You see a zombie")
    print("    1.Sneak")
    print("    2.Shoot his head")
    newbeewudi = int(input("What is your choice? "))
    if newbeewudi ==1:
        newbee6()
    elif newbeewudi ==2:
        newbee7()
        
def newbee6():
    print("You won")
def newbee7():
    print("After you kill him, other zombies already surrounded you... Game over!!!")
def newbee8():
    print("You kill a few zombies, then you don't have any more bullet, you are dead... Game over!!!")
def game9():
    print("You go down the stairs, suddenly found a group of faces of the ferocious 'people' -- the zombie...")
    print("And then, game over.")
def game100():
    print("You go down the stairs, suddenly found a group of faces of the ferocious 'people' -- the zombie...")
    print("And then, Game over!!!")
    print("DO U WANA TRY AGAIN?")
    print("YES = 1, NO = 2")
    sb = int(input("1 or 2? "))
    if sb == "1":
        game()
    elif sb =="2":
        print("bye")
        
        

game()

    