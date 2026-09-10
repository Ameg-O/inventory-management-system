from person import Person

class Admin(Person):
    def __init__(self,person_id,name,phone,email,username,password):
        super().__init__(person_id,name,phone,email)
        self.username=username
        self.password=password
    def display(self):
        super().display()
        print("username : ",self.username)
    def login(self,username,password):
        if self.username==username and self.password==password:
            return True
        else:
             return False