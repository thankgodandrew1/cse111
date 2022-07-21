from calculator import square_root, cone_volume, density, calc_molarity, wind_chill_calculator, \
    area_trapezoid
from pytest import approx
import pytest

def test_square_root():
    """verify that the square_root function works very well
    Parameters: None
    Returns: nothing
    """    
    assert square_root(12) == approx(3.46, 0.1)
    assert square_root(6) == approx(2.45, 0.1)
    assert square_root(50) == approx(7.1, 0.1)
    assert square_root(3) == approx(2, 1)
    assert square_root(350) == approx(19, 0.1)


def test_cone_volume():
    """verify that the cone_volume function works very well
    Parameters: None
    Returns: nothing
    """    

    assert cone_volume(12, 15) == approx(2262, 0.1)
    assert cone_volume(7, 4) == approx(205.3, 0.1)
    assert cone_volume(111, 118) == approx(1522497.48, 1)

def test_density():
    """verify that the density function works very well
    Parameters: None
    Returns: nothing
    """    
    assert density(50, 100) == approx(0.5, 0.1)
    assert density(10, 5) == approx(2, 0.1)
    assert density(150, 130) == approx(1.2, 0.1)
    assert density(1000, 1200) == approx(1, 1)

def test_molarity():
    """verify that the molarity function works very well
    Parameters: None
    Returns: nothing
    """    
    assert calc_molarity(30, 2) == approx(15, 0.01)
    assert calc_molarity(0.8, 3) == approx(0.3, 1)
    assert calc_molarity(10, 100) == approx(0.1)

def test_wind_chill():
    """verify that the wind_chill function works very well
    Parameters: None
    Returns: nothing
    """ 
    
    assert wind_chill_calculator(12, 5) == approx(3.584, 0.01)
    assert wind_chill_calculator(29, 18) == approx(16.7, 0.01)
    assert wind_chill_calculator(2, 30) == approx(-23.15, 0.01)
    assert wind_chill_calculator(-10, 10) == approx(-28.33, 0.01)

def test_arae_trapezoid():
    """verify that the area_trapezoid function works very well
    Parameters: None
    Returns: nothing
    """ 
    assert area_trapezoid(5, 7, 8) == approx(48)
    assert area_trapezoid(10, 12, 17) == approx(187)
    assert area_trapezoid(25.5, 24.3, 29) == approx(722.1, 0.1)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
