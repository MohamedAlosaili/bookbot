from bot import Bot 
from cli import CLI 
import sys

def main():
    cli = CLI(sys.argv)
    cli.read_command()

    print("cli.options", cli.options)
    bot = Bot(cli.options)
    bot.analyze()

try:
    main()
except TypeError as e:
    print("Invalid Argument:")
    print(e)
except Exception as e:
    print("Unexpected error happened:")
    print(e)