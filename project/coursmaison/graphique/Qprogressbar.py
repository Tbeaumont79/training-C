#!/bin/env python

from PySide import QtGui
from PySide import QtCore
import sys
import time

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
progress = QtGui.QProgressBar(window)
progress.setMaximum(100)
layout = QtGui.QVBoxLayout()
layout.addWidget(progress)
window.setLayout(layout)

def update():
    if progress.value() == progress.maximum():
        progress.reset()
        progress.setMaximum(progress.maximum() + 20)
        progress.setValue(progress.value() + 1)

    timer = QtCore.QTimer(window)
    timer.start(100)
    timer.connect(timer, QtCore.SIGNAL('timeout()'), update)

    window.show()
    time.sleep(8)
    app.exec_()
update()
