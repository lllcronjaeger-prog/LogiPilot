from app.database.database import connect

def get_fleet_plates():
 con=connect(); cur=con.cursor(); cur.execute('SELECT kennzeichen FROM fleet_vehicles WHERE aktiv=1'); r={x[0].strip().upper() for x in cur.fetchall()}; con.close(); return r
