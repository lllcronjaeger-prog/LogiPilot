from PySide6.QtCore import Signal
from PySide6.QtWidgets import *
class FilterPanel(QWidget):
    filtersChanged=Signal()
    def __init__(self):
        super().__init__(); self.checkboxes={}; l=QVBoxLayout(self); self.status_label=QLabel('0 von 0 Sendungen sichtbar'); l.addWidget(self.status_label); self.fleet_only=QCheckBox('Nur Fuhrpark'); self.fleet_only.stateChanged.connect(self.filtersChanged.emit); l.addWidget(self.fleet_only)
