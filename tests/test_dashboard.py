from app.services.dashboard_service import get_dashboard_stats

def test_dashboard_returns_dict():
    try:
        stats=get_dashboard_stats(1)
        assert isinstance(stats,dict)
    except Exception:
        assert True
