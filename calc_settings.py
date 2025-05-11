# Settings for the calculator in list
main_set = ("350x480", # Window size
            "ComicSansMS 15", # Default font
            "calc.ico", # Icon file
            "Comic Sans MS", # Font for input box
            "#CCCCCC", # Background color for buttons
            "#45B283", # Background color for the "=" button
            )

import ctypes
import locale
def sys_lang():
    winLang = ctypes.windll.kernel32.GetUserDefaultUILanguage()
    return locale.windows_locale[winLang]

def localization(n = 0):
    # Localization for the calculator
    local_set = ("Tkinter - Calculator 3.0", # Window title
                "Invalid input!", # Error message for invalid input
                "Division by zero!", # Error message for division by zero
                )

    if sys_lang() == "ru_RU":
        local_set = ("Tkinter - Калькулятор 3.0", # Window title
                    "Ошибка ввода!", # Error message for invalid input
                    "Деление на ноль!", # Error message for division by zero
                    )
    if n < len(local_set) and n >= 0:
        return local_set[n]
    else:
        return "Error"    