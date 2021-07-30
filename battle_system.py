from random import randint


def calc_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


def game_ends(winner_name):
    print(winner_name + " won!")


def main():
    game_running = True
    game_results = []

    while game_running:
        counter = 0
        new_round = True
        player = {"name": "Player", "attack": 13, "heal": 16, "health": 100}
        monster = {"name": "Enemy", "attack_min": 12, "attack_max": 17, "health": 80}

        print("---" * 7)
        player["name"] = input("Enter your name : ")
        
        if player["name"] == "":
            player["name"] = "Player"
        
        print("Welcome, " + player["name"] + "\n")

        while new_round:
            counter += 1
            player_won = False
            monster_won = False

            print("---" * 7)
            print("Please an select action: ")
            print("1. Attack ")
            print("2. Heal ")
            print("3. Exit Game")

            player_choice = input(" >>> ")
            print("---" * 7)

            if player_choice == "1":
                monster["health"] -= player["attack"]
                if monster["health"] <= 0:
                    monster["health"] = 0
                    player_won = True

                else:
                    player["health"] -= calc_monster_attack(monster["attack_min"], monster["attack_max"])
                    if player["health"] <= 0:
                        player["health"] = 0
                        monster_won = True

                print(f"\nAttacking {monster['name']}!")
                print(f"{monster['name']} now has {monster['health']} health left")
                print(f"Attacking {player['name']}!")
                print(f"{player['name']} now has {player['health']} health left\n")

            elif player_choice == "2":
                player["health"] += player["heal"]
                print(f"Healing {player['name']}!")
                print(f"{player['name']} now has {player['health']} health")

            elif player_choice == "3":
                print("Ending game...")
                game_running = False
                new_round = False

            else:
                print("Invalid Input. Please choose from the options above!")

            if player_won and monster_won:
                print(player["name"] + " has " + player["health"] + " left")
                print(monster["name"] + " has " + monster["health"] + " left")

            elif player_won:
                game_ends(player["name"])
                round_result = print("Name :", player["name"] + "\n" +
                      "Health :", str(player["health"]) + "\n" +
                      "Rounds :", counter)
                game_results.append(round_result)
                print("The round has now ended...")
                new_round = False

            elif monster_won:
                game_ends(monster["name"])
                round_result = print("Name :", player["name"] + "\n" +
                      "Health :", str(player["health"]) + "\n" +
                      "Rounds :", counter)
                game_results.append(round_result)
                print("The round has now ended...")
                new_round = False

main()