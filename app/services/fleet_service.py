from app.database.database import connect

def get_fleet_plates():
 c=connect();cur=c.cursor();cur.execute('SELECT kennzeichen FROM fleet_vehicles WHERE aktiv=1');r={x[0] for x in cur.fetchall()};c.close();return r
