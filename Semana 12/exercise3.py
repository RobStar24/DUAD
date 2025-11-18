class Husband:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working...")

    def do_housework(self):
        print(f"{self.name} is doing household chores...")


class ImpostorSyndrome:
    def __init__(self, name):
        self.name = name

    def feel_insecure(self):
        print(
            f"{self.name} feels like a fraud. He thinks he's not good enough at what he does."
        )


class Student:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def study(self):
        print(f"{self.name} is studying {self.subject}...")

    def procrastinate(self):
        print(
            f"{self.name} is procrastinating. He studies Python, but can't help watching cat memes!"
        )


class Carlos(Husband, ImpostorSyndrome, Student):
    def __init__(self, name, subject):
        Husband.__init__(self, name)
        ImpostorSyndrome.__init__(self, name)
        Student.__init__(self, name, subject)

    def daily_routine(self):
        self.work()
        self.do_housework()
        self.feel_insecure()
        self.procrastinate()
        self.study()


carlos = Carlos("Carlos", "Programming")
carlos.daily_routine()
