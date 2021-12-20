'''
To run these unit tests only:
pytest tests/unit
'''
import sys
sys.path.append('path to your directory')
import source

def test_add_numbers():
    assert source.add_numbers(2, 2) == 4, 'Should be 4'

def test_subtract_numbers():
    assert source.subtract_numbers(2, 2) == 0, 'Should be 0'

if __name__ == '__main__':
    test_add_numbers()
    test_subtract_numbers()
