#! /usr/bin/python2
# -*- coding: utf-8 -*-

# A completer (distinction des en -er et en -ir pour les Conjugaison)

def displayConj(conjs, verbe, temps):
    if temps == "present" :
        verbe = verbe[0:-1]

    for conj in conjs :
        print conj.format(verbe)

print "\n== Conjugaison futur et présent : -er -ir ==\n"

print 'Entrer votre verbe (en -er ou -ir) : '
verbe=raw_input()

conjPresent = ['\tJe {}', '\tTu {}s', '\tIl/Elle/On {}', '\tNous {}ons', '\tVous {}z', '\tIls/Elles {}ont']
print '\nAu présent :\n'

if verbe[0] in ['a', 'e', 'i', 'o', 'u', 'y'] :
    conjPresent[0] = '\tJ\'{}'

displayConj(conjPresent, verbe, 'present')

print '\nAu futur :\n'
conjFutur = ['\tJe {}ai', '\tTu {}as', '\tIl/Elle/On {}a', '\tNous {}ons', '\tVous {}ez', '\tIls/Elles {}ont']

if verbe[0] in ['a', 'e', 'i', 'o', 'u', 'y'] :
    conjFutur[0] = '\tJ\'{}ai'

displayConj(conjFutur, verbe, 'futur')
