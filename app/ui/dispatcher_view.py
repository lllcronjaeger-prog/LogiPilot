from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QTabBar,QPushButton,QLabel
from app.ui.week_summary_widget import WeekSummaryWidget

class DispatcherView(QWidget):
    def __init__(self, week=1):
        super().__init__()
        layout=QVBoxLayout(self)
        top=QHBoxLayout()
        self.tabs=QTabBar()
        for kw in range(max(1,week-2), week+3):
            self.tabs.addTab(f"KW {kw}")
        top.addWidget(self.tabs)
        top.addStretch()
        self.export_btn=QPushButton("Excel exportieren")
        top.addWidget(self.export_btn)
        layout.addLayout(top)
        self.status=QLabel("Disponentenansicht")
        layout.addWidget(self.status)
        self.summary=WeekSummaryWidget(week)
        layout.addWidget(self.summary)
