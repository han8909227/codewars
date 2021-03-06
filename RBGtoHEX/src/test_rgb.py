import pytest


@pytest.mark.parametrize('r, g, b, result', [(0, 0, 0, '000000'), (1, 2, 3, '010203'),
    (255, 255, 255, 'FFFFFF'), (254, 253, 252, 'FEFDFC'), (-20, 275, 125, '00FF7D'),
    (90, 41, 52, '5A2934'), (50, 185, 177, "32B9B1")])
def test_rgb(r, g, b, result):
    """."""
    from rgb import rgb
    assert rgb(r, g, b) == result
