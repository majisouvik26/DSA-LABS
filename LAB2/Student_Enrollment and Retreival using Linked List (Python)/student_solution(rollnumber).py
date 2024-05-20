import re

EntityArray = []
Students = []

class StudentRecord:
    def __init__(self, studentName=None, rollNumber=None):
        self.studentName = studentName
        self.rollNumber = rollNumber

    def get_studentName(self):
        return self.studentName

    def set_studentName(self, name):
        self.studentName = name

    def get_rollNumber(self):
        return self.rollNumber

    def set_rollNumber(self, rollnum):
        self.rollNumber = rollnum

class Node:
    def __init__(self, student):
        self.next = None
        self.element = student

    def get_next(self):
        return self.next

    def set_next(self, value):
        self.next = value

    def get_element(self):
        return self.element

    def set_element(self, student):
        self.element = student

class LinkedList:
    def __init__(self):
        self.head = None
        
    # add_student 
    def add_student(self, student):
        if self.iterator is None:
            self.iterator = Node(student)
        else:
            new_node = Node(student)
            new_node.set_next(self.iterator)
            self.iterator = new_node

    # delete_student    
    def delete_student(self, student_name):
        current = self.iterator
        previous = None

        while current:
            if current.get_element().get_studentName() == student_name:
                if previous:
                    previous.set_next(current.get_next())
                else:
                    self.iterator = current.get_next()
                return
            previous = current
            current = current.get_next()
            
        
class Entity(LinkedList):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.iterator = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_iterator(self):
        return self.iterator

    def set_iterator(self, iter):
        self.iterator = iter

    def get_entity(cls, entity_name):
        for entity in EntityArray:
            if entity.get_name() == entity_name:
                return entity


def random_list(data):
    return data.strip("[]").split(',')

def remove_brackets(name):
    return name.strip('[]')

def get_student(entity, student_name):
    current = entity.head
    while current:
        if current.get_element().get_studentName() == student_name:
            return current.get_element()
        current = current.get_next()

def create_entity(name):
    for entity in EntityArray:
        if entity.get_name() == name:
            return entity
    new_entity = Entity(name)
    EntityArray.append(new_entity)
    return new_entity

#Reading the input file
def read_input_file(file_path):
    pattern = r'(\w+),(\w+),(\w+),\[(.*?)\],(\w+),\[(.*?)\]'
    with open(file_path, 'r') as file:
        data = file.read()

    components = re.findall(pattern, data)

    for Elements in components:
        name, roll_number, department, courses, hostel, clubs = Elements
        courses = courses.split(',')
        clubs = clubs.split(',')
        student = StudentRecord(name, roll_number)

        department_entity = create_entity(department)
        hostel_entity = create_entity(hostel)

        department_entity.add_student(student)
        hostel_entity.add_student(student)

        for course in courses:
            course_entity = create_entity(course)
            course_entity.add_student(student)

        for club in clubs:
            club_entity = create_entity(club)
            club_entity.add_student(student)

