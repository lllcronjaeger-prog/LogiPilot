# Patch für main_window.py

Nach erfolgreichem Import kann später dieser Aufruf ergänzt werden:

```python
from app.ui.export_dialog import export_week_dialog

# Beispiel:
# export_week_dialog(self, selected_week)
```

Diese Datei überschreibt bewusst keine bestehende main_window.py.
