from PySide6.QtCore import Qt,QAbstractTableModel
class PandasTableModel(QAbstractTableModel):
    def __init__(self,df): super().__init__(); self.df=df
    def rowCount(self,p=None): return len(self.df)
    def columnCount(self,p=None): return len(self.df.columns)
    def data(self,i,r=Qt.DisplayRole): return str(self.df.iat[i.row(),i.column()]) if r==Qt.DisplayRole else None
    def headerData(self,s,o,r=Qt.DisplayRole):
        if r!=Qt.DisplayRole: return None
        return str(self.df.columns[s]) if o==Qt.Horizontal else str(s+1)
