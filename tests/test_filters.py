from app.services.fleet_service import get_fleet_plates

def test_fleet_returns_set(): assert isinstance(get_fleet_plates(), set)
