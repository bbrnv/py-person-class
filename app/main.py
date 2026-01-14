class Person:
    people: dict[str, "Person"] = {}  # class attribute to store all instances

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    # Step 1: Create all Person instances
    for person in people:
        person_obj = Person(person["name"], person["age"])
        person_list.append(person_obj)

    # Step 2: Link wife/husband attributes
    for person in people:
        current = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            current.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            current.husband = Person.people[person["husband"]]

    return person_list
