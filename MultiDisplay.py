from dataclasses import dataclass


@dataclass
class MultiDisplay:
    message: str = "Hello World!"
    count: int = 1

    def get_message(self):
        return self.message

    def get_count(self):
        return self.count

    def set_message(self, s):
        self.message = s

    def set_count(self, num):
        self.count = num

    def to_string(self):
        return "Message: " + self.message + ", Count: " + str(self.count)

    def display(self):
        for i in range(0, self.count):
            print(self.message)

    def set_display(self, s, num):
        self.message = s
        self.count = num
        print(self.display())
