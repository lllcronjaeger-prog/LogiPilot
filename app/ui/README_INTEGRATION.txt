In app/ui/main_window.py:

1. Import ergänzen:
   from app.reports.excel_reports import create_reports, available_weeks

2. Button '📊 Excel-Auswertungen' ruft auf:
   create_reports(self.last_file, self.selected_kw)

3. self.selected_kw wird aus der KW-Combo gesetzt.
