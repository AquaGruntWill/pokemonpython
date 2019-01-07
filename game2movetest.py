"""and we're back 6 months later lol"""



from pokemon2 import urPoke
import random
from random import randint
import sys
from moves import pokeMove

pokemon = [
    urPoke("Metagross", "Steel", "Psychic", 270, 247, 238, 175, 166, 900, 8, 2),
    urPoke("Dragonite", "Dragon", "Flying", 292, 245, 175, 184, 184, 148, 15, 14),
    urPoke("Hydreigon", "Dragon", "Dark", 294, 193, 166, 229, 166, 180, 3, 9),
    urPoke("Genesect", "Bug", "Steel", 252, 220, 175, 220, 175, 182, 10, 5),
    urPoke("Goodra", "Dragon", "NA", 190, 184, 130, 202, 274, 148, 3, 5),
    urPoke("Heatran", "Fire", "Steel", 292, 166, 195, 238, 195, 143, 16, 11),
    urPoke("Salamance", "Dragon", "Flying",  300, 247, 148, 202, 148, 184, 3, 5),
    urPoke("Necrozma", "Psychic", "NA", 304, 197, 186, 233, 164, 146, 8, 11),
    urPoke("Tyranitar", "Rock", "Dark", 310, 245, 202, 175, 184, 114, 11, 3),
    urPoke("Garchomp", "Dragon", "Ground", 326, 238, 175, 148, 157, 188, 15, 13),
    urPoke("Kommo-o", "Dragon", "Fighting", 260, 202, 229, 184, 193, 157, 15, 12),
    urPoke("Volcanion", "Fire", "Water", 270, 202, 220, 238, 306, 262, 2, 7),
    urPoke("Heracross", "Bug", "Fighting", 270, 229, 139, 76, 295, 157, 10, 12),

            ]

moves = [
    pokeMove('Hyper Fang', "Normal", 0, 80, 100),
    pokeMove('Fire Punch', "Fire", 1, 80, 100),
    pokeMove('Meteor Mash', "Steel", 0, 90, 100),
    pokeMove('Dragon Claw', "Dragon", 0, 80, 100),
    pokeMove('Shadow Ball', "Ghost", 1, 80, 100),
    pokeMove('Slam', "Normal", 0, 80, 100),
    pokeMove('Drill Peck', "Flying", 0, 80, 100),
    pokeMove('Waterfall', "Water", 0, 80, 100),
    pokeMove('Extrasensory', "Psychic", 1, 80, 100),
    pokeMove('Dark Pulse', "Dark", 1, 80, 100),
    pokeMove('X-Scissor', "Bug", 0, 80, 100),
    pokeMove('Power Gem', "Rock", 1, 80, 100),
    pokeMove('Sky Uppercut', "Fighting", 0, 80, 100),
    pokeMove('Drill Run', "Ground", 0, 80, 100),
    pokeMove('Air Slash', "Flying", 0, 80, 100),
    pokeMove('Dragon Pulse', "Dragon", 0, 80, 100),
    pokeMove('Flash Canon', "Steel", 0, 80, 100),



]
random.shuffle(pokemon)
poke1 = pokemon.pop()
poke2 = pokemon.pop()
poke3 = pokemon.pop()
poke4 = pokemon.pop()
poke5 = pokemon.pop()
poke6 = pokemon.pop()

pokemonusing = 0

playerpoke = [

poke1,
poke2,
poke3,
poke4,
poke5,
poke6,

]
enemiesleft = 6

def win():
    print("\033c")
    print("~~~VICTORY~~~")
    quit()

class Game:
    score = 0
    print("Go! {}!".format(playerpoke[pokemonusing].name) + "\n")

    while enemiesleft > 0:
        enemypoke = pokemon.pop()

        print("{} appears! \n".format(enemypoke.name))
        while enemypoke.isAlive():

            print("HEALTH: {}".format(playerpoke[pokemonusing].health))
            print("What will {} do?".format(playerpoke[pokemonusing].name))
            command = input("FIGHT | ITEM | POKEMON | RUN \n").lower()
            if command == "fight":

                """INPUT MOVE CHOICE"""
                print("\n")
                usingmove = input("{} (1) | {} (2)\n".format(moves[playerpoke[pokemonusing].move1].name, moves[playerpoke[pokemonusing].move2].name))

                """PLAYER GOES FIRST"""
                if playerpoke[pokemonusing].spd > enemypoke.spd:

                    """MOVE 1"""
                    if usingmove == "1":
                        print("\033c")
                        print("{} uses {}!".format(playerpoke[pokemonusing].name, moves[playerpoke[pokemonusing].move1].name))

                        """CRIT CHECK"""
                        critchance = randint(1, 24)
                        if critchance == 24:
                            crit = 1.5
                            print("CRITICAL HIT!")
                        else:
                            crit = 1

                        """RANDOM MODIFIER"""
                        rand = random.randrange(85, 100) / 100

                        """PHYS/SPECIAL CHECK"""
                        if moves[playerpoke[pokemonusing].move1].phys == 0:
                            damage = (((42 * moves[playerpoke[pokemonusing].move1].power * playerpoke[pokemonusing].atk / enemypoke.defence) / 50) + 2) * (crit * rand)
                        elif moves[playerpoke[pokemonusing].move1].phys == 1:
                            damage = (((42 * moves[playerpoke[pokemonusing].move1].power * playerpoke[pokemonusing].spatk / enemypoke.spdef) / 50) + 2) * (crit * rand)
                        damage = int(round(damage))
                        """(((((Level x 2)/5 + 2) x Move Power x Attack / Defence) / 50) + 2) x (Crit x Random x STAB x Type)"""

                        """DEAL DAMAGE"""
                        enemypoke.health -= damage
                        print("{} takes {} damage!".format(enemypoke.name, damage))

                        """ENEMY TURN"""
                        if enemypoke.isAlive():
                            enemymove = random.randrange(0, 2)
                            if enemymove == 0:
                                print("{} uses {}!".format(enemypoke.name, moves[enemypoke.move1].name))
                                critchance = randint(1, 24)
                                if critchance == 24:
                                    crit = 1.5
                                    print("CRITICAL HIT!")
                                else:
                                    crit = 1
                                rand = random.randrange(85, 100) / 100
                                if moves[playerpoke[pokemonusing].move1].phys == 0:
                                    damage = (((42 * moves[enemypoke.move1].power * enemypoke.atk / playerpoke[pokemonusing].defence) / 50) + 2) * (crit * rand)
                                elif moves[playerpoke[pokemonusing].move1].phys == 1:
                                    damage = (((42 * moves[enemypoke.move1].power * enemypoke.spatk / playerpoke[pokemonusing].spdef) / 50) + 2) * (crit * rand)
                                damage = int(round(damage))
                                playerpoke[pokemonusing].health -= damage
                                print("{} takes {} damage!".format(playerpoke[pokemonusing].name, damage) + "\n")
                            if enemymove == 1:
                                print("{} uses {}!".format(enemypoke.name, moves[enemypoke.move2].name))
                                critchance = randint(1, 24)
                                if critchance == 24:
                                    crit = 1.5
                                    print("CRITICAL HIT!")
                                else:
                                    crit = 1
                                rand = random.randrange(85, 100) / 100
                                if moves[playerpoke[pokemonusing].move2].phys == 0:
                                    damage = (((42 * moves[enemypoke.move2].power * enemypoke.atk / playerpoke[pokemonusing].defence) / 50) + 2) * (crit * rand)
                                elif moves[playerpoke[pokemonusing].move2].phys == 1:
                                    damage = (((42 * moves[enemypoke.move2].power * enemypoke.spatk / playerpoke[pokemonusing].spdef) / 50) + 2) * (crit * rand)
                                damage = int(round(damage))
                                playerpoke[pokemonusing].health -= damage
                                print("{} takes {} damage!".format(playerpoke[pokemonusing].name, damage) + "\n")

                    """MOVE 2"""
                    if usingmove == "2":
                        print("\033c")
                        print("{} uses {}!".format(playerpoke[pokemonusing].name, moves[playerpoke[pokemonusing].move2].name))

                        """CRIT CHECK"""
                        critchance = randint(1, 24)
                        if critchance == 24:
                            crit = 1.5
                            print("CRITICAL HIT!")
                        else:
                            crit = 1

                        """RANDOM MODIFIER"""
                        rand = random.randrange(85, 100) / 100

                        """PHYS/SPECIAL CHECK"""
                        if moves[playerpoke[pokemonusing].move1].phys == 0:
                            damage = (((42 * moves[playerpoke[pokemonusing].move2].power * playerpoke[pokemonusing].atk / enemypoke.defence) / 50) + 2) * (crit * rand)
                        elif moves[playerpoke[pokemonusing].move1].phys == 1:
                            damage = (((42 * moves[playerpoke[pokemonusing].move2].power * playerpoke[pokemonusing].spatk / enemypoke.spdef) / 50) + 2) * (crit * rand)
                        damage = int(round(damage))

                        """DEAL DAMAGE"""
                        enemypoke.health -= damage
                        print("{} takes {} damage!".format(enemypoke.name, damage))

                        """ENEMY TURN"""
                        if enemypoke.isAlive():
                            enemymove = random.randrange(0, 2)
                            if enemymove == 0:
                                print("{} uses {}!".format(enemypoke.name, moves[enemypoke.move1].name))
                                critchance = randint(1, 24)
                                if critchance == 24:
                                    crit = 1.5
                                    print("CRITICAL HIT!")
                                else:
                                    crit = 1
                                rand = random.randrange(85, 100) / 100
                                if moves[playerpoke[pokemonusing].move1].phys == 0:
                                    damage = (((42 * moves[enemypoke.move1].power * enemypoke.atk / playerpoke[pokemonusing].defence) / 50) + 2) * (crit * rand)
                                elif moves[playerpoke[pokemonusing].move1].phys == 1:
                                    damage = (((42 * moves[enemypoke.move1].power * enemypoke.spatk / playerpoke[pokemonusing].spdef) / 50) + 2) * (crit * rand)
                                damage = int(round(damage))
                                playerpoke[pokemonusing].health -= damage
                                print("{} takes {} damage!".format(playerpoke[pokemonusing].name, damage) + "\n")
                            if enemymove == 1:
                                print("{} uses {}!".format(enemypoke.name, moves[enemypoke.move2].name))
                                critchance = randint(1, 24)
                                if critchance == 24:
                                    crit = 1.5
                                    print("CRITICAL HIT!")
                                else:
                                    crit = 1
                                rand = random.randrange(85, 100) / 100
                                if moves[playerpoke[pokemonusing].move2].phys == 0:
                                    damage = (((42 * moves[enemypoke.move2].power * enemypoke.atk / playerpoke[pokemonusing].defence) / 50) + 2) * (crit * rand)
                                elif moves[playerpoke[pokemonusing].move2].phys == 1:
                                    damage = (((42 * moves[enemypoke.move2].power * enemypoke.spatk / playerpoke[pokemonusing].spdef) / 50) + 2) * (crit * rand)
                                damage = int(round(damage))
                                playerpoke[pokemonusing].health -= damage
                                print("{} takes {} damage!".format(playerpoke[pokemonusing].name, damage) + "\n")

                """CPU GOES FIRST"""
                if enemypoke.isAlive():
                        """PLAYER TURN"""
                        """MOVE 1"""
                        if usingmove == "1":
                            print("{} uses {}!".format(playerpoke[pokemonusing].name, moves[playerpoke[pokemonusing].move1].name))

                            """CRIT CHECK"""
                            critchance = randint(1, 24)
                            if critchance == 24:
                                crit = 1.5
                                print("CRITICAL HIT!")
                            else:
                                crit = 1

                            """RANDOM MODIFIER"""
                            rand = random.randrange(85, 100) / 100

                            """PHYS/SPECIAL CHECK"""
                            if moves[playerpoke[pokemonusing].move1].phys == 0:
                                damage = (((42 * moves[playerpoke[pokemonusing].move1].power * playerpoke[pokemonusing].atk / enemypoke.defence) / 50) + 2) * (crit * rand)
                            elif moves[playerpoke[pokemonusing].move1].phys == 1:
                                damage = (((42 * moves[playerpoke[pokemonusing].move1].power * playerpoke[pokemonusing].spatk / enemypoke.spdef) / 50) + 2) * (crit * rand)
                            damage = int(round(damage))
                            """(((((Level x 2)/5 + 2) x Move Power x Attack / Defence) / 50) + 2) x (Crit x Random x STAB x Type)"""

                            """DEAL DAMAGE"""
                            enemypoke.health -= damage
                            print("{} takes {} damage! \n".format(enemypoke.name, damage))

                        """MOVE 2"""
                        if usingmove == "2":
                            print("{} uses {}!".format(playerpoke[pokemonusing].name, moves[playerpoke[pokemonusing].move2].name))

                            """CRIT CHECK"""
                            critchance = randint(1, 24)
                            if critchance == 24:
                                crit = 1.5
                                print("CRITICAL HIT!")
                            else:
                                crit = 1

                            """RANDOM MODIFIER"""
                            rand = random.randrange(85, 100) / 100

                            """PHYS/SPECIAL CHECK"""
                            if moves[playerpoke[pokemonusing].move1].phys == 0:
                                damage = (((42 * moves[playerpoke[pokemonusing].move2].power * playerpoke[pokemonusing].atk / enemypoke.defence) / 50) + 2) * (crit * rand)
                            elif moves[playerpoke[pokemonusing].move1].phys == 1:
                                damage = (((42 * moves[playerpoke[pokemonusing].move2].power * playerpoke[pokemonusing].spatk / enemypoke.spdef) / 50) + 2) * (crit * rand)
                            damage = int(round(damage))

                            """DEAL DAMAGE"""
                            enemypoke.health -= damage
                            print("{} takes {} damage! \n".format(enemypoke.name, damage))
            elif command == "kill":
                playerpoke[pokemonusing].health = 0

            elif command == "pokemon":
                x = 1
                for poke in playerpoke:
                    print("{} ({})".format(playerpoke[x - 1].name, x))
                    x += 1
                pokemonusing = int(input()) - 1
                print("\033c")
                print("Go! {}!".format(playerpoke[pokemonusing].name) + "\n")

            elif command == "item":
                print("not in yet lol")
            elif command == "run":
                print("\033c")
                caught = random.randint(1,5) == 1
                if not caught:
                    print("Got away safely!")
                    sys.exit(0)
                else:
                    print("\033c")
                    print("Couldn't get away!")

            if playerpoke[pokemonusing].health <= 0:
                if len(playerpoke) > 1:
                    print("\033c")
                    print("{} Fainted!".format(playerpoke[pokemonusing].name))
                    playerpoke.remove(playerpoke[pokemonusing])
                    if pokemonusing > len(playerpoke):
                        pokemonusing = len(playerpoke) - 1
                    print("Go! {}!".format(playerpoke[pokemonusing].name) + "\n")
                elif len(playerpoke) == 1:
                        print("\033c")
                        print("~~~GAME OVER~~~")
                        quit()
        print("\033c")
        print("Enemy {} is defeated!".format(enemypoke.name))
        enemiesleft -= 1
    win()


    """def yourwelcome(name, health, atk, defence, spatk, spdef, spd):
        print("YOUR POKEMON IS: {} \n has  {} health, \n {} attack, \n {} defence \n {} \n {} {}".format(name, health, atk, defence, spatk, spdef, spd))

    def enemywelcome(name, health, atk, defence, spatk, spdef, spd):
        print("ENEMY POKEMON IS: {} \n has  {} health, \n {} attack, \n {} defence \n {} \n {} {}".format(name, health, atk, defence, spatk, spdef, spd))

    yourwelcome(playerpoke.name, playerpoke.health, playerpoke.atk, playerpoke.defence, playerpoke.spatk, playerpoke.spdef, playerpoke.spd)
    enemywelcome(enemypoke.name, enemypoke.health, enemypoke.atk, enemypoke.defence, enemypoke.spatk, enemypoke.spdef, enemypoke.spd)"""
