#!/usr/bin/env python
## Copyright (c) 2008 Alessandro Pisa <alessandro...pisa@@@gmail...com>
## All rights reserved.
##
## Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions
## are met:
##
## 1. Redistributions of source code must retain the above copyright
##    notice, this list of conditions and the following disclaimer.
## 2. Redistributions in binary form must reproduce the above copyright
##    notice, this list of conditions and the following disclaimer in the
##    documentation and/or other materials provided with the distribution.
##
## THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
## IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
## OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
## IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
## INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
## NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
## THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
from qombinatorics.QombGui import *

app = QtGui.QApplication([])
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

VERSION=0.2

def factorial(n):
    """Factorial calculation"""
    if n==0: return 1L
    else: return factorial(n-1)*n

def newline():
    ui.output.append("<hr>")

def permutationWithoutRepetition():
    stuff={}
    stuff['n'] = ui.permutationSpin.value()
    stuff['k'] = ui.picksSpin.value()
    if stuff['k']>stuff['n']:
        newtext="<b>Error!</b> Objects in set must be greater than the number of picks!"
    else:
        stuff['answer']=factorial(stuff['n'])/factorial(stuff['n']-stuff['k'])
        newtext="%(n)s!/(%(n)s-%(k)s)! = %(answer)s" % stuff
    ui.output.append("%s" % (newtext))

def permutationWithRepetition():
    stuff={}
    stuff['n'] = ui.permutationSpin.value()
    stuff['k'] = ui.picksSpin.value()
    stuff['answer']=stuff['n']**stuff['k']
    newtext="(%(n)s)<sup>%(k)s</sup> = %(answer)s" % stuff
    ui.output.append("%s" % (newtext))

def combinationWithoutRepetition():
    stuff={}
    stuff['n'] = ui.spinSet.value()
    stuff['k'] = ui.spinSubset.value()
    if stuff['k']>stuff['n']:
        newtext="<b>Error!</b> Objects in set must be greater than the one in subset!"
    else:
        stuff['answer'] = factorial(stuff['n'])/factorial(stuff['k'])/factorial(stuff['n']-stuff['k'])
        newtext="%(n)s!/%(k)s!/(%(n)s-%(k)s)! = %(answer)s" % stuff
    ui.output.append("%s" % (newtext))

def combinationWithRepetition():
    stuff={}
    stuff['n'] = ui.spinSet.value()
    stuff['k'] = ui.spinSubset.value()
    if stuff['k']>stuff['n']:
        newtext="<b>Error!</b> Objects in set must be greater than the one in subset!"
    elif stuff['n'] == 0:
        stuff['answer'] = 1
        newtext="(%(n)s+%(k)s-1)!/%(k)s!/(%(n)s-1)! = %(answer)s" % stuff
    else:
        num=factorial(stuff['n']+stuff['k']-1)
        den=factorial(stuff['k'])*factorial(stuff['n']-1)
        stuff['answer'] = num/den
        newtext="(%(n)s+%(k)s-1)!/%(k)s!/(%(n)s-1)! = %(answer)s" % stuff
    ui.output.append("%s" % (newtext))

def combination():
    if ui.repetitionCheckBox.checkState()==2:
        ui.output.append("<br><b>Combination with repetitions</b>")
        combinationWithRepetition()
    else:
        ui.output.append("<br><b>Combination without repetitions</b>")
        combinationWithoutRepetition()

def permutation():
    if ui.repetitionCheckBox.checkState()==2:
        ui.output.append("<br><b>Permutation with repetitions</b>")
        permutationWithRepetition()
    else:
        ui.output.append("<br><b>Permutation without repetitions</b>")
        permutationWithoutRepetition()

def about():
    text="""<h1>qombinatorics %s</h1><br>
        qombinatorics is an application devoted
        to calculate combinations and permutations.
        <br><br>
        <b>Developer</b><br>
        Alessandro Pisa
        <br><br>
        <b>Homepage</b><br>
        <a href='http://darkmoon.altervista.org'>http://darkmoon.altervista.org</a>
        <br><br>
        <b>About combinatorics</b><br>
        <a href='http://en.wikipedia.org/wiki/Combinatorics'>http://en.wikipedia.org/wiki/Combinatorics</a>
        """ % VERSION
    QtGui.QMessageBox.information(ui.calculateButton, "About combinatorics", text)

def calculate():
    if ui.tabWidget.currentIndex()==0:
        permutation()
    if ui.tabWidget.currentIndex()==1:
        combination()
    newline()

# button stuff
app.connect(ui.calculateButton,QtCore.SIGNAL("clicked()"),calculate)
app.connect(ui.action_About,QtCore.SIGNAL("triggered()"),about)
def run():
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
