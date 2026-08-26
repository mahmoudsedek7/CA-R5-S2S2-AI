class Person:
    """Base class for all people in the hospital."""
    def __init__(self, id, name, age):
        self.name = name
        self.age = age
        self.id = id

    def view_info(self):
        """View basic information about the person."""
        return f"id: {self.id}, Name: {self.name}, Age: {self.age}"


class Patient(Person):
    """Class for hospital patients, inheriting from Person."""
    def __init__(self, id, name, age, medical_record):
        super().__init__(id, name, age)
        self.medical_record = medical_record

    def view_record(self):
        """View patient record."""
        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    """Class for hospital staff, inheriting from Person."""
    def __init__(self, id, name, age, position):
        super().__init__(id, name, age)
        self.position = position

    def view_info(self):
        """View staff information."""
        return f"Staff id: {self.id}, Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Hospital:
    """Class for managing hospital operations."""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []  # List to hold departments

    def add_department(self, department):
        """Add a department to the hospital."""
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")


class Department:
    """Class representing a department in the hospital."""
    def __init__(self, name):
        self.name = name
        self.patients = []  # List to hold patients
        self.staff = []     # List to hold staff

    def add_patient(self, patient):
        """Add a patient to the department."""
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        """Add staff member to the department."""
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")