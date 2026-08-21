from PySide6.QtCore import Signal
from PySide6.QtWidgets import *
class FilterPanel(QWidget):
    filtersChanged=Signal()
    def __init__(self):
        super().__init__(); l=QVBoxLayout(self); self.status=QLabel('0 von 0 Sendungen sichtbar'); l.addWidget(self.status); self.fleet=QCheckBox('Nur Fuhrpark'); l.addWidget(self.fleet)
