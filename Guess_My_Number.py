def guessmynumber():
    import random
    import webbrowser
    yes = ("yes", "Yes", "YES", "Yeah", "yeah", "okay", "Okay")
    no = ("no", "No", "No", "nope", "nah", "Nah", "Nope")
    n1 = random.randint(0,1000)
    n2 = random.randint(0,1000)
    n3 = random.randint(0,1000)
    x = random.randint(1,20)
    guessset = sorted([n1, n2, n3])
    #print(guessset)
    n = guessset[1]
    #print(n)
    print("You have " + str(x) + " guesses, to guess my number between "
          + str(guessset[0]) + " and " + str(guessset[2]) + "\n")
    while x != 0:
        guess = int(input("Guess my number \n"))
        guessset.append(guess)
        guessset = sorted(guessset)
        x = x - 1
        if guess == n:
            print("Correct! Well Done! You are GENIUS! Here is Otter to congratulate you!")
            webbrowser.open("https://media.giphy.com/media/NSY5PMSdamewjHkt14/giphy.gif")
            break
        else:
            if x != 0:
                if guess < n:
                    print("Bigger, try again!")
                elif guess > n:
                    print("Smaller, try again")
                else:
                    print("Try a NUMBER!")
                print("You have " + str(x) + " more guesses")
                print("\n")
            else:
                print("Bad luck!")
                print("The answer was " + str(n))
                tryagain = input("Do you to try again? Yes or no? \n")
                if tryagain in yes:
                    guessmynumber()
                elif tryagain in no:
                    print("Fair enough \n")
                else:
                    print("Goodbye person who didn't answer yes or no \n")
            if x <= 5:
                if random.randint(0,1) == 0:
                    hint = input("Do you want a hint? Yes or no? \n")
                    if hint in yes:
                        print("The answer is between "
                              + str(guessset[(guessset.index(n)) - 1]) + " and " +
                              str(guessset[(guessset.index(n)) + 1]) + "\n")
                    elif hint in no:
                        print("Fair enough \n")
                    else:
                        print("Answer yes or no next time \n")

guessmynumber()