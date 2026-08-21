from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QTableView,QLabel,QGroupBox,QCheckBox,QPushButton
from app.ui.pandas_model import PandasModel
class WeekView(QWidget):
    def __init__(self,df):
        super().__init__(); root=QHBoxLayout(self); l=QVBoxLayout(); l.addWidget(QLabel("<h2>Wochenansicht</h2>")); t=QTableView(); t.setModel(PandasModel(df)); t.setSortingEnabled(True); l.addWidget(t); root.addLayout(l,4); g=QGroupBox("Filter & Aktionen"); r=QVBoxLayout(g); [r.addWidget(QCheckBox(x)) for x in ["Unternehmer ausschließen","Nur Fuhrpark","Bearbeitete ausblenden"]]; r.addStretch(); r.addWidget(QPushButton("Speichern")); b=QPushButton("Excel erzeugen"); b.setEnabled(False); r.addWidget(b); root.addWidget(g,1)
