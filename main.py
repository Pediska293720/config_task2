import sys

def parse_arguments():
    args = {'package': None,
            'url': None,
            'test_mode': False,
            'output_file': "default_graf.png",
            'depth': 2,
            'filter': None}

    if "--package" in sys.argv:
        idx = sys.argv.index('--package')
        if idx + 1 < len(sys.argv):
            args['package'] = sys.argv[idx + 1]

    if "--url" in sys.argv:
        idx = sys.argv.index('--url')
        if idx + 1 < len(sys.argv) and not sys.argv[idx + 1].startswith('--'):
            args['url'] = sys.argv[idx + 1]
        else:
            print("Error: no value for url\n")
            sys.exit(1)
    if "--test_mode" in sys.argv:
        args['test_mode'] = True

    if "--output_file" in sys.argv:
        idx = sys.argv.index('--output_file')
        if idx + 1 < len(sys.argv) and not sys.argv[idx + 1].startswith('--'):
            args['output_file'] = sys.argv[idx + 1]
        else:
            print("Error: no name for output file\n")
            sys.exit(1)
    if "--depth" in sys.argv:
        idx = sys.argv.index('--depth')
        if idx + 1 < len(sys.argv) and not sys.argv[idx + 1].startswith('--'):
            try:
                args['depth'] = int(sys.argv[idx + 1])
            except ValueError:
                print("Error: depth should be integer value\n")
                sys.exit(1)
        else:
            print("Error: no value for depth\n")
            sys.exit(1)
    if "--filter" in sys.argv:
        idx = sys.argv.index('--filter')
        if idx + 1 < len(sys.argv) and not sys.argv[idx + 1].startswith('--'):
            args['filter'] = sys.argv[idx + 1]
        else:
            print("Error: no value for filter\n")
            sys.exit(1)
    return args

def main():
    arguments = parse_arguments()
    if arguments['package'] == None:
        print("Error: no value for package")
        return

    for key, value in arguments.items():
        print(f'{key}: {value}')



if __name__ == "__main__":
    main()
