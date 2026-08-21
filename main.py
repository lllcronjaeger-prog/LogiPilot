
import sys
from PySide6.QtWidgets import QApplication
from app.database.database import init_db
from app.config.settings import load
from app.ui.main_window import MainWindow
init_db(); load(); app=QApplication(sys.argv); w=MainWindow(); w.show(); sys.exit(app.exec())
