from datetime import datetime

def create_import_id(year:int, week:int, sequence:int)->str:
    return f"IMP-{year}-{week:02d}-{sequence:03d}"

def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
