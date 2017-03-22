#! /usr/bin/python2
# -*- coding: utf-8 -*-

import math

print "\n== Calcul de la circonférence d'un cercle avec lecture au clavier ==\n"

print 'Entrer un rayon : '
rayon = input()

print "\nRayon : " + str(rayon) + "\n"

circ = math.pi * 2 * rayon

print "Resultat : " + str(circ) + "\n"
