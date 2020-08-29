import time
import random


print('##################################')
print('#   Little Red Riding Hood RPG   #')
print('##################################')
print('                                  ')


def print_pause(message):
    print(message)
    time.sleep(2.0)

# A discription of what is happening is presented to the player


def intro(item, option):
    print_pause("You are walking in the woods on your way to visit"
                " your sick Grandma, with a basket of goodies.\n")
    print_pause("It's getting late in the evening. ")
    print_pause("You're aware of the dangers of a 'Big Bad Wolf' "
                "lurking somewhere in the woods.\n")
    print_pause("Your goal is to safely reach your Grandma's home "
                "in the woods.\n")
    print_pause("On route you reach a bridge over a stream, where you")
    print_pause("come across a " + option + ".\n")
    print_pause("You are obliged to offer something to cross.\n")
    print_pause("You reach inside your basket and offer:\n")


def chorizo(item, option):
    if "meat" in item:
        print_pause("\nThe " + option + " smells the candy, "
                    "grins and snatches it off your hand.")
        print_pause("\nHe chomps away at the chorizo.")
        print_pause("\nWhilst he's attention is on eating the chorizo,"
                    " you must choose wisely what to do next.\n")
    else:
        item.append("candy")
    bank(item, option)


def candy(item, option):
    print_pause("\nThe candy makes him SNARL!")
    print_pause("\nYou are about to pass "
                "when the " + option + " comes towards you.")
    print_pause("\nShriek! You can see the " + option + "'s fangs!")
    print_pause("You become aware that this is actually not a " + option + " "
                "but the 'Big Bad Wolf'.\n")
    if "meat" not in item:
        print_pause("You realise that candy only enfuriated the "
                    "'Big Bad Wolf' and will not fill his hunger. "
                    "You must make a quick decision, "
                    "or be next on the menu. Gulp!\n")
    while True:
        choice2 = input("Would you like to (1) Run for it (2) "
                        "Jump into the stream? ")
        if choice2 == "1":
                print_pause("\nYou try to run past him but...")
                print_pause("The " + option + " realises and lunges at you.")
                print_pause("\nEek! You have been gobbled up!\n")
                print_pause("Too bad.You are defeated.\n")
                play_again()
                break
        if choice2 == "2":
            print_pause("\nYou dash for the stream and jump in. "
                        "\nLuckily, you're a fast swimmer, "
                        "and the " + option + " is afraid of water. "
                        "He can't swim either.\n")
            print_pause("You reach the other side of the stream.\n")
            print_pause("The " + option + " runs across in pursuit."
                        " By the time he gets there he is tired "
                        "but still won't let you pass.\n")
        stream(item, option)


def more(item, option):
        print_pause("\nThe " + option + " smells the chorizo, "
                    "he grins and snatches it off your hand.")
        print_pause("\nHe chomps away at the chorizo.")
        print_pause("\nThe " + option + " eats and eats until he becomes "
                    "so full, that he cannot eat anymore... "
                    "So he lies down and falls fast asleep zzZZ.")
        print_pause("\nYou seeze this moment and sneek past.")
        print_pause("\nOnce in the clear, you run for your life to safety.")
        print_pause("\nYou reach your beloved Grandma's home "
                    "and fly into her open arms.")
        print_pause("\nYipee! Victory is yours.\n")


def run(item, option):
        print_pause("\nYou try to run away but...")
        print_pause("The " + option + " is too fast for you "
                    "and catches up in no time at all. "
                    "He chows down onto you...")
        print_pause("\nEek! You have been gobbled up!\n")
        print_pause("Too bad. You are defeated.\n")


def sneek(item, option):
        print_pause("\nYou try to sneek past him but...")
        print_pause("The " + option + " realises and lunges at you.")
        print_pause("\nEek! You have been gobbled up!\n")
        print_pause("Too bad.You are defeated.\n")


def bridge(item, option):
    print_pause("Enter 1 to offer candy.")
    print_pause("Enter 2 to offer chorizo.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            candy(item, option)
            break
        elif choice1 == "2":
            chorizo(item, option)
            break


def stream(item, option):
    print_pause("Enter 1 to offer chorizo.")
    print_pause("Enter 2 to run away.")
    print_pause("What would you like to do?")
    while True:
        choice3 = input("(Please enter 1 or 2.)\n")
        if choice3 == "1":
            chorizo(item, option)
            break
        elif choice3 == "2":
            run(item, option)
            break


def bank(item, option):
    print_pause("Enter 1 to offer more chorizo.")
    print_pause("Enter 2 to sneek past.")
    print_pause("What would you like to do?")
    while True:
        choice3 = input("(Please enter 1 or 2.)\n")
        if choice3 == "1":
            more(item, option)
            break
        elif choice3 == "2":
            sneek(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = ["meat", "more", ]
    option = random.choice(["crossing guard", "sheep",
                            "feeble man", ])
    intro(item, option)
    bridge(item, option)
    stream(item, option)
    bank(item, option)

play_game()
