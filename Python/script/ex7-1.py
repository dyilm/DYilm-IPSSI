#! /usr/bin/python2
# -*- coding: utf-8 -*-

import math

print "\n== Calculs cercle avec classe ==\n"

class Cercle :
    "Calculs de cercle"
    def __init__ (self, r=1) :
        self.rayon = r
    def diametre (self) :
        diam = self.rayon * 2
        return diam
    def circonference (self) :
        circ = math.pi * 2 * self.rayon
        return circ


print 'Entrer votre rayon : '
ray = input()

c = Cercle(ray)

print "\nRayon : {}".format(ray)
print "Diametre : {}".format(c.diametre())
print "Circonférence : {}\n".format(c.circonference())
