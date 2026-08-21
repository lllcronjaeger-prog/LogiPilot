from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QTableView,QGroupBox,QCheckBox,QPushButton,QLabel
from app.ui.table_model import PandasTableModel
class ImportPage(QWidget):
    def __init__(self,df):
        super().__init__(); r=QHBoxLayout(self); l=QVBoxLayout(); l.addWidget(QLabel('<h2>Wochenansicht</h2>')); t=QTableView(); t.setModel(PandasTableModel(df)); t.setSortingEnabled(True); l.addWidget(t); r.addLayout(l,4); g=QGroupBox('Filter & Aktionen'); v=QVBoxLayout(g); [v.addWidget(QCheckBox(x)) for x in ['Unternehmer ausschließen','Nur Fuhrpark','Bearbeitete ausblenden']]; v.addStretch(); v.addWidget(QPushButton('Änderungen speichern')); b=QPushButton('Excel erzeugen'); b.setEnabled(False); v.addWidget(b); r.addWidget(g,1)
