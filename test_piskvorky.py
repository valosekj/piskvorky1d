# Run this script in terminal:  python -m pytest -vs test_piskvorky.py
# (option -s for pytest has to be included to allow input)

from piskvorky import tah_hrace

def test_tah_hrace():
    assert tah_hrace('-------', 'x') == 'x------'

