#! /usr/bin/python2
# -*- coding: iso-8859-1 -*-

from os import system, name

print 'HLLWRD'

if name == 'posix':
    print 'Appuyer sur une touche pour fermer...'
    system('read key')
    pass
