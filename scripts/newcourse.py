from collections import defaultdict
import os.path, sys

MATH_DEPT = [
    '21', '36'
]

CS_DEPT = [
    '15', '02', '10', '11'
]

ECE_DEPT = [
    '18', '33'
]

CS_DIR = "../CS_Courses"
ECE_DIR = "../ECE_Courses"
MATH_DIR = "../Math_Courses"

DEFAULT = "../Misc_Courses"

NO_ARGS = 8

def add_to_map(ddm: dict, dept: list, ident: str):
    for dept_no in dept:
        ddm[dept_no] = ident

if __name__ == "__main__":
    if len(sys.argv) != NO_ARGS:
        print(
            "Usage: ... newcourse.py XXXXX Course_Name SemesterTaken InstructorName " + \
            "Enjoyment Difficulty TimeCommitment"
        )
        exit(0)
    # Initialize XX -> dept mapping
    dept_dir_map = defaultdict(lambda: DEFAULT)
    add_to_map(dept_dir_map, MATH_DEPT, MATH_DIR)
    add_to_map(dept_dir_map, CS_DEPT, CS_DIR)
    add_to_map(dept_dir_map, ECE_DEPT, ECE_DIR)
    # Parse arguments
    _, course_title, course_name, sem_taken, instr_name, \
                    enjoy, diff, timecom = sys.argv
    # Post-processing
    dept = course_title[0:2]
    course_no = course_title[2:]
    course_name = course_name.replace("_", " ")
    # Assemble final contents
    markdown = f"# {dept}-{course_no}: {course_name}\n\n"
    markdown += f"## Basics\nTaken: *{sem_taken}*  \nInstructor: *{instr_name}*\n\n"
    markdown += f"## Ratings\n\n| __Category__ | __Rating__ |\n|---|---|\n"
    markdown += f"| Enjoyment | {enjoy}/10 |\n"
    markdown += f"| Difficulty | {diff}/10 |\n"    
    markdown += f"| Time Commitment | {timecom}/10 |\n\n"
    markdown += "## Overview\n"
    # Get appropriate path
    path = os.path.join(dept_dir_map[dept], f"{course_title}.md")
    # Write new file
    with open(path, 'w') as new_course_file:
        new_course_file.write(markdown)
    exit(0)
