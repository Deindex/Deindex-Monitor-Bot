from src.monitor.robots_checker import check_robots


def test_function_exists():
    assert callable(check_robots)
