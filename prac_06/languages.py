"""
language program file
Estimate: 30 minutes
Actual:   35 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
