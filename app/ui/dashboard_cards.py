from PySide6.QtWidgets import QWidget,QGridLayout,QGroupBox,QVBoxLayout,QLabel

class DashboardCards(QWidget):
    def __init__(self):
        super().__init__()
        self.labels={}
        layout=QGridLayout(self)
        for i,title in enumerate(["KW","Sendungen","Unternehmer","Fuhrpark"]):
            box=QGroupBox(title); bl=QVBoxLayout(box)
            lbl=QLabel("-"); lbl.setStyleSheet("font-size:24px;font-weight:bold;")
            self.labels[title]=lbl; bl.addWidget(lbl)
            layout.addWidget(box,i//2,i%2)
    def update_stats(self,stats):
        self.labels["KW"].setText(str(stats.get("week","-")))
        self.labels["Sendungen"].setText(str(stats.get("shipments",0)))
        self.labels["Unternehmer"].setText(str(stats.get("entrepreneurs",0)))
        self.labels["Fuhrpark"].setText(str(stats.get("fleet",0)))
