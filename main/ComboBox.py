from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QComboBox


class ComboBox(QComboBox):
    popupAboutToBeShown = pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()
