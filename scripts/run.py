from __future__ import print_function
from subprocess import call
import os


def run():
    if not os.path.exists('../conf/osdev.bochsrc'):
        raise Exception('Missing bochs config!')

    if not os.path.exists('../bin/floppy.bin'):
        raise Exception("Missing disk image.\nYou should run 'python manage.py build' first.")

    print("Running bochs...")
    if call('bochs -f "../conf/osdev.bochsrc"', shell=True) is not 0:
        raise Exception("Error running bochs...")
