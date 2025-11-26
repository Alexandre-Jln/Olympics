"""CLI public options."""

import argparse

from . import cli

parser = argparse.ArgumentParser(
    prog='olympics',
    description='Display various information about Olympics results',
)
parser.add_argument(
    'command',
    help='command to launch',
    choices=('countries', 'collective', 'individual', 'discipline'),
)
parser.add_argument(
    '--top',
    help='number of top elements to display',
    type=int,
    default=10,
)
parser.add_argument(
    '--discipline-id',
    help='discipline ID for discipline top command',
    type=int,
)

def main(argv=None):
    args = parser.parse_args(argv)
    if (top := args.top) <= 0:
        raise argparse.ArgumentTypeError(f'{top} is not a positive number')
    match args.command:
        case 'countries':
            cli.top_countries(top)
        case 'collective':
            cli.top_collective(top)
        case 'individual':
            cli.top_individual(top)
        case 'discipline':
            if args.discipline_id is None:
                raise ValueError("You must specify --discipline-id for 'discipline' command")
            cli.top_countries_by_discipline(args.discipline_id, top)

if __name__ == '__main__':  # pragma: no cover
    main()
