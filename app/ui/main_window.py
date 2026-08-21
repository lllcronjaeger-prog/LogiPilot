
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt,QDate
from app.imports.detector import detect,available_weeks

class DropArea(QFrame):
    def __init__(self,cb):
        super().__init__()
        self.cb=cb; self.setAcceptDrops(True); self.setMinimumHeight(170)
        self.setStyleSheet("QFrame{border:2px dashed #f97316;border-radius:12px;background:#111827;} QLabel{color:white;font-size:18px;}")
        l=QVBoxLayout(self); self.lab=QLabel("📂 Datei hier ablegen\n(DispoTest oder Speditionsbuch)"); self.lab.setAlignment(Qt.AlignCenter); l.addWidget(self.lab)
    def dragEnterEvent(self,e):
        if e.mimeData().hasUrls(): e.acceptProposedAction()
    def dropEvent(self,e):
        if e.mimeData().hasUrls(): self.cb(e.mimeData().urls()[0].toLocalFile())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle("LogiPilot v0.3.2"); self.resize(1380,840)
        root=QWidget(); self.setCentralWidget(root); h=QHBoxLayout(root); h.setContentsMargins(0,0,0,0)
        side=QFrame(); side.setFixedWidth(240); side.setStyleSheet("background:#16233b;color:white;")
        sv=QVBoxLayout(side); t=QLabel("LogiPilot"); t.setStyleSheet("font-size:24px;font-weight:bold;color:#f97316;padding:18px;"); sv.addWidget(t)
        wk=QFrame(); wk.setStyleSheet("background:#f97316;border-radius:10px;color:white;"); wv=QVBoxLayout(wk); wv.addWidget(QLabel(f"KW {QDate.currentDate().weekNumber()[0]}")); wv.addWidget(QLabel("Bereit für Import")); sv.addWidget(wk)
        [sv.addWidget(QPushButton(x)) for x in ["Dashboard","Historie","Unternehmer","Fuhrpark","Einstellungen"]]; sv.addStretch(); h.addWidget(side)
        main=QWidget(); mv=QVBoxLayout(main); mv.setContentsMargins(24,24,24,24)
        top=QHBoxLayout(); top.addWidget(QLabel("<h1>Dashboard</h1>")); top.addStretch(); b=QPushButton("📂 Datei auswählen"); b.clicked.connect(self.pick); b.setStyleSheet("background:#f97316;color:white;padding:10px;border-radius:8px;"); top.addWidget(b); mv.addLayout(top)
        self.drop=DropArea(self.import_file); mv.addWidget(self.drop)
        self.info=QLabel("Noch keine Datei ausgewählt."); mv.addWidget(self.info)
        self.combo=QComboBox(); self.combo.hide(); mv.addWidget(self.combo)
        self.diag=QTextEdit(); self.diag.setReadOnly(True); self.diag.setMaximumHeight(140); mv.addWidget(self.diag)
        h.addWidget(main); self.setStyleSheet("QMainWindow{background:#0f172a;} QLabel{color:white;} QTextEdit{background:#111827;color:white;border-radius:8px;} QPushButton{background:#243b63;color:white;border:none;padding:8px;border-radius:6px;} QPushButton:hover{background:#355285;}")
    def pick(self):
        f,_=QFileDialog.getOpenFileName(self,"Datei","","Excel (*.xls *.xlsx)")
        if f:self.import_file(f)
    def import_file(self,f):
        det=detect(f); weeks,header,col=available_weeks(f,det)
        self.info.setText(f"Quelle: {det.source}\nDatei: {f.split('/')[-1]}")
        self.combo.clear(); self.combo.addItems(weeks or ["Keine KW gefunden"]); self.combo.show()
        self.diag.setPlainText(f"Importdiagnose\nDatei: {f.split('/')[-1]}\nQuelle: {det.source}\nBlatt: {det.sheet}\nKopfzeile: {header}\nDatumsspalte: {col}\nKalenderwochen: {', '.join(weeks) if weeks else 'Keine'}")
