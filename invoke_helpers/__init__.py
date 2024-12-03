import contextlib
import os
import logging

# Logging configs
# -------------------------------------------------------------------------
FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(FORMATTER)
logger.addHandler(console_handler)


class Printf:

    class Color:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

        ENDC = '\033[0m'

    @classmethod
    def header(cls, message):
        cls.print(message, color=Printf.Color.HEADER)

    @classmethod
    def info(cls, message):
        cls.print(message, color=None)

    @classmethod
    def success(cls, message):
        cls.print(message, color=Printf.Color.OKGREEN)

    @classmethod
    def warning(cls, message):
        cls.print(message, color=Printf.Color.WARNING)
    
    @classmethod
    def error(cls, message):
        cls.print(message, color=Printf.Color.FAIL)

    @staticmethod
    def print(message, color=None):
        if color:
            print(f'{color}{message}{Printf.Color.ENDC}')
        else:
            print(message)

def run(c, command, print_command=True):
    if print_command:
        Printf.header(command)
        Printf.header('-'*120)
    return c.run(command)

@contextlib.contextmanager
def on_working_dir(dirname=None):
    cwd = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(cwd)
