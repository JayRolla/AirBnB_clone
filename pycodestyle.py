#!/usr/bin/python3
class ALXStudent:
    """
    A simple class representing an ALX student.
    Attributes:
        name (str): The name of the student.
        cohort (int): The cohort number.
    """

    def __init__(self, name, cohort):
        """
        Initialize an ALXStudent instance with a name and cohort.
        Args:
            name (str): The name of the student.
            cohort (int): The cohort number of the student.
        """
        self.name = name
        self.cohort = cohort

    def __str__(self):
        """
        Return a string representation of the ALXStudent.
        """
        return f"ALXStudent(name={self.name}, cohort={self.cohort})"

    def display_info(self):
        """
        Print information about the student.
        """
        print(f"Student Name: {self.name}")
        print(f"Cohort Number: {self.cohort}")

# Example usage:
if __name__ == "__main__":
    student = ALXStudent("Molapo Kgarose", 5)
    print(student)
    student.display_info()
