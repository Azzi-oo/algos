def combat(health, damage):
    health1 = health - damage
    if health1 < 0:
        health1 = 0
    return health1
