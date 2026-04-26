-> This are Eligible for Student's in Tire 3 collage.
students = []

def insert_student(name, marks):
  total = sum(marks)
  percentage = (total / len(marks) * 100)) * 100
  students.append({
      "name": name,
      "marks":marks,
      "percentage": percentage
  })

def select_eligible(threashold=60):
  eligible = [s for s in students if s["percentage"] >= threadhold]
  return eligible

insert_student("shaikh Tashif",[70,80,90,80])
insert_student("shaikh Aman",[60,50,50,70])
insert_student("shaikh pervaz",[70,70,75,90])

print("All students")
for s in students:
  print(f"{s['name']} - {s['percentage']:.2f}%)

print("\n Eligible Students (>=70%):")
eligible_studnets = select_eligible()
for s in eligible_students:
  print(f"{s['name']} - s {s['percentage']:.2f}%")





