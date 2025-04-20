def chatbot():
    print("Hi there! I'm your friendly chatbot.")
    name = input("What's your name? ")

    keep_chatting = True

    while keep_chatting:
        mood = input(f"How are you feeling today, {name}? (good/bad/neutral): ").lower()

        if mood == "good":
            print("That's awesome to hear!")
            hobby = input("What’s one of your favorite hobbies? ")
            print(f"Nice! I wish I could try {hobby} too.")
        elif mood == "bad":
            print("Oh no, I’m really sorry to hear that.")
            activity = input("What’s something you enjoy that might cheer you up? ")
            print(f"{activity} sounds like a great idea. I hope it helps!")
        elif mood == "neutral":
            print("Gotcha. Just one of those days, huh?")
            day = input("What’s your day been like so far? ")
            print(f"Thanks for sharing. Hope the rest of the day goes well!")

        again = input("Would you like to keep chatting? (yes/no): ").lower()
        if again != "yes":
            keep_chatting = False
            print(f"Alright, {name}. It was really nice chatting with you. Have a great day!")

chatbot()
