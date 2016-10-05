"""Resolvewang

Usage:
    pc_shutdow.py name <name> password <password>
    pc_shutdow.py (-h | --help)
    pc_shutdow.py --version

Options:
    -h --help   Show this screen.
    --version   Show version.
"""

from login import get_cur_session
from weibo_parser import get_newest
from docopt import docopt
from os import system
import platform


def shutdown(name, password):
    session, uid = get_cur_session(name, password)
    return get_newest(session, uid)


if __name__ == '__main__':
    args = docopt(__doc__, version='ShutdownMyPC 1.0')
    login_name = args.get('<name>')
    login_pass = args.get('<password>')
    cont, ptdelta = shutdown(login_name, login_pass)
    info = cont.split(' ')

    if info[0] == '关机' and ptdelta < 30 * 60:
        shut_time = 0
        try:
            shut_time = int(info[1])
        except Exception:
            print('马上自动关机')
        else:
            print('{time}分钟后自动关机'.format(time=info[1]))
        finally:
            os_system = platform.system().lower()
            if os_system == 'windows':
                command = 'shutdown -s -t {shut_time}'.format(shut_time=shut_time*60)
            else:
                command = 'shutdown -h {shut_time}'.format(shut_time=shut_time)
            system(command)
