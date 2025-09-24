
""" 
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""

import datetime

class AttendanceRegister:
    def __init__(self):
        self.attendance_records = {}

    def register_student(self, student_name):
        if student_name not in self.attendance_records:
            self.attendance_records[student_name] = {
                "present_days": [],
                "absent_days": []
            }
        else:
            print(f"Student '{student_name}' is already registered.")

    def mark_present(self, student_name):
 
        today_date = str(datetime.date.today())
        if student_name in self.attendance_records:
            if today_date not in self.attendance_records[student_name]["present_days"]:
                self.attendance_records[student_name]["present_days"].append(today_date)

        
            if today_date in self.attendance_records[student_name]["absent_days"]:
                self.attendance_records[student_name]["absent_days"].remove(today_date)
        else:
            print(f"Student '{student_name}' is not found!.")


    def mark_absent(self, student_name):
        today_date = str(datetime.date.today())
        if student_name in self.attendance_records:
            if today_date not in self.attendance_records[student_name]["absent_days"]:
                self.attendance_records[student_name]["absent_days"].append(today_date)

    
            if today_date in self.attendance_records[student_name]["present_days"]:
                self.attendance_records[student_name]["present_days"].remove(today_date)
        else:
            print(f"Student '{student_name}' is not registered.")

    def get_status(self, student_name):
        today_date = str(datetime.date.today())
        if student_name in self.attendance_records:
            student_record = self.attendance_records[student_name]
            if today_date in student_record["present_days"]:
                return "Present"
            elif today_date in student_record["absent_days"]:
                return "Absent"
            else:
                return "Not marked"
        else:
            return f"Student '{student_name}' is not registered."

    def show_register(self):
        return self.attendance_records


student1 = AttendanceRegister()
student1.register_student("John")
student1.register_student("John")

print(student1.attendance_records)
student1.mark_present("John")
print(student1.get_status("John"))
print(student1.show_register())