from typing import List, Optional

import inquirer


class Colors:
    green = "\033[92m"
    red = "\033[31m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[96m"
    reset = "\033[0m"
    bold = "\033[1m"


class Text:
    def __init__(self, text: str):
        self._text = text

    def text(self):
        print(f"{Colors.reset}[{Colors.yellow}?{Colors.reset}] {self._text}")


class Field:
    def __init__(self, name: str, value: Optional[str] = None):
        self.name = name
        self.value = value

    def ask(self):
        if self.value:
            user = input(
                f"{Colors.reset}[{Colors.yellow}?{Colors.reset}] {self.name} {Colors.green}[{self.value}]{Colors.reset}{Colors.bold} "
            )
        else:
            user = input(
                f"{Colors.reset}[{Colors.yellow}?{Colors.reset}] {self.name}{Colors.bold} "
            )

        return user


class Checkbox:
    def __init__(self, name: str, question: str):
        self.name = name
        self.question = question

    def ask(self):
        question = inquirer.Checkbox(
            name=self.name, message=self.name, choices=[(self.question, "")]
        )
        return True if inquirer.prompt([question])[self.name] else False


class Select:
    def __init__(self, name: str, question: str, options: list):
        self.name = name
        self.question = question
        self.options = options

    def ask(self):
        question = inquirer.Checkbox(
            name=self.name, message=self.question, choices=self.options
        )
        return inquirer.prompt([question])[self.name]


class Radio:
    def __init__(self, name: str, question: str, options: list):
        self.name = name
        self.question = question
        self.options = options

    def ask(self):
        question = inquirer.List(
            name=self.name, message=self.question, choices=self.options
        )
        return inquirer.prompt([question])[self.name]


class Password:
    def __init__(self, name: str, mask: str = "*"):
        self.name = name
        self.mask = mask

    def ask(self):
        question = inquirer.Password(
            name=self.name,
            message=self.name,
            echo="*" if self.mask is None else self.mask,
        )
        return inquirer.prompt([question])[self.name]


class Submit:
    def __init__(self, name: str):
        self.name = name

    def ask(self):
        input(
            f"[{Colors.yellow}?{Colors.reset}] [{Colors.red}{self.name}{Colors.reset}]"
        )


class Form:
    def __init__(
        self,
        title: str,
        description: str,
        content: List[Text | Field | Select | Radio | Password | Submit],
    ):
        self.title = title
        self.description = description
        self.content = content
        self.answers = {}

    def show(self):
        print(f"{Colors.bold}{self.title}{Colors.reset}")
        print(self.description + "\n")

        for item in self.content:
            if isinstance(item, Text):
                item.text()
            elif (
                isinstance(item, Field)
                or isinstance(item, Checkbox)
                or isinstance(item, Select)
                or isinstance(item, Radio)
                or isinstance(item, Password)
                or isinstance(item, Submit)
            ):
                self.answers[item.name] = item.ask()

    def get_all(self):
        return self.answers

    def get(self, name: str):
        return self.answers[name]

    def set(self, name: str, value: str):
        self.answers[name] = value

    def clear(self):
        self.answers = {}
