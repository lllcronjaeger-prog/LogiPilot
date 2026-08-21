from openpyxl.styles import Font, PatternFill

HEADER_FILL=PatternFill(fill_type="solid", fgColor="1F4E78")
HEADER_FONT=Font(bold=True, color="FFFFFF")

def style_header(row):
    for cell in row:
        cell.fill=HEADER_FILL
        cell.font=HEADER_FONT
