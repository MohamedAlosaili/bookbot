import sys
from print import Print

class CLI:
    def __init__(self, args):
        self.args = args 
        self.__flags = self.__create_flags()
        self.__available_flags = self.__get_available_flags()
        self.__command = sys.argv
        self.__print = Print()
        self.options = self.create_cli_options()

    def __create_flags(self):
        flags = [
            {
                "flag": "--help",
                "description": "Get list of available flags and brief description",
                "alias": "-h",
                "defaultValue": 'yes'
            },
            {
                "flag": "--words-count",
                "description": "Add word count in the final report. default to true set to false to remove '--words-count=false'",
                "alias": "-wc",
                "defaultValue": 'yes'
            },
            {
                "flag": "--lines-count",
                "description": "Add lines count in the final report. default to true set to false to remove '--lines-count=false'",
                "alias": "-lc",
                "defaultValue": 'yes'
            },
            {
                "flag": "--characters-count",
                "description": "Add characters count in the final report. default to true set to false to remove '--characters-count=false'",
                "alias": "-cc",
                "defaultValue": 'yes'
            },
            {
                "flag": "--target-file",
                "description": "The file to analyze",
                "alias": "-tf",
                "defaultValue": None
            }
        ]
        return flags

    def __get_available_flags(self):
        flags = []
        for flag in self.__flags:
            flags.append(flag["flag"])
            flags.append(flag["alias"])
        return flags

    def read_command(self):
        if len(self.__command) == 1:
            return
        
        if self.__command[1] in ["-h", "--help"]:
            self.show_help()
            return exit(0)

        args = self.__command[1:]

        for arg in args:
            flag = arg.split("=")
            key = flag[0]
            
            
            if key not in self.__available_flags:
                print(f"invalid flag. cannot find {arg} flag. \nrun bookbot -h to see all available flags")
                exit(1)
            
            if len(flag) < 2: continue
            
            if not key.startswith("--"):
                for f in self.__flags:
                    if f["alias"] == key:
                        key = f["flag"]
                        break 
    
            print("flag", flag)
            value = flag[1]

            self.options[key] = value


    def show_help(self):
        self.__print.info("\nWelcome to bookbot cli:\n")
        self.__print.fancy("\tbookbot [options] [FILE]\n")

        for flag in self.__flags:
            self.__print.bold(f"Flag: {flag["flag"]}, {flag["alias"]}")
            self.__print.normal(f"Description: {flag["description"]}\n")

    def create_cli_options(self):
        options = {}
        for flag in self.__flags:
            options[flag["flag"]] = flag["defaultValue"]

        return options 
        