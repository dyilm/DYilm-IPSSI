#! /usr/bin/python2
# -*- coding: utf-8 -*-

# A completer (distinction des en -er et en -ir pour les Conjugaison)

class Conjugaison :
    "Class conjugaison"
    def __init__(self, v=''):
        if v != '':
            self.verbe = v
        else:
            raise ValueError('Pas de verbe defini')

        self.conjPresent = ['\tJe {}', '\tTu {}s', '\tIl/Elle/On {}', '\tNous {}ons', '\tVous {}z', '\tIls/Elles {}ont']
        self.conjFutur = ['\tJe {}ai', '\tTu {}as', '\tIl/Elle/On {}a', '\tNous {}ons', '\tVous {}ez', '\tIls/Elles {}ont']

        if verbe[0] in ['a', 'e', 'i', 'o', 'u', 'y'] :
            self.conjPresent[0] = '\tJ\'{}'
            self.conjFutur[0] = '\tJ\'{}ai'
    def exportConj(self, file):
        # Export de la Conjugaison au futur

        print >> file, 'Au futur : \n'
        for conj in self.conjFutur :
            print >> file, conj.format(verbe)

        # Export de la Conjugaison au present

        print >> file, '\nAu présent : \n'
        verbe_pre = self.verbe[0:-1]

        for conj in self.conjPresent :
            print >> file, conj.format(verbe_pre)




print "\n== Conjugaison futur et présent : -er -ir ==\n"

print 'Entrer votre verbe (en -er ou -ir) : '

verbe=raw_input()
c = Conjugaison(verbe)

# Ouverture du fichier
try:
    outfile = open('conj.txt', 'w')
except IOError:
    print "Error when open file"
else:
    # Appel de la fonction pour exporter les conjugaisons dans le fichier ouvert
    c.exportConj(outfile)

    # Fermeture du fichier
    outfile.close()
