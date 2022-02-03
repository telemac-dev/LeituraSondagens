import csv

with open('students.csv', 'w', newline='') as student_file:
    writer = csv.writer(student_file)
    writer.writerow(["RollNo", "Name", "Subject"])
    writer.writerow([1, "ABC", "Economics"])
    writer.writerow([2, "TUV", "Arts"])
    writer.writerow([3, "XYZ", "Python"])
    