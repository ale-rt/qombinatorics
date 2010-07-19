"""
Copyright (c) 2009 Alessandro Pisa <alessandro...pisa@@@gmail...com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from qombinatorics.QombGui import Ui_MainWindow, QtGui, QtCore

from sys import exit

VERSION = "1.0rc1"

BGCOLORS = ('white', '#eeeeee')
QOMBICON16 = ":/img/icons/16/qombicon.png"

def factorial(n):
    """Factorial calculation
    
    This is a really simple function
    it's argument should never be greater then 100 so we shouldn't have 
    particular problems
    
    >>> factorial(0)
    1L
    >>> factorial(1)
    1L
    >>> factorial(5)
    120L
    >>> factorial(100)
    933262154...4000000000000000000000000L
    """
    if n == 0:
        return 1L
    else:
        return factorial(n - 1) * n

class QombMainWindow(Ui_MainWindow):
    '''
    This class extends the pyuic generated Ui_MainWindow class, adding 
    attributes and functions that cannot be edited by qt designer
    
    Simple usecase
    First we get the window
    >>> my = QombMainWindow()
    >>> my
    <__main__.QombMainWindow object at ...>
    
    We should have some attributes defined
    >>> my.index
    0
    >>> my.app
    <PyQt4.QtGui.QApplication object at ...>
    >>> my.MainWindow
    <PyQt4.QtGui.QMainWindow object at ...>
    
    Let's try to use my app
    First we clean the output text
    >>> my.output.setText('')
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'')

    Then we play with the interface
    The default tab should be the one of permutations
    >>> my.tabWidget.tabText(my.tabWidget.currentIndex())
    PyQt4.QtCore.QString(u'&Permutations')
    
    We change the sliders values
    >>> my.spinSet.setValue(4)
    >>> my.spinSubset.setValue(2)
    >>> my.permutationSpin.setValue(4)
    >>> my.picksSpin.setValue(2)
    
    and call the calculate function to see the output text
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Permutation with repetitions...(4)2 = 16 ')
    
    Then we toggle the repetitions checkBox
    >>> my.output.setText('')
    >>> my.repetitionCheckBox.setCheckState(0)
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Permutation without repetitions...4!/(4-2)! = 12 ')

    And we pass to calculate Combinations
    >>> my.tabWidget.setCurrentIndex(1)
    >>> my.tabWidget.tabText(my.tabWidget.currentIndex())
    PyQt4.QtCore.QString(u'&Combinations')
    
    And we redo the tests
    >>> my.output.setText('')
    >>> my.repetitionCheckBox.setCheckState(2)
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Combination with repetitions...(4+2-1)!/2!/(4-1)! = 10 ')
    
    >>> my.output.setText('')
    >>> my.repetitionCheckBox.setCheckState(0)
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Combination without repetitions...4!/2!/(4-2)! = 6 ')
    
    Now we switch the sliderValues and redo the tests
    >>> my.spinSet.setValue(2)
    >>> my.spinSubset.setValue(4)
    >>> my.permutationSpin.setValue(2)
    >>> my.picksSpin.setValue(4)
    
    >>> my.tabWidget.setCurrentIndex(0)
    >>> my.repetitionCheckBox.setCheckState(0)
    >>> my.output.setText('')
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Permutation without...the number of pics! ')
    
    >>> my.tabWidget.setCurrentIndex(0)
    >>> my.repetitionCheckBox.setCheckState(2)
    >>> my.output.setText('')
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Permutation with repetitions...(2)4 = 16 ')
    
    >>> my.tabWidget.setCurrentIndex(1)
    >>> my.repetitionCheckBox.setCheckState(0)
    >>> my.output.setText('')
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Combination without ... subset! ')
    
    >>> my.tabWidget.setCurrentIndex(1)
    >>> my.repetitionCheckBox.setCheckState(2)
    >>> my.output.setText('')
    >>> my.calculate()
    >>> my.output.toPlainText()
    PyQt4.QtCore.QString(u'Combination with ... subset! ')
    '''
    def __init__(self):
        '''
        Constructing the class
        '''
        super(Ui_MainWindow, self).__init__()
        self.index = 0
        self.app = QtGui.QApplication([])
        self.MainWindow = QtGui.QMainWindow()

        self.setupUi(self.MainWindow)
        self.cursor = QtGui.QTextCursor(self.output.document())
        self.cursor.movePosition(QtGui.QTextCursor.End)
        self.scrollbar = self.output.verticalScrollBar()
        # connecting signal slots
        self.app.connect(self.calculateButton, QtCore.SIGNAL("clicked()"), self.calculate)
        self.app.connect(self.action_About, QtCore.SIGNAL("triggered()"), self.about)

    def appendResults(self, results):
        """Appends the results in the TextEdit"""
        self.output.append('')

        self.cursor.insertHtml('<p>%s</p>' % results)
        self.scrollbar.setValue(self.scrollbar.maximum())

    def combinationParser(self):
        '''
        gets user input from the interface and returns it as a dict 
        when calculating combinations
        '''
        return {'n' : self.spinSet.value(),
                'k' : self.spinSubset.value()}

    def permutationParser(self):
        '''
        gets user input from the interface and returns it as a dict
        when calculating permutations
        '''
        return {'n' : self.permutationSpin.value(),
                'k' : self.picksSpin.value()}

    def permutationWithoutRepetition(self):
        '''
        handles button click when calculating permutations without repetitions
        '''
        stuff = self.permutationParser()
        if stuff['k'] > stuff['n']:
            return '''<br><img src="%s" alt="Error!">
                    Objects in set must be greater 
                    than the number of pics!''' % QOMBICON16
        else:
            stuff['answer'] = factorial(stuff['n']) / factorial(stuff['n'] - stuff['k'])
            return "%(n)s!/(%(n)s-%(k)s)! = %(answer)s" % stuff

    def permutationWithRepetition(self):
        '''
        handles button click when calculating permutations with repetitions
        '''
        stuff = self.permutationParser()
        stuff['answer'] = stuff['n'] ** stuff['k']
        return "(%(n)s)<sup>%(k)s</sup> = %(answer)s" % stuff

    def combinationWithoutRepetition(self):
        '''
        handles button click when calculating combinations without repetitions
        '''
        stuff = self.combinationParser()
        if stuff['k'] > stuff['n']:
            return '''<br><img src="%s" alt="Error!">
                    Objects in set must be greater 
                        than the one in subset!''' % QOMBICON16
        else:
            stuff['answer'] = factorial(stuff['n']) / factorial(stuff['k']) / factorial(stuff['n'] - stuff['k'])
            return "%(n)s!/%(k)s!/(%(n)s-%(k)s)! = %(answer)s" % stuff

    def combinationWithRepetition(self):
        '''
        handles button click when calculating combinations with repetitions
        '''
        stuff = self.combinationParser()
        if stuff['k'] > stuff['n']:
            return '''<br><img src="%s" alt="Error!">
                        Objects in set must be greater 
                        than the one in subset!''' % QOMBICON16
        elif stuff['n'] == 0:
            # when n is zero the answer is always 1
            return "(%(n)s+%(k)s-1)!/%(k)s!/(%(n)s-1)! = 1" % stuff
        else:
            num = factorial(stuff['n'] + stuff['k'] - 1)
            den = factorial(stuff['k']) * factorial(stuff['n'] - 1)
            stuff['answer'] = num / den
            return "(%(n)s+%(k)s-1)!/%(k)s!/(%(n)s-1)! = %(answer)s" % stuff

    def about(self):
        text = """<div><h1>qombinatorics %s</h1><br>
            qombinatorics is an application devoted
            to calculate combinations and permutations.
            <br><br>
            <b>Developer</b><br>
            Alessandro Pisa
            <br><br>
            <b>Homepage</b><br>
            <a href="http://darkmoon.altervista.org">http://darkmoon.altervista.org</a>
            <br><br>
            <b>The code</b><br>
            <a href="http://http://code.google.com/p/qombinatorics/">http://code.google.com/p/qombinatorics</a>
            <br><br>
            <b>About combinatorics</b><br>
            <a href="http://en.wikipedia.org/wiki/Combinatorics">http://en.wikipedia.org/wiki/Combinatorics</a>
            </div>
            """ % VERSION
        QtGui.QMessageBox.information(self.calculateButton,
                                      "About combinatorics",
                                      text)

    def calculate(self):
        '''
        handler for button clicked signal
        '''
        tabIndex = self.tabWidget.currentIndex()
        checkBoxState = self.repetitionCheckBox.checkState()
        self.output.setTextBackgroundColor(QtGui.QColor(BGCOLORS[self.index % 2]))
        if tabIndex == 0:
            if checkBoxState == 2:
                title = "Permutation with repetitions"
                body = self.permutationWithRepetition()
            elif checkBoxState == 0:
                title = "Permutation without repetitions"
                body = self.permutationWithoutRepetition()
        elif tabIndex == 1:
            if checkBoxState == 2:
                title = 'Combination with repetitions'
                body = self.combinationWithRepetition()
            elif checkBoxState == 0:
                title = 'Combination without repetitions'
                body = self.combinationWithoutRepetition()
        else:
            title, body = "<h2><img src='%s'> Something is going wrong!!!</h2>" % QOMBICON16, ''
        msg = """
        <h4>%s</h4>
        %s
        <hr />
        """ % (title, body)

        self.appendResults(msg)
        self.index += 1

def run():
    '''
    window runner
    '''
    ui = QombMainWindow()
    ui.MainWindow.show()
    exit(ui.app.exec_())

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
