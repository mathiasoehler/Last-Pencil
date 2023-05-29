import random
import string
name1 = "John"
name2 = "Jack"
first_template = string.Template("Who will be the first ($first, $second):\n")
chosen = string.Template("Choose between $first and $second")

while True:
    try:
        pencil = int(input("How many pencils would you like to use:\n"))
        if pencil < 0:  # or negativ. o: The number of pencils should be numeric
            print("The number of pencils should be numeric")

        elif pencil == 0:  # check if input 0. o: The number of pencils should be positive
            print("The number of pencils should be positive")
        else:
            break
    except ValueError: # check if input numeric
        print("The number of pencils should be numeric")

while True:
    chosen_player = str(input(first_template.substitute(first=name1, second=name2)))
    if chosen_player == name1 or chosen_player == name2:
        break
    else:
        print(chosen.substitute(first=name1, second=name2))
# Check if the player Name 1 or Name 2. o: Choose between *Name1* and *Name2*


while pencil > 0:
    print(pencil * "|")
    print(chosen_player, "'s turn:")

    if chosen_player == name1:
        while True:
            try:
                player_pencil = int(input())
                if player_pencil <= 0 or player_pencil > 3:  # max taken pencil 3. o:  Possible values: '1', '2' or '3'
                    print("Possible values: '1', '2', '3'")
                elif player_pencil > pencil:  # the player takes more pencil than are on the table o: many pels were taken
                    print("Too many pencils were taken")
                else:
                    pencil -= player_pencil
                    break
            except ValueError:
                print("Possible values: '1', '2', '3'")

    else:
        if pencil == 1:  # only on pencil left, bot loses
            player_pencil = 1
            pencil -= player_pencil
            print(player_pencil)
        elif (pencil - 1) % 4 == 0:
            player_pencil = random.randint(1, 3)
            pencil -= player_pencil
            print(player_pencil)
        else:
            player_pencil = (pencil - 1) % 4
            pencil -= player_pencil
            print(player_pencil)

    chosen_player = name1 if chosen_player == name2 else name2
    if pencil == 0:
        print(f"{chosen_player} won!")
        break
