class Member_Info:
   def __init__(self, name, age, id):
      self.name = name
      self.age = age
      self.id = id

   def get_name(self):
      return self.name
   def get_age(self):
      return self.age
   def get_id(self):
      return self.id
   
M = Member_Info
name = input('Enter name --> ')
age = input('Enter age --> ')
id = input('Enter id --> ')
print(M.get_name(name))
print(M.get_age(age))
print(M.get_id(id))
