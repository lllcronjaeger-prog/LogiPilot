from PySide6.QtWidgets import QWidget,QHBoxLayout,QTableView
from app.ui.filter_panel import FilterPanel
from app.ui.pandas_model import PandasModel

class WeekView(QWidget):
    def __init__(self, dataframe):
        super().__init__()
        self.df=dataframe.copy()
        self.filtered=self.df.copy()
        layout=QHBoxLayout(self)
        self.table=QTableView()
        self.table.setModel(PandasModel(self.filtered))
        self.table.setSortingEnabled(True)
        layout.addWidget(self.table,4)
        self.filters=FilterPanel()
        self.filters.filtersChanged.connect(self.apply_filters)
        layout.addWidget(self.filters,1)
        if "Unternehmer" in self.df.columns:
            self.filters.set_entrepreneurs(sorted(self.df["Unternehmer"].dropna().unique()))
        self.filters.set_status(len(self.filtered),len(self.df))
    def apply_filters(self):
        selected=self.filters.selected_entrepreneurs()
        df=self.df
        if "Unternehmer" in df.columns and selected:
            df=df[df["Unternehmer"].isin(selected)]
        self.filtered=df.copy()
        self.table.setModel(PandasModel(self.filtered))
        self.filters.set_status(len(self.filtered),len(self.df))
