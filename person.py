class Person:
    def __init__(self,person_id,name,phone,email):
        self.person_id=person_id
        self.name=name
        self.phone=phone
        self.email=email
    def display(self):
        print("ID : ",self.person_id)
        print("Name : ",self.name)
        print("Phone : ",self.phone)
        print("Email : ",self.email)


