from src.monitor.index_checker import check_url


def test_function_exists():
    assert callable(check_url)
