import pytest
from secteni import secti

def test_secti():
    """Otestuje funkci secti"""
    assert secti(1, 2) == 4

def test_spatneho_tahu():
    """🤘 vs. 🖖 není správný vstup"""
    with pytest.raises(ValueError):
        vyhodnot('metal', 'spock')