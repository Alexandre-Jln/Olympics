from io import StringIO
import pytest

from olympics import cli
from olympics.__main__ import main

def test_top_countries():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert 'Top' in text

def test_cli_top_countries_by_discipline():
    string = StringIO()
    cli.top_countries_by_discipline(3, 5, file=string)
    text = string.getvalue()
    assert 'Top' in text


def test_cli_invalid_type():
    with pytest.raises(SystemExit):
        main(["discipline", "--discipline-id", "abc"])
