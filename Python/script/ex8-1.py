#! /usr/bin/python2
# -*- coding: utf-8 -*-

print "\n== Liste Jours avec excepiton ==\n"

print 'Entrer un jour de la semaine en anglais : '
day=raw_input()

tradDay = { "lundi" : "Monday", "mardi" : "Tuesday", "mercredi": "Wednesday", "jeudi": "Thurday", "vendredi": "Friday", "samedi": "Saturday", "dimanche": "Sunday"}

if day in tradDay :
    print '\nJour traduit : {}\n'.format(tradDay[day])
else:
    raise ValueError("{} n\'est pas dans les jours de la semaine".format(day))
