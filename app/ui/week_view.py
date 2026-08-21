
from PySide6.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QTableView,QGroupBox,QCheckBox,QPushButton,QLabel
from app.ui.pandas_model import PandasModel

class WeekView(QWidget):
    def __init__(self,dataframe):
        super().__init__()
        root=QHBoxLayout(self)
        left=QVBoxLayout()
        left.addWidget(QLabel("<h2>Wochenansicht</h2>"))
        self.table=QTableView()
        self.table.setModel(PandasModel(dataframe))
        self.table.setSortingEnabled(True)
        left.addWidget(self.table)
        root.addLayout(left,4)

        box=QGroupBox("Filter")
        right=QVBoxLayout(box)
        self.exclude=QCheckBox("Unternehmer ausschließen")
        self.fp=QCheckBox("Nur Fuhrpark")
        right.addWidget(self.exclude)
        right.addWidget(self.fp)
        right.addStretch()
        right.addWidget(QPushButton("Speichern"))
        export=QPushButton("Excel erzeugen")
        export.setEnabled(False)
        right.addWidget(export)
        root.addWidget(box,1)
