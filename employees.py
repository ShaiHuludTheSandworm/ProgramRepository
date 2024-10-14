"""
On my/our honor, Shasa Lloyd Kolar and Ethan Gomez, this 
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: SLK2633
UT EID 2: EGB664
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """

    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self.performance = INITIAL_PERFORMANCE
        self.happiness = INITIAL_HAPPINESS
        if salary < 0:
            raise ValueError(SALARY_ERROR_MESSAGE)
        self.salary = salary

    def get_name(self):
        return self.__name
    
    def get_manager(self):
        return self.__manager

    @abstractmethod
    def work(self):
        pass

    def interact(self, other):
        if other.__name not in self.relationships:
            self.relationships[other.__name] = 0

        if self.relationships[other.__name] > RELATIONSHIP_THRESHOLD:
            self.happiness += 1
        elif self.happiness >= HAPPINESS_THRESHOLD and other.happiness >= HAPPINESS_THRESHOLD:
            self.relationships[other.__name] += 1
        else:
            self.relationships[other.__name] -= 1
            self.happiness -= 1
        self.happiness = adjust_employee_values(self.happiness)

    def daily_expense(self):
        self.savings -= DAILY_EXPENSE
        self.happiness -= 1
        self.happiness = adjust_employee_values(self.happiness)

    def __str__(self):
        return (
            f"{self.__name}\n"
            f"\tSalary: ${self.salary}\n"
            f"\tSavings: ${self.savings}\n"
            f"\tHappiness: {self.happiness}%\n"
            f"\tPerformance: {self.performance}%"
        )


class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """
    @property
    def name(self):
        return self._Employee__name

    @property
    def performance(self):
        return self._performance
    
    @performance.setter
    def performance(self, new_performance):
        self._performance = max(min(new_performance, 100), 0)

    @property
    def happiness(self):
        return self._happiness
    
    @happiness.setter
    def happiness(self, new_happiness):
        self._happiness = max(min(new_happiness, 100), 0)

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        elif new_salary < 0:
            raise ValueError(SALARY_ERROR_MESSAGE)

    def work(self):
        change_performance = random.randint(-5, 5)
        self.performance += change_performance
        if change_performance <= 0:
            self.happiness -= 1
            for key in self.relationships:
                self.relationships[key] -= 1
        else:
            self.happiness += 1
        self.performance = adjust_employee_values(self.performance)
        self.happiness = adjust_employee_values(self.happiness)


class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """
    def name(self):
        return self.get_name

    def manager(self):
        return self.get_manager

    @property
    def performance(self):
        return self._performance
    
    @performance.setter
    def performance(self, new_performance):
        self._performance = max(min(new_performance, 100), 0)

    @property
    def happiness(self):
        return self._happiness
    
    @happiness.setter
    def happiness(self, new_happiness):
        self._happiness = max(min(new_happiness, 100), 0)

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        elif new_salary < 0:
            raise ValueError(SALARY_ERROR_MESSAGE)

    def work(self):
        change_performance = random.randint(-15, 15)
        if change_performance <= 0:
            self.happiness -= 2
        else:
            self.happiness += 1
        self.performance = adjust_employee_values(self.performance)
        self.happiness = adjust_employee_values(self.happiness)
    
    def interact(self, other):
        super().interact(other)
        if other.__name == self.__manager:
            if other.happiness > HAPPINESS_THRESHOLD and self.performance >= TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD:
                self.savings += MANAGER_BONUS
            elif other.happiness <= HAPPINESS_THRESHOLD:
                self.salary = self.salary // 2
                self.happiness -= 5
                self.happiness = adjust_employee_values(self.happiness)
                if self.salary == 0:
                    self.is_employed = False


class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """
    def name(self):
        return self.get_name

    def manager(self):
        return self.get_manager

    @property
    def performance(self):
        return self._performance
    
    @performance.setter
    def performance(self, new_performance):
        self._performance = max(min(new_performance, 100), 0)

    @property
    def happiness(self):
        return self._happiness
    
    @happiness.setter
    def happiness(self, new_happiness):
        self._happiness = max(min(new_happiness, 100), 0)


    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        elif new_salary < 0:
            raise ValueError(SALARY_ERROR_MESSAGE)
    def work(self):
        change_performance = random.randint(-10, 10)
        if change_performance >= 0:
            self.happiness += 1
        self.performance = adjust_employee_values(self.performance)
        self.happiness = adjust_employee_values(self.happiness)
    
    def interact(self, other):
        super().interact(other)
        if other.__name == self.__manager:
            if other.happiness > HAPPINESS_THRESHOLD and self.performance > PERM_EMPLOYEE_PERFORMANCE_THRESHOLD:
                self.savings += MANAGER_BONUS
            elif other.happiness <= HAPPINESS_THRESHOLD:
                self.happiness -= 1
                self.happiness = adjust_employee_values(self.happiness)


def adjust_employee_values(value):
    return max(min(value, 100), 0)