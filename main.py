from collections import namedtuple

Command = namedtuple('Command', ['function', 'args'])
known_commands = {}

def get_command():

    c, *args = input('> ').split()
    command = Command(c, args)

    return command


def main():

    running = True;
    while running:
        try:
            c = get_command()

            if c.function in known_commands:
                known_commands[c.function](c.args)
            else:
                print('Unknown command: {} {}'.format(c.function, c.args))

        except (EOFError, KeyboardInterrupt):
            running = False

    print('\nExiting...')


if __name__ == '__main__':
    main()

