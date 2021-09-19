# wapp to detect grade for list of student

# wapp to detect grade of student using OOP

class student:
	def __init__(self, rno, name, marks):
		self.rno = rno
		self.name = name
		self.marks = marks
	def show(self):
		print("rno = ", self.rno)
		print("name = ", self.name)
		print("marks = ", self.marks)
	def find_grade(self):
		if self.marks > 80:
			print("Grade A ")
		elif self.marks > 60:
			print(" Grade B")
		else:
			print(" Grade C")
data = []
while True:
	op = int(input("1 add, 2 view, 3 delete and 4 exit "))
	if op == 1:
		rno = int(input(" enter your rno "))
		name = input(" enter your name ")
		marks = int(input(" enter your marks "))
		s = student(rno, name, marks)
		data.append(s)
	elif op == 2:
		for d in data:
			print("*" * 50)
			d.show()
			d.find_grade()
			print("*" * 50)
	elif op == 3:
		rno = int(input(" enter rno to be deleted "))
		for d in data:
			if d.rno == rno:
				data.remove(d) 
	elif op == 4:
		break
	else:
		print(" invalid option ")


