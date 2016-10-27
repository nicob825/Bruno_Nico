print("You are in the woods, you don't know how you got there. You see a sword on the ground and a spell tome.")
choice = input("What do you pick up, the sword or the spell tome?")

if choice == "sword":
    print("You have picked up the sword! It is even balanced and you can feel rage course through you. You put it back in the scabard and your rage feels bottled up.")
    print("You stumble across a bandit camp! ")
    choice = input("You can either sneak and take supplies you need or deliver punishment. Sneak or kill:")
    if choice == "kill":
        print("You kill the rest of them. You now notice the bandit leader who is twice as burly as you.")
        choice = input("Do you try: reason or slay")
        if choice=="slay":
            print("As you point your sword to him he understands the threat. He pulls out a massive axe and charges you. You cleave him in half cleanly and you are victorious.")
        else:
            print("As you walk up to the man, he seems to twitch when you come to close. As you jump back, an axe misses your head only by centimeters. He charges you and you dodge the first attack and he lands a blow on you and you die.")
    else:
        print("As you sneak into the camp, you see some scouts. They approach you, but dont see you yet.")
        choice=input("Do you kill or or wait.")
        if choice=="wait":
            print("You wait there, watching the scouts. They don't notice you. You sneak in and take what you need a leave.")
        else:
            print("As you slay the scouts, another one pops out of no where and calls the bandits. They swarm you and you are shot with an arrow to the chest. You die.")
else:
    print("You picked up the spell tome and you feel the power within you awaken. You now feel complete, as if the spell tome was the other half of you soul.")
    print("You stumble accros a bandit camp!")
    choice=input("Do you sneak or kill?")
    if choice=="kill":
        print("You use your spell tome to launch lightning from your fingers! You slaughter them all and then you see the bandit leader!")
        choice=input("Do you: reason or kill")
        if choice=="reason":
            print("As you try to reason with him, he gets angrier and angrier. You use your spell tome to calm him and then he leaves.")
        else:
            print("You look for a spell to kill the bandit leader the most horrif way. As you look through it he charges you. You cast some random spell which makes the bandit leader an elephant. He tramples you.")
    else:
        print("You get close to the camp and see some scouts.")
        choice=input("Do you: wait or kill")
        if choice=="wait":
            print("You wait there, patiently. One gets to close and you cast a spell that makes you invisible and the bandit passes by you, by a few inches. While you are invisible you take what you need and leave.")
        else:
            print("You kill all the scouts with a fireball. The explosion brings even more bandits and your soon surronded. You cast an invicible shield spell but because you were weaken from casting spells it isn't strong enough and you die.")
