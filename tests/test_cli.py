from io import StringIO

from olympics import cli


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
