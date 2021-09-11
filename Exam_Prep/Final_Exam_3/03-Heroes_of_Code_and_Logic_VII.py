# 03. Heroes of Code and Logic VII
max_hp = 100
max_mp = 200

n = int(input())

heroes_party = {}

for _ in range(n):
    heroes = input().split()
    hero = heroes[0]
    hp = int(heroes[1])
    mp = int(heroes[2])
    if hp <= max_hp and mp <= max_mp:
        heroes_party[hero] = {'health_power': hp, 'mana_power': mp}

commands = input()

while not commands == "End":
    command = commands.split(" - ")[0]
    hero_name = commands.split(" - ")[1]

    if command == "CastSpell":
        mana_power_needed = int(commands.split(" - ")[2])
        spell_name = commands.split(" - ")[3]

        if heroes_party[hero_name]['mana_power'] >= mana_power_needed:
            heroes_party[hero_name]['mana_power'] -= mana_power_needed

            print(f"{hero_name} has successfully cast "
                  f"{spell_name} and now has "
                  f"{heroes_party[hero_name]['mana_power']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(commands.split(" - ")[2])
        attacker = commands.split(" - ")[3]

        heroes_party[hero_name]['health_power'] -= damage
        if heroes_party[hero_name]['health_power'] > 0:

           print(f"{hero_name} was hit for {damage}"
                 f" HP by {attacker} and now has "
                 f"{heroes_party[hero_name]['health_power']} HP left!")
        else:
            del heroes_party[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        amount = int(commands.split(" - ")[2])

        if heroes_party[hero_name]['mana_power'] + amount > max_mp:
            print(f"{hero_name} recharged for {max_mp - heroes_party[hero_name]['mana_power']} MP!")
            heroes_party[hero_name]['mana_power'] = max_mp
        else:
            heroes_party[hero_name]['mana_power'] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif command == "Heal":
        health_power_amount = int(commands.split(" - ")[2])
        if heroes_party[hero_name]['health_power'] + health_power_amount > max_hp:
            print(f"{hero_name} healed for {max_hp - heroes_party[hero_name]['health_power']} HP!")
            heroes_party[hero_name]['health_power'] = max_hp
        else:
            heroes_party[hero_name]['health_power'] += health_power_amount
            print(f"{hero_name} healed for {health_power_amount} HP!")

    commands = input()


for key,value in sorted(heroes_party.items(), key=lambda x: (-x[1]['health_power'], x[0])):
    print(f"{key}")
    print(f" HP: {value['health_power']}")
    print(f" MP: {value['mana_power']}")