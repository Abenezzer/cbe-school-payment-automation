
from SchoolWeb import SchoolWebExtraction

try:

    school = SchoolWebExtraction("BIS/S/00002")
    student_data  = school.action()

    print(student_data)

except Exception as e:
    print(e)