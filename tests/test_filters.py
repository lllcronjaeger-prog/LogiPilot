from app.services.fleet_service import get_fleet_plates

def test_set(): assert isinstance(get_fleet_plates(),set)
