from collections import namedtuple
import os

Command = namedtuple('Command', ['function', 'args'])
known_commands = {}

def parse_command_list():

    files = []

    for i in os.listdir('./Commands'):
        if i[0] != '_' and i[0] != '.' and i[-3:] == '.py':
            files.append(i)

    s = '### Begin Auto-generated Code ###\n'
    for i in files:
        s += 'import Commands.{}\n'.format(i[:-3])

    s += '\ncommands = {}\n'
    for i in files:
        s += 'commands[\'{0}\'] = {0}.main\n'.format(i[:-3])

    with open('Commands/__init__.py', 'w') as f:
        f.write('{}\n'.format(s))


    global known_commands

    import Commands
    known_commands = Commands.commands


def get_command():

    c, *args = input('> ').split()
    command = Command(c, args)

    return command


def main():

    global known_commands
    parse_command_list()

    running = True
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
