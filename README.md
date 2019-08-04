# USYD-Class-Change
This script is for attempting to change to classes which are at maximum capacity. While the script is running, it spams the University of Sydney timetable website with class change requests so that as soon as there is a vacancy, the user's current class will be changed to that session.

Note that for every 21 failed requests performed in succession, the user will be locked out and denied from making requests for an hour. However, this can be bypassed by performing a successful class change, which will reset the user's request count. The script automatically handles this.

To use the program, a .txt file must be provided with the details of each class change on a separate line. For each class change, the course name, course code and class option must be provided. An example can be found in the included text file.
