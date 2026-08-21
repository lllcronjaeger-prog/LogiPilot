from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget,QVBoxLayout,QGroupBox,QCheckBox,QLabel,QScrollArea
class FilterPanel(QWidget):
    filtersChanged=Signal()
    def __init__(self):
        super().__init__()
        self.boxes={}
        l=QVBoxLayout(self)
        self.status=QLabel("0 von 0 Sendungen sichtbar"); l.addWidget(self.status)
        g=QGroupBox("Unternehmer"); gl=QVBoxLayout(g)
        self.scroll=QScrollArea(); self.scroll.setWidgetResizable(True)
        self.inner=QWidget(); self.inner_l=QVBoxLayout(self.inner); self.scroll.setWidget(self.inner)
        gl.addWidget(self.scroll); l.addWidget(g)
        self.fleet=QCheckBox("Nur Fuhrpark"); self.fleet.stateChanged.connect(self.filtersChanged.emit); l.addWidget(self.fleet); l.addStretch()
    def set_entrepreneurs(self,names):
        while self.inner_l.count():
            i=self.inner_l.takeAt(0)
            if i.widget(): i.widget().deleteLater()
        self.boxes={}
        for n in sorted(names):
            cb=QCheckBox(n); cb.setChecked(True); cb.stateChanged.connect(self.filtersChanged.emit)
            self.boxes[n]=cb; self.inner_l.addWidget(cb)
    def selected(self): return [n for n,b in self.boxes.items() if b.isChecked()]
    def set_status(self,v,t): self.status.setText(f"{v} von {t} Sendungen sichtbar")
