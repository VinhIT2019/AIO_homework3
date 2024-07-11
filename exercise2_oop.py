#2
from abc import ABC, abstractmethod
class Person(ABC):
  def __init__(self, name:str, yob:int):
    self._name = name
    self._yob = yob

  def get_yob(self):
    return self._yob

  @abstractmethod
  def discribe(self):
    pass

class Teacher(Person):
  def __init__(self, name:str, yob:int, subject:str):
    super().__init__(name, yob)
    self._subject = subject

  def discribe(self):
    print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
  def __init__(self, name:str, yob:int, specialist:str):
    super().__init__(name, yob)
    self._specialist = specialist

  def discribe(self):
    print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

class Student(Person):
  def __init__(self, name:str, yob:int, grade:str):
    super().__init__(name, yob)
    self._grade = grade

  def discribe(self):
    print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

#2a
student1 = Student(name ="studentA", yob=2010 , grade ="7")
student1.discribe()

teacher1 = Teacher(name ="teacherA", yob =1969 , subject ="Math")
teacher1.discribe()

doctor1 = Doctor(name ="doctorA", yob =1945 , specialist ="Endocrinologists")
doctor1.discribe()

class Ward:
  def __init__ (self , name : str):
    self.__name = name
    self.__list_people = []

  def add_person (self , person : Person ):
    self.__list_people.append(person)

  def describe ( self ):
    print(f"Ward - Name: {self.__name}")
    for person in self.__list_people:
      person.discribe()

  def count_doctor ( self ):
    count = 0
    for person in self.__list_people:
      if isinstance(person, Doctor):
        count += 1
    return count

  def sort_age(self):
    self.__list_people.sort(key=lambda x: x._yob, reverse = True)

  def compute_average(self):
    total_age = 0
    num_teachers = 0
    for person in self.__list_people:
      if isinstance(person, Teacher):
        total_age += person._yob
        num_teachers += 1
    if num_teachers == 0:
      return 0
    return total_age / num_teachers

#2b
print ()
teacher2 = Teacher(name ="teacherB", yob =1995 , subject ="History")
doctor2 = Doctor(name ="doctorB", yob =1975 , specialist ="Cardiologists")
ward1 = Ward(name ="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

#2c
print(f"\nNumber of doctors : {ward1.count_doctor()}")

#2d
print("\nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

#2e
print(f"\nAverage year of birth ( teachers ): {ward1.compute_average()}")