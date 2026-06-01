'''
запуск
'''

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../lab05"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../lab06"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from cli import CLI


if __name__ == "__main__":
    cli = CLI()

    cli.run()