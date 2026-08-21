from PySide6.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QTabBar,QPushButton
from app.ui.dashboard_cards import DashboardCards
from app.ui.week_summary_widget import WeekSummaryWidget
from app.services.dashboard_service import get_dashboard_stats

class DispatcherViewV2(QWidget):
    def __init__(self,week=1):
        super().__init__()
        self.week=week
        layout=QVBoxLayout(self)
        self.cards=DashboardCards(); layout.addWidget(self.cards)
        top=QHBoxLayout()
        self.tabs=QTabBar()
        for kw in range(max(1,week-2),week+3): self.tabs.addTab(f"KW {kw}")
        self.tabs.currentChanged.connect(self._changed)
        top.addWidget(self.tabs)
        self.export_btn=QPushButton("Excel exportieren"); top.addWidget(self.export_btn)
        layout.addLayout(top)
        self.summary=WeekSummaryWidget(week); layout.addWidget(self.summary)
        self._refresh()
    def _changed(self,index):
        self.week=max(1,self.week-2)+index
        self.summary.load_week(self.week)
        self._refresh()
    def _refresh(self):
        self.cards.update_stats(get_dashboard_stats(self.week))
