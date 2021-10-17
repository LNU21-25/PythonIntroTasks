from dataclasses import dataclass


@dataclass
class Name:
    first: str = "John"
    last: str = "Doe"

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def set_first(self, str):
        self.first = str

    def set_last(self, str):
        self.last = str

    def to_string(self):
        return self.first + self.last

    def get_short_name(self):
        return self.first[0] + ". " + self.last
