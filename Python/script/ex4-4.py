#! /usr/bin/python2
# -*- coding: utf-8 -*-

print "\n== Température ==\n"

print 'Entrer une température : '
temp=input()

if temp > 25 :
    print '\nChaud\n'
elif temp >= 20 and temp <= 25 :
    print '\nParfait\n'
else:
    print '\nFroid\n'
