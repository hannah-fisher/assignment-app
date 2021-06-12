import json
import datetime

from AssignmentAppData import AssignmentAppData

class Serializer():
    def __init__(self):
        pass

    @classmethod
    def serialize(cls):
        """
        Given an AssignmentAppData object,
        Write the contents to a json file
        """
        pass
        # TODO

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
                    due_date = datetime.datetime(d["year"], d["month"], d["day"], hour=d["hour"])
                    appData.add_assignment(category_name, int(assignment["id"]), assignment["title"], due_date, assignment["notes"], int(assignment["priority"]))
            # TODO load finished assignments
            json_file.close()
            return appData
        except FileNotFoundError:
            # TODO something more here
            print("file not found: " + json_file_path)
