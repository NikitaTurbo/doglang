import textwrap

class DogLangInterpreter:
    def __init__(self):
        self.variables = {}
        self.commands = {
            'гав': 'print',
            'Гав': 'input',
            'рррр': 'if',
            'тяв': 'else',
            'гав-гав': 'while',
            'мяу': '==',
            'мур': '!=',
            'хрю': '<',
            'хнык': '>',
            'фыр': '>=',
            'соп': '<=',
            'ауф': 'and',
            'уф': 'or',
            'фу': 'not',
            'ням': '+',
            'ам': '-',
            'ням-ням': '*',
            'ам-ам': '/',
            'собака': '='
        }

    def translate(self, code):
        code = textwrap.dedent(code)
        lines = code.splitlines()
        new_lines = []
        sorted_commands = sorted(self.commands, key=len, reverse=True)
        for line in lines:
            indent = line[:len(line) - len(line.lstrip())]
            content = line.lstrip()
            for dog_cmd in sorted_commands:
                content = content.replace(dog_cmd, self.commands[dog_cmd])
            if content.startswith("print") and not content.startswith("print("):
                if content.startswith("print "):
                    content = "print(" + content[6:].strip() + ")"
                else:
                    content = "print(" + content[len("print"):].strip() + ")"
            new_lines.append(indent + content)
        return "\n".join(new_lines)

    def execute(self, code):
        try:
            translated = self.translate(code)
            if '__builtins__' not in self.variables:
                self.variables['__builtins__'] = __builtins__
            exec(translated, self.variables, self.variables)
        except Exception as e:
            print(f"Ошибка: {str(e)}")

    def interactive_mode(self):
        print("Добро пожаловать в DogLang! (Введите 'выход' для завершения)")
        while True:
            try:
                code = input("гав >>> ")
                if code.lower() == "выход":
                    break
                self.execute(code)
            except KeyboardInterrupt:
                print("\nВыход из DogLang...")
                break