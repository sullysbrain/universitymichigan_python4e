class PartyAnimal():
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print('i am constructed')
    
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)
    
    def __del__(self):
        print('i am destructed')

j = PartyAnimal('jim')
s = PartyAnimal('sally')

j.party()
j.party()

s.party()
