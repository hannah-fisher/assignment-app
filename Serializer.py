import json
import datetime

from AssignmentAppData import AssignmentAppData


class Serializer():
    def __init__(self):
        pass

    @classmethod
    def serialize(cls, filename, appData):
        """
        Given an AssignmentAppData object,
        Write the contents to a json file
        """
        categoriesData = {}
        finishedData = []
        for category in appData.categories:
            categoryData = {}
            categoryData["Color"] = category.color
            assignmentsData = []
            for assignment in category.assignments:
                assignmentData = {}
                assignmentData["id"] = f"{assignment.id}"
                assignmentData["title"] = assignment.title
                dueDateData = {}
                dueDateData["year"] = assignment.due_date.year
                dueDateData["month"] = assignment.due_date.month
                dueDateData["day"] = assignment.due_date.day
                dueDateData["hour"] = assignment.due_date.hour
                assignmentData["due_date"] = dueDateData
                assignmentData["notes"] = assignment.notes
                assignmentData["priority"] = f"{assignment.priority:01}"
                assignmentsData.append(assignmentData)
            categoryData["Assignments"] = assignmentsData
            categoriesData[category.name] = categoryData
        for finishedAssignment in appData.finished:
            finishedAssignmentData = {}
            finishedAssignmentData["category"] = finishedAssignment.category
            dateData = {}
            dateData["year"] = finishedAssignment.finished_date.year
            dateData["month"] = finishedAssignment.finished_date.month
            dateData["day"] = finishedAssignment.finished_date.day
            dateData["hour"] = finishedAssignment.finished_date.hour
            finishedAssignmentData["finished_date"] = dateData
            assignmentData = {}
            assignmentData["id"] = f"{finishedAssignment.assignment.id}"
            assignmentData["title"] = finishedAssignment.assignment.title
            dueDateData = {}
            dueDateData["year"] = finishedAssignment.assignment.due_date.year
            dueDateData["month"] = finishedAssignment.assignment.due_date.month
            dueDateData["day"] = finishedAssignment.assignment.due_date.day
            dueDateData["hour"] = finishedAssignment.assignment.due_date.hour
            assignmentData["due_date"] = dueDateData
            assignmentData["notes"] = finishedAssignment.assignment.notes
            assignmentData[
                "priority"] = f"{finishedAssignment.assignment.priority:01}"
            finishedAssignmentData["assignment"] = assignmentData
            finishedData.append(finishedAssignmentData)
        preferencesData = appData.preferences
        appDataDict = {"Categories": categoriesData, "Finished": finishedData, "Preferences": preferencesData}
        # write to file
        try:
            json_file = open(filename, "w")
            json.dump(appDataDict, json_file, indent=1)
            json_file.close()
        except FileNotFoundError:
            # TODO something more here
            print("file not found: " + filename)

    @classmethod
    def deserialize(cls, json_file_path):
        """
        Given a json file path,
        Reads the json and creates an AssignmentAppData object
        """
        try:
            json_file = open(json_file_path)
            json_data = json.load(json_file)
            appData = AssignmentAppData()
            # load categories
            for category_name in json_data["Categories"]:
                category_json = json_data["Categories"][category_name]
                if "Color" in category_json:
                    appData.add_category(category_name, category_json["Color"])
                else:
                    appData.add_category(category_name)
                assignments_json = category_json["Assignments"]
                for assignment in assignments_json:
                    d = assignment["due_date"]
                    due_date = datetime.datetime(d["year"],
                                                 d["month"],
                                                 d["day"],
                                                 hour=d["hour"])
                    appData.add_assignment(category_name, assignment["id"],
                                           assignment["title"], due_date,
                                           assignment["notes"],
                                           int(assignment["priority"]))
            # TODO load finished assignments
            # load preferences
            for preference in json_data["Preferences"]:
                appData.add_preference(preference, json_data["Preferences"][preference])
            json_file.close()
            return appData
        except FileNotFoundError:
            # TODO something more here
            print("file not found: " + json_file_path)
            return AssignmentAppData()
