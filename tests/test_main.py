from olympics.__main__ import main


def test_countries():
    argv = ['countries']
    main(argv)

def test_main_discipline():
    argv = ['discipline', '--discipline-id', '3', '--top', '5']
    main(argv)
