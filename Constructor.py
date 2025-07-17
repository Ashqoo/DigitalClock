class person:
    def __init__(self):
        print("Hey I am a Person ")

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person()
a.name="Ashish"
a.occ="hr"
a.info()