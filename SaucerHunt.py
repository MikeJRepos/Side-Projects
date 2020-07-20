#Program where the student must come up with an algorithm to intercept a flying saucer

#Inputs: Saucers x, y, and z speeds. Units: m/s

#Outputs: Time and position that saucer is hit

import random
import math

class Missle:
    """Saucer Object"""
    def __init__(self, posX, posY, posZ, velX, velY, velZ, accelX, accelY, accelZ):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.velX = velX
        self.velY = velY
        self.velZ = velZ
        self.accelX = accelX
        self.accelY = accelY
        self.accelZ = accelZ

    def getXPos(self):
        return self.posX

    def getYPos(self):
        return self.posY

    def getZpos(self):
        return self.posZ

    def getXVel(self):
        return self.velX

    def getYVel(self):
        return self.velY

    def getZVel(self):
        return self.velZ

    def getXAccel(self):
        return self.accelX
    
    def getYAccel(self):
        return self.accelY

    def getZAccel(self):
        return self.accelZ

    def misXPosition(self, Missle, t):
        xPosition = (Missle.getXAccel() * t**2) + (Missle.getXVel() * t) + Missle.getXPos()
        return xPosition

    def misYPosition(self, Missle, t):
        yPosition = (Missle.getYAccel() * t**2) + (Missle.getYVel() * t) + Missle.getYPos()
        return yPosition

    def misZPosition(self, Missle, t):
        zPosition = (Missle.getZAccel() * t**2) + (Missle.getZVel() * t) + Missle.getZPos()
        return yPosition

    def misAbsPosition(self, x, y):
        return math.sqrt((x**2 + y**2))

class Saucer:
    """Saucer Object"""
    def __init__(self, posX, posY, posZ, velX, velY, velZ, accelX, accelY, accelZ):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.velX = velX
        self.velY = velY
        self.velZ = velZ
        self.accelX = accelX
        self.accelY = accelY
        self.accelZ = accelZ

    def getXPos(self):
        return self.posX

    def getYPos(self):
        return self.posY

    def getZpos(self):
        return self.posZ

    def getXVel(self):
        return self.velX

    def getYVel(self):
        return self.velY

    def getZVel(self):
        return self.velZ

    def getXAccel(self):
        return self.accelX
    
    def getYAccel(self):
        return self.accelY

    def getZAccel(self):
        return self.accelZ

    def ufoXPosition(self, Saucer, t):
        xPosition = (self.accelX * t**2) + (Saucer.getXVel() * t) + Saucer.getXPos()
        return xPosition

    def ufoYPosition(self, Saucer, t):
        yPosition = (Saucer.getYAccel() * t**2) + (Saucer.getYVel() * t) + Saucer.getYPos()
        return yPosition

    def ufoZPosition(self, Saucer, t):
        zPosition = (Saucer.getZAccel() * t**2) + (Saucer.getZVel() * t) + Saucer.getZPos()
        return zPosition

    def ufoAbsPosition(self, x, y):
        return math.sqrt((x**2 + y**2))


def trackingAlgorithm():
    print("Tracking Started")
    t = 0
    ufo = Saucer(10, 2, 0, 2, 2, 2, 0, 0, 0)
    missle = Missle(0, 0, 0, 5, 5, 5, 0, 0, 0)
    for t in range(100):
        Ux = ufo.ufoXPosition(ufo, t)
        Uy = ufo.ufoYPosition(ufo, t)
        UdistFromOrigin = ufo.ufoAbsPosition(Ux, Uy)
        print("UFO Position: %s" %UdistFromOrigin)
        Mx = missle.misXPosition(missle, t)
        My = missle.misYPosition(missle, t)
        MdistFromOrigin = missle.misAbsPosition(Mx, My)
        print("Missle Position: %s" %MdistFromOrigin)
        if MdistFromOrigin >= UdistFromOrigin:
            print("HIT at t = %s" %t)
            break
 
    

trackingAlgorithm()
