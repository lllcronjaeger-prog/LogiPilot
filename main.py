
import sys
from app.database.migrate import run_migrations
from PySide6.QtWidgets import QApplication
from app.database.database import init_db
from app.config.settings import load
from app.ui.main_window import MainWindow
run_migrations()
init_db(); load(); app=QApplication(sys.argv); w=MainWindow(); w.show(); sys.exit(app.exec())
