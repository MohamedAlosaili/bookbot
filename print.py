class Print:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    def normal(self, text = ""):
        print(text)

    def error(self, text):
        print(Print.FAIL +text+ Print.ENDC)

    def warning(self, text):
        print(Print.WARNING +text+ Print.ENDC)

    def info(self, text):
        print(Print.OKBLUE +text+ Print.ENDC)

    def fancy(self, text):
        print(Print.OKCYAN +text+ Print.ENDC)

    def bold(self, text):
        print(Print.BOLD +text+ Print.ENDC)

