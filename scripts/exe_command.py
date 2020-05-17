import argparse
import os
import subprocess
import sys


def execute_command(command):
    """
    shell comand の実行
    """
    print(f"exceute: {command}")
    res = subprocess.run(command.split(), stdout=subprocess.PIPE) # env=env, shell=True
    if res.stdout != b'':
        print(res.stdout.decode(sys.getfilesystemencoding()), end='')
    if res.stderr != None:
        print(res.stderr, file=sys.stderr)
    if res.returncode != 0:
        print(f'returncode = {res.returncode}')


def parse_command_line_arguments():
    """
    コマンドラインの引数の受け取り
    """
    parser = argparse.ArgumentParser(description='execute command')
    parser.add_argument('command', type=str, default='', help='command')
    args = parser.parse_args()
    command = args.command
    return command


if __name__ == '__main__':
    command = parse_command_line_arguments()
    execute_command(command)