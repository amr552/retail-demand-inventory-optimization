import platform
import sys

def check_environment():


    print('checking project environment ...')
    print(f'python version: {platform.python_version()}')
    print(f'python system: {platform.system()}')
    print(f'python excutable: {sys.executable}')
    print('project environment is ready')


if __name__ == '__main__':
    check_environment()