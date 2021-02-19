import argparse

def run():
    parser = argparse.ArgumentParser(description='Grapple CLI tool')
    parser.add_argument('-p', '--playbook', help='Playbook to run', type=str, choices=['foo', 'bar'], required=True)
    parser.add_argument('-c', help='Config file to use', type=str)

    args = parser.parse_args()
    print(args)
