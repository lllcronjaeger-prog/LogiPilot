from PySide6.QtWidgets import QWidget,QGridLayout,QGroupBox,QVBoxLayout,QLabel

class DashboardPage(QWidget):
    def __init__(self, stats=None):
        super().__init__()
        stats = stats or {}
        layout = QGridLayout(self)
        cards = [
            ("Aktive KW", stats.get("week","-")),
            ("Sendungen", stats.get("shipments",0)),
            ("Unternehmer", stats.get("entrepreneurs",0)),
            ("Fuhrpark", stats.get("fleet",0)),
        ]
        for i,(title,value) in enumerate(cards):
            box=QGroupBox(title)
            b=QVBoxLayout(box)
            lbl=QLabel(str(value))
            lbl.setStyleSheet("font-size:28px;font-weight:bold;")
            b.addWidget(lbl)
            layout.addWidget(box,i//2,i%2)
