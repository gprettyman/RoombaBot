#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, InfraredSensor)
from pybricks.parameters import (Port, Direction, Color)
from pybricks.robotics import DriveBase

greg = EV3Brick()
colorBlind = ColorSensor(Port.S1)
predatorEyes = InfraredSensor(Port.S4)
leftMotor = Motor(Port.B, positive_direction = Direction.CLOCKWISE, gears = None)
rightMotor = Motor(Port.C, positive_direction = Direction.CLOCKWISE, gears = None)
wheels = DriveBase(leftMotor, rightMotor, wheel_diameter=43.2, axle_track = 145)
attackMotor = Motor(Port.D, positive_direction = Direction.CLOCKWISE, gears = None)



Quit = False
counter = 0

def retreat():
    wheels.stop()
    wheels.turn(120)
    greg.speaker.beep(frequency = 2500, duration = 500)
        
def attack():
    greg.speaker.beep(frequency = 3000, duration = 250)
    attackMotor.run_angle(20, 120, then=Stop.HOLD, wait=True)
    attackMotor.run_angle(20, -120, then=Stop.HOLD, wait=True)

while Quit != True:
    wheels.drive(300, 0)
    if counter == 10:
        Quit = True
    if (colorBlind.color() == Color.RED) or (predatorEyes.distance() < 25):
        retreat()
        counter += 1
    elif (colorBlind.color() == Color.BLACK):
        attack()
        counter += 1