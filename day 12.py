# scope
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Local Scope
def drink_portion():
    portion_strength = 2
    print(portion_strength)


# GLobal Scope
player_health = 10


def drink_portione():
    portion_strength = 2
    print(player_health)


drink_portione()

game_level = 3

wezi = ["Skeleton", "Zoombie", "Alien"]
if game_level < 5:
    new_wezi = wezi[0]


print(new_wezi)
