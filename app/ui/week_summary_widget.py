from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel,QTableWidget,QTableWidgetItem
from app.services.week_summary_service import create_summary

class WeekSummaryWidget(QWidget):
    def __init__(self, week:int):
        super().__init__()
        layout=QVBoxLayout(self)
        self.title=QLabel(f"Wochenübersicht KW {week}")
        self.table=QTableWidget()
        layout.addWidget(self.title)
        layout.addWidget(self.table)
        self.load_week(week)

    def load_week(self, week:int):
        data=create_summary(week)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["Kennzeichen","Unternehmer","Sendungen","Umsatz"]
        )
        self.table.setRowCount(len(data))
        for r,row in enumerate(data):
            for c,val in enumerate(row):
                self.table.setItem(r,c,QTableWidgetItem(str(val)))
