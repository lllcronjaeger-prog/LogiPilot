
from PySide6.QtCore import Qt, QAbstractTableModel

class PandasModel(QAbstractTableModel):
    def __init__(self, dataframe):
        super().__init__()
        self.df=dataframe

    def rowCount(self,parent=None):
        return len(self.df.index)

    def columnCount(self,parent=None):
        return len(self.df.columns)

    def data(self,index,role=Qt.DisplayRole):
        if role==Qt.DisplayRole:
            return str(self.df.iat[index.row(), index.column()])
        return None

    def headerData(self,section,orientation,role=Qt.DisplayRole):
        if role!=Qt.DisplayRole:
            return None
        return str(self.df.columns[section]) if orientation==Qt.Horizontal else str(section+1)
