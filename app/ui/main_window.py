import re
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QDate
from app.imports.detector import detect, available_weeks
from app.reports.excel_reports import create_reports
import re

class DropArea(QFrame):
    def __init__(self, cb):
        super().__init__()
        self.cb = cb
        self.setAcceptDrops(True)
        self.setMinimumHeight(140)
        self.setStyleSheet("QFrame{border:2px dashed #f97316;border-radius:12px;background:#111827;} QLabel{color:white;font-size:16px;}")
        l=QVBoxLayout(self)
        self.lab=QLabel("📂 Datei hier ablegen\n(DispoTest oder Speditionsbuch)")
        self.lab.setAlignment(Qt.AlignCenter)
        l.addWidget(self.lab)
    def dragEnterEvent(self,e):
        if e.mimeData().hasUrls(): e.acceptProposedAction()
    def dropEvent(self,e):
        if e.mimeData().hasUrls(): self.cb(e.mimeData().urls()[0].toLocalFile())

class Card(QFrame):
    def __init__(self,title,value="-"):
        super().__init__()
        self.setStyleSheet("QFrame{background:#16233b;border-radius:10px;} QLabel{color:white;}")
        l=QVBoxLayout(self)
        l.addWidget(QLabel(title))
        self.val=QLabel(str(value))
        self.val.setStyleSheet("font-size:26px;font-weight:bold;color:#f97316;")
        l.addWidget(self.val)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LogiPilot v1.0 – Disponentenansicht")
        self.resize(1500,900)

        root=QWidget(); self.setCentralWidget(root)
        h=QHBoxLayout(root); h.setContentsMargins(0,0,0,0)

        side=QFrame(); side.setFixedWidth(240)
        side.setStyleSheet("background:#16233b;color:white;")
        sv=QVBoxLayout(side)
        t=QLabel("LogiPilot"); t.setStyleSheet("font-size:24px;font-weight:bold;color:#f97316;padding:18px;")
        sv.addWidget(t)
        for txt in ["🏠 Dashboard","📦 Import","📅 Wochen","🚛 Fuhrpark","👥 Unternehmer","⚙ Einstellungen"]:
            sv.addWidget(QPushButton(txt))
        sv.addStretch()
        h.addWidget(side)

        main=QWidget(); mv=QVBoxLayout(main); mv.setContentsMargins(24,24,24,24)

        top=QHBoxLayout()
        top.addWidget(QLabel("<h1>Disponentenansicht</h1>"))
        top.addStretch()
        pick=QPushButton("📂 Datei auswählen")
        pick.clicked.connect(self.pick)
        pick.setStyleSheet("background:#f97316;color:white;padding:10px;border-radius:8px;")
        top.addWidget(pick)
        self.report_btn=QPushButton("📊 Excel-Auswertungen")
        self.report_btn.setEnabled(False)
        self.report_btn.clicked.connect(self.make_reports)
        top.addWidget(self.report_btn)
        mv.addLayout(top)

        cards=QGridLayout()
        self.c_kw=Card("Aktive KW",QDate.currentDate().weekNumber()[0])
        self.c_ship=Card("Sendungen",0)
        self.c_ent=Card("Unternehmer",0)
        self.c_fleet=Card("Fuhrpark",0)
        cards.addWidget(self.c_kw,0,0); cards.addWidget(self.c_ship,0,1)
        cards.addWidget(self.c_ent,1,0); cards.addWidget(self.c_fleet,1,1)
        mv.addLayout(cards)

        self.tabs=QTabBar()
        current=QDate.currentDate().weekNumber()[0]
        for kw in range(max(1,current-2),current+3):
            self.tabs.addTab(f"KW {kw}")
        mv.addWidget(self.tabs)

        self.drop=DropArea(self.import_file); mv.addWidget(self.drop)

        self.info=QLabel("Noch keine Datei ausgewählt."); mv.addWidget(self.info)

        self.combo=QComboBox(); self.combo.hide(); mv.addWidget(self.combo)

        self.table=QTableWidget(0,4)
        self.table.setHorizontalHeaderLabels(["Kennzeichen","Unternehmer","Sendungen","Status"])
        mv.addWidget(self.table,1)

        self.diag=QTextEdit(); self.diag.setReadOnly(True); self.diag.setMaximumHeight(120); mv.addWidget(self.diag)

        h.addWidget(main)
        self.setStyleSheet("QMainWindow{background:#0f172a;} QLabel{color:white;} QTextEdit{background:#111827;color:white;border-radius:8px;} QPushButton{background:#243b63;color:white;border:none;padding:8px;border-radius:6px;} QPushButton:hover{background:#355285;}")

    def pick(self):
        f,_=QFileDialog.getOpenFileName(self,"Datei","","Excel (*.xls *.xlsx)")
        if f:self.import_file(f)

    def import_file(self,f):
        det=detect(f); weeks,header,col=available_weeks(f,det)
        self.info.setText(f"Quelle: {det.source}\nDatei: {f.split('/')[-1]}")
        self.combo.clear(); self.combo.addItems(weeks or ["Keine KW gefunden"]); self.combo.show()
        self.c_kw.val.setText(weeks[0] if weeks else "-")
        self.last_file=f
        self.report_btn.setEnabled(True)
        self.diag.setPlainText(f"Importdiagnose\nDatei: {f.split('/')[-1]}\nQuelle: {det.source}\nBlatt: {det.sheet}\nKopfzeile: {header}\nDatumsspalte: {col}\nKalenderwochen: {', '.join(weeks) if weeks else 'Keine'}")


    def make_reports(self):
        if not hasattr(self,'last_file'):
            return
        m=re.search(r'(\d+)', self.combo.currentText())
        if not m:
            return
        out=create_reports(self.last_file,int(m.group(1)))
        QMessageBox.information(self,'Excel-Auswertungen',f'Erstellt:\n{out}')
