class FamilyMember:
    def __init__(self, name, schizophrenia, blindness, hard_of_hearing):
        self.name = name
        self.schizophrenia = schizophrenia
        self.blindness = blindness
        self.hard_of_hearing = hard_of_hearing

class User:
    def __init__(self, name):
        self.name = name
        self.family = []

    def add_family_member(self, name, schizophrenia, blindness, hard_of_hearing):
        self.family.append(FamilyMember(name, schizophrenia, blindness, hard_of_hearing))

    def check_family_history(self):
        schizophrenia_count = sum([member.schizophrenia for member in self.family])
        blindness_count = sum([member.blindness for member in self.family])
        hard_of_hearing_count = sum([member.hard_of_hearing for member in self.family])

        print(f"In {self.name}'s family history:")
        print(f"Schizophrenia cases: {schizophrenia_count}")
        print(f"Blindness cases: {blindness_count}")
        print(f"Cases of Hard of Hearing: {hard_of_hearing_count}")

# Usage
user = User("John")
user.add_family_member("Mother", schizophrenia=True, blindness=False, hard_of_hearing=False)
user.add_family_member("Father", schizophrenia=False, blindness=True, hard_of_hearing=False)
user.add_family_member("Grandfather", schizophrenia=False, blindness=False, hard_of_hearing=True)

user.check_family_history()
