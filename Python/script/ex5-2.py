#! /usr/bin/python2
# -*- coding: utf-8 -*-

print "\n== Calcul de puissance ==\n"


def power(**args):
    return args['a']**args['b'];

r = power(a=2, b=4)

print '\nPuissance {a}**{b} : {res}\n'.format(a=2, b=4, res=r)
