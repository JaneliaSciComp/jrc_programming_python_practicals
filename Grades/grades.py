"""
This program take a list of student grades and calculated their grade for the course.
The file is in the following format:
	Student Name
	81
	97
	100
	63

"""

def calculateGrade(grades):
	"""Calculates the mean of the students grades to
	get their overall grade in the class.
	Returns the overall grade.
	"""
	sum = 0
	count = 0
	for grade in grades:
		count += 1
		sum += grade
	return sum / float(count)

def parseFile(filename):
	"""
	Reads the grades file and gets the student name and 
	a list of their grades.
	Returns the name and list of grades.
	"""
	fi = open(filename)
	grades = []
	name = ""
	for line in fi:
		if not name:
			name = line.strip()
		else:
			grade = line.strip()
			grades.append(int(grade))
	fi.close()
	return name, grades


filename = "grades.txt"
name, grades = parseFile(filename)
studentGrade = calculateGrade(grades)
print studentGrade
if studentGrade >= 90:
	print name, "got an A."
elif studentGrade >= 80:
	print name, "got an B."
elif studentGrade >= 70:
	print name, "got an C."
elif studentGrade >= 60:
	print name, "got an D."
else:
	print name, "failed."