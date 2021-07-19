import datetime
import enum

class AssignmentAppData:
    def __init__(self):
        self.categories = []
        self.finished = []

    def add_category(self, name, color="#FFFFFF"):
        category = Category(name, color)
        self.categories.append(category)

    def add_assignment(self, category_name, id, title, due_date, notes, priority):
        assignment = Assignment(id, title, due_date, notes, priority)
        for category in self.categories:
            if category.name == category_name:
                category.add_assignment(assignment)

    def clear_all_data(self):
        self.categories = []
        self.finished = []

    def complete_assignment(self, assignment):
        for c in self.categories:
            for a in c.assignments:
                if a.id == assignment.id:
                    finished_assignment = FinishedAssignment(assignment, datetime.datetime.now(), c.name)
                    self.finished.append(finished_assignment)
                    c.assignments.remove(assignment)
                    break

    def get_category_names(self):
        return [category.name for category in self.categories]

    def get_soonest_n_assignments(self, n):
        all_assignments_with_categories = []
        for category in self.categories:
            for assignment in category.assignments:
                all_assignments_with_categories.append((assignment, category.color))
        all_assignments_with_categories = sorted(all_assignments_with_categories, key=lambda x: x[0].due_date)
        return all_assignments_with_categories[:n]

    def __str__(self):
        string = ""
        string += "Categories:\n\n"
        for category in self.categories:
            string += category.name + ", " + category.color + "\n"
            string += str(category.assignments)
            string += "\n"
        # TODO add the other attributes here also
        return string


class Category:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.assignments = [] # should be sorted newest to oldest date

    def add_assignment(self, assignment):
        self.assignments.append(assignment)


class Assignment:
    def __init__(self, id, title, due_date, notes, priority):
        self.id = id # unique
        self.title = title
        self.due_date = due_date
        self.notes = notes
        self.priority = priority

class FinishedAssignment:
    def __init__(self, assignment, finished_date, category):
        self.assignment = assignment
        self.finished_date = finished_date
        self.category = category


class Priority(enum.Enum):
    none = 0
    low = 1
    medium = 2
    high = 3
