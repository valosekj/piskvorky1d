# Replace user input by monkeypatch
# Inspiration - https://www.linuxjournal.com/content/testing-your-code-pythons-pytest-part-ii

from piskvorky import tah_hrace
from io import StringIO

# create object simulating user input (\n - has to be included - it simulates new line)
mock_input = StringIO('0\n')

def test_tah_hrace(monkeypatch):

    # replace user input
    monkeypatch.setattr('sys.stdin',mock_input)

    assert tah_hrace('-------', 'x') == 'x------'

