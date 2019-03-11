import datetime, sys, yaml

HEADER = """
# This file was automatically generated on {timestamp}
# by script {script} from the Wikipedia English color pages.

COLORS = {{"""
FOOTER = '}'

SPECIAL_COLORS = {
    ('Peach', 0xFFCBA4): 'Deep peach',
    ('Vermilion', 0xD9381E): 'Medium vermillion',
    ('Tea rose', 0xF88379): 'Tea rose orange',
}


def get_name(color):
    name = color['name'].strip()
    if name.startswith('[['):
        name = name[2:]
    if name.endswith(']]'):
        name = name[:-2]
    return name.split('|')[-1].strip().replace("'", "\\'")


def run_all():
    timestamp = datetime.datetime.now().isoformat()
    script = sys.argv[0]
    print(HEADER.format(**locals()))
    for color in yaml.load_all(open('colors.yml')):
        name = get_name(color)
        hex = color['hex'].strip().lower()
        name = SPECIAL_COLORS.get((name, int(hex, 16)), name)
        print("    '{name}': 0x{hex},".format(**locals()))
    print(FOOTER)


if __name__ == '__main__':
    run_all()
