# class for an IFS transform, which consists of
# 8 parameters:
#    SCALING/REFLECTION: r and s (horizontal and vertical respectively)
#    ROTATION: theta and phi (horizontal and vertical rotation, respectively)
#    TRANSLATION: h and k (horizontal and vertical shift, respectively)
#    PROBABILITY: p
#    COLOR: c
#
# For a transformation to be "interesting", it needs to be a contraction, which
# means r and s must be no greater than 1 in magnitude. In other words,
#      |r| <= 1 and |s| <= 1
#
# theta and phi will be stored in DEGREES
#
# no restrictions on h and k
#
# p is always a non-negative WHOLE number, representing a probability weighting
# for that transformation. p = 0 is a way of turning that transformation OFF. The higher
# p is, the more likely it is that the transformation will be selected.
#
# c can be any valid color in python

from math import *

class IFS_Transform:

    def __init__(self, xScale = 0.5, yScale = 0.5,
                 theta = 0.0, phi = 0.0,
                 h = 0.0, k = 0.0,
                 p = 1, c = 'white'):
        # scaling and reflection
        self.r = xScale
        self.s = yScale

        # rotation (rigid if theta = phi)
        self.theta = theta
        self.phi = phi
        self.thetaRadians = radians(self.theta)
        self.PhiRadians = radians(self.phi)

        # translation
        self.e = h
        self.f = k

        # probability and color
        self.prob = p
        self.color = c

    def setR(self, xScale):
        self.r = xScale

    def setS(self, yScale):
        self.s = xScale

    def setTheta(self, angle):
        self.theta = angle
        self.thetaRadians = radians(self.theta)

    def setPhi(self, angle):
        self.phi = angle
        self.PhiRadians = radians(self.phi)

    def setHshift(self, shift):
        self.h = shift

    def setVshift(self, shift):
        self.k = shift

    def setProb(self, prob):
        self.p = prob

    def setColor(self, myColor):
        self.c = myColor

    def getR(self):
        return self.r

    def getS(self):
        return self.s

    def getTheta(self):
        return self.theta

    def getPhi(self):
        return self.phi

    def getE(self):
        return self.e

    def getF(self):
        return self.f

    def getProb(self):
        return self.prob

    def getColor(self):
        return self.color

    def transformPoint(self, x, y):
        newX = x * self.r * cos(thetaRadians) - y * self.s * sin(phiRadians) + self.e
        newY = x * self.r * sin(thetaRadians) + y * self.s * cos(phiRadians) + self.f
        return newX, newY

    def __str__(self):
        #toString method
        result = '[scale(' + str(self.r) + ',' + str(self.s) + '), '
        result += 'rot(' + str(self.theta) + ',' + str(self.phi) + '), '
        result += 'trans(' + str(self.e) + ',' + str(self.f) + '), '
        result += 'prob(' + str(self.prob) + '), '
        result += 'col(' + str(self.color) + ')]'
        return result
