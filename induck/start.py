import induck as duck

##############세팅############
induck = duck.Duck(3, "인덕더럭쿵덕", (0,0))
duck.start()
duck.create_lake(10,10)
duck.set_images()
duck.stamp(induck)
#############################

def movemove(n):
    for i in range(n):
        induck.move()

induck.turn_right()
induck.turn_right()
movemove(3)

induck.turn_left()
movemove(5)

induck.turn_right()
induck.turn_right()
induck.turn_right()
movemove(2)

induck.turn_right()
movemove(2)

induck.turn_right()
movemove(7)

induck.turn_right()
movemove(3)


duck.last()

# duck.turnRight()
# duck.turnRight()

