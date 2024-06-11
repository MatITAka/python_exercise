class Identity :
    def __init__(self,name,age, location,job):
        self.firstName = name
        self.age = age
        self.location = location
        self.job = job

class IndetityCard(Identity) :
    pass


Identity1 = Identity("Mateo", 22, "France", "Dev")

IdentityCard1 = IndetityCard("Tom", 20, "Italie", "Dev")

print(Identity1.firstName)
print(Identity1.age)

print(IdentityCard1.firstName)
print(IdentityCard1.location)






