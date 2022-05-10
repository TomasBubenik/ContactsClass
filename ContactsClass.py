class Contact:
    def __init__(self,name,surname,number,id):
        self.name = name
        self.surname = surname
        self.number = number
        self.id = id
    def __str__(self):
        return self.name+","+self.surname+","+str(self.number)+","+str(self.id)

        



class ContactList:
    contacts = []
    nextid = 1
    def add(self,name,surname,number):
        self.contacts.append(Contact(name,surname,number,self.nextid))
        self.nextid = self.nextid+1
    def print(self):
        for i in self.contacts:
            print(i)
    def remove(self,id):
        for i in (self.contacts):
           if i.id == id:
               self.contacts.remove(i)
        
    def find(self,id):
        for i in (self.contacts):
           if i.id == id:
               print(i)
s = ContactList()

s.add("Tomas","Bubenik","0915039110")
s.add("Lukas","Forro","0911333664")
s.remove(2)
s.print()



