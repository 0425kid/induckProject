import induck as duck

##############세팅############
duck.start()
duck.create_lake(10,10)
duck.set_images()

induck = duck.Duck(3, "인덕더럭쿵덕", (3,3), 0.1)
duck.stamp(induck)
#############################

def movemove(n):
    for i in range(n):
        induck.move()

def zigzag(n):
    movemove(n)
    induck.turn_left()
    induck.move()
    induck.turn_left()
    movemove(n)

def corner():
    induck.turn_right()
    induck.move()
    induck.turn_right()


induck.turn_right()
induck.turn_right()
movemove(4)
induck.turn_left()
movemove(5)
induck.turn_left()
movemove(7)
induck.turn_left()
movemove(8)
induck.turn_left()
movemove(6)

duck.last()

# duck.turnRight()
# duck.turnRight()

