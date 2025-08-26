class Head:
    def __init__(self, eyes=2, mouth=1, nose=1):
        self.eyes = eyes
        self.mouth = mouth
        self.nose = nose

    def __str__(self):
        return f"Head with {self.eyes} eyes, {self.mouth} mouth, {self.nose} nose"


class Torso:
    def __init__(self, heart=True, lungs=2):
        self.heart = heart
        self.lungs = lungs

    def __str__(self):
        return f"Torso with heart: {self.heart}, lungs: {self.lungs}"


class Arm:
    def __init__(self, side):
        self.side = side
        self.hand = Hand()

    def __str__(self):
        return f"{self.side} arm with hand"


class Hand:
    def __init__(self, fingers=5):
        self.fingers = fingers

    def __str__(self):
        return f"Hand with {self.fingers} fingers"


class Leg:
    def __init__(self, side):
        self.side = side
        self.feet = Feet()

    def __str__(self):
        return f"{self.side} leg with foot"


class Feet:
    def __init__(self, toes=5):
        self.toes = toes

    def __str__(self):
        return f"Foot with {self.toes} toes"


class Human:
    def __init__(self, name):
        self.name = name
        self.head = Head()
        self.torso = Torso()
        self.left_arm = Arm("Left")
        self.right_arm = Arm("Right")
        self.left_leg = Leg("Left")
        self.right_leg = Leg("Right")

    def __str__(self):
        return (
            f"Human: {self.name}\n"
            f" - {self.head}\n"
            f" - {self.torso}\n"
            f" - {self.left_arm}\n"
            f" - {self.right_arm}\n"
            f" - {self.left_leg}\n"
            f" - {self.right_leg}"
        )


person = Human("Android No.18")
print(person)
