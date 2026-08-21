from app.database.database import connect

def save_export(year:int, week:int, export_type:str, file_name:str):
    con=connect(); cur=con.cursor()
    cur.execute("INSERT INTO export_history(year,week,export_type,file_name) VALUES(?,?,?,?)",
                (year,week,export_type,file_name))
    con.commit(); con.close()
