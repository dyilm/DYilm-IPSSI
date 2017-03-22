#! /usr/bin/python2
# -*- coding: utf-8 -*-

print "\n== Calcul moyenne ==\n"


def average(*notes):
    aver = 0

    # Addition de toutes les notes
    for note in notes:
        aver += note

    # Division par le nombre de note
    aver = aver / len(notes)

    return aver;


print '\nMoyenne : {}\n'.format(average(15,18,14,5))
