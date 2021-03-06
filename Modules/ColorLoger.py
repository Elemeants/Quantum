import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

class Loger:
    # DEFINITIONS STYLE TEXT
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'
    # DEFINITIONS COLOR TEXT
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'
    # DEFINITIONS COLOR TEXT 2
    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'
    # DEFINITIONS COLOR BACKGROUND
    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'
    # DEFINITIONS COLOR BACKGROUND 2
    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'

    DEFAULT = "[" + CBOLD + "{2}{0}" + CEND + "] {3}{1}" + CEND
    ERROR = CRED2
    OK = CGREEN2
    WARNING = CVIOLET2
    NORMAL = CYELLOW2
    INFO = CBLUE2

    @staticmethod
    def Error(Message: str):
        print(Loger.DEFAULT.format("ERROR", Message, Loger.ERROR, Loger.NORMAL))

    @staticmethod
    def Ok(Message: str):
        print(Loger.DEFAULT.format("OK", Message, Loger.OK, Loger.NORMAL))

    @staticmethod
    def Warning(Message: str):
        print(Loger.DEFAULT.format("WARNING", Message, Loger.WARNING, Loger.NORMAL))

    @staticmethod
    def Info(Message: str):
        print(Loger.DEFAULT.format("INFO", Message, Loger.INFO, Loger.NORMAL))

    @staticmethod
    def Help(Message: str):
        print("{1}{0}{2}".format(Message, Loger.NORMAL, Loger.CEND))
