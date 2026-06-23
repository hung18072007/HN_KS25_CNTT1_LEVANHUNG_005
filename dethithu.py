class Course:
    def __init__(self, course_id, course_name, credit, midterm_score, final_score, assignment_score):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        self.midterm_score = midterm_score
        self.final_score = final_score
        self.assignment_score = assignment_score
        self.total_score = 0
        self.grade = ""
        self.status = ""
        self.calculate_total_score()   
        self.calculate_grade()
        self.update_status()
        
    def calculate_total_score(self):
        total = (self.midterm_score * 0.3) + (self.assignment_score * 0.2) + (self.final_score * 0.5)
        self.total_score = total

    def calculate_grade(self):
        if self.total_score >= 8.5:
            self.grade = "A"
        elif self.total_score >= 7.0:
            self.grade = "B"
        elif self.total_score >= 5.5:
            self.grade = "C"
        elif self.total_score >= 4.0:
            self.grade = "D"
        else:
            self.grade = "F"

    def update_status(self):
        if self.grade in ["A", "B", "C" ,"D"]:
            self.status = "Pass"
        else:
            self.status = "Retake"


class Student:
    def __init__(self, student_id, name, age, class_name):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.class_name = class_name
        self.courses = []

    def add_course(self):
        print("\n--- ĐĂNG KÝ MÔN HỌC ---")
        try:
            course_id = input("Nhập ID môn học: ").strip().upper()
            if course_id == "":
                print("ID môn học không được rỗng!")
                return
            for c in self.courses:
                if c.course_id.upper() == course_id:
                    print("Môn học này đã được đăng ký trước đó rồi!")
                    return
            course_name = input("Nhập tên môn học: ").strip()
            if course_name == "":
                print("Tên môn học không được rỗng!")
                return
            credit = int(input("Nhập số tín chỉ: "))
            if credit <= 0:
                print("Số tín chỉ phải lớn hơn 0!")
                return
            midterm_score = float(input("Nhập điểm giữa kỳ: "))
            final_score = float(input("Nhập điểm cuối kỳ: "))
            assignment_score = float(input("Nhập điểm bài tập: "))
            
            new_course = Course(course_id, course_name, credit, midterm_score, final_score, assignment_score)
            self.courses.append(new_course)
            print("Đã đăng ký môn học thành công!")
        except ValueError:
            print("Dữ liệu nhập vào không hợp lệ!")

    def remove_course(self):
        print("\n--- XÓA MÔN HỌC ---")
        course_id = input("Mời bạn nhập ID môn học cần xóa: ").strip().upper()
        for c in self.courses:
            if c.course_id.upper() == course_id:
                self.courses.remove(c)
                print("Đã xóa môn học thành công!")
                return
        print("Không tìm thấy môn học có ID này để xóa!")

    def calculate_gpa(self):
        if len(self.courses) == 0:
            return 0.0
        total_point = 0.0
        total_credit = 0
        for c in self.courses:
            if c.grade == "A":
                point = 4.0
            elif c.grade == "B":
                point = 3.0
            elif c.grade == "C":
                point = 2.0
            elif c.grade == "D":
                point = 1.0
            else:
                point = 0.0
            total_point += point * c.credit
            total_credit += c.credit
        return total_point / total_credit

    def academic_status(self):
        gpa = self.calculate_gpa()
        if len(self.courses) == 0:
            return "Chưa học"
        if gpa >= 3.6:
            return "Xuất sắc"
        elif gpa >= 3.2:
            return "Giỏi"
        elif gpa >= 2.5:
            return "Khá"
        elif gpa >= 2.0:
            return "Trung bình"
        else:
            return "Yếu"
    

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            student_id = input("Nhập id sinh viên: ").strip().upper()
            if student_id == "":
                print("Id sinh viên ko đc rỗng!")
                return
            for student in self.students:
                if student.student_id.upper() == student_id:
                    print("Id sinh viên ko được trùng")
                    return
            name = input("Mời bạn nhập tên sinh viên: ").strip()
            if name == "":
                print("Tên sinh viên ko đc rỗng!")
                return
            age = int(input("Mời bạn nhập tuổi của sinh viên: "))
            if age < 16:
                print("Độ tuổi của sinh viên ko hợp lệ!")
                return
            class_name = input("Nhập tên lớp của sinh viên: ").strip()
            if class_name == "":
                print("Tên lớp không được rỗng!")
                return
                
            new_student = Student(student_id, name, age, class_name)
            self.students.append(new_student)
            print("Thêm mới sinh viên thành công")
        except ValueError:
            print("Dữ liệu không hợp lệ (Tuổi phải là số)!")
            
    def show_all(self):
        if len(self.students) == 0:
            print("Danh sách sinh viên đang rỗng")
            return
        print("\n=== DANH SÁCH SINH VIÊN ===")
        for s in self.students:
            print(f"ID: {s.student_id} | Tên: {s.name} | Lớp: {s.class_name} | GPA: {s.calculate_gpa()} | Học lực: {s.academic_status()}")
            
    def update_student(self):
        id_update = input("Mời bạn nhập id sinh viên cần cập nhật:").strip().upper()
        for s in self.students:
            if s.student_id == id_update:
                try:
                    new_name = input("Mời bạn nhập tên sinh viên mới:").strip()
                    if new_name == "":
                        print("Tên sinh viên không hợp lệ!")
                        return
                    new_class = input("Nhập tên lớp mới của sinh viên:")
                    if new_class == "":
                        print("Tên lớp ko hợp lệ!")
                        return
                    new_age = int(input("Mời bạn nhập tuổi mới của sinh viên:"))
                    if new_age < 16:
                        print("Tuổi sinh viên ko hợp lệ")
                        return
                    
                    s.name = new_name
                    s.class_name = new_class
                    s.age = new_age
                    print("Cập nhật sinh viên thành công")
                    return
                except ValueError:
                    print("Dữ liệu tuổi mới không hợp lệ!")
                    return
                
        print("Không tìm thấy sinh viên có ID này!")

    def delete_student(self):
        print("\n--- XÓA SINH VIÊN ---")
        id_delete = input("Mời bạn nhập ID sinh viên cần xóa: ").strip().upper()
        for s in self.students:
            if s.student_id == id_delete:
                confirm = input(f"Bạn có chắc chắn muốn xóa sinh viên {s.name}? (Y/N): ").strip().upper()
                if confirm == "Y":
                    self.students.remove(s)
                    print("Đã xóa sinh viên thành công!")
                else:
                    print("Đã hủy thao tác xóa.")
                return
                
        print("Không tìm thấy sinh viên có ID này!")

    def manage_student_courses(self):
        id_find = input("Nhập ID sinh viên cần quản lý học phần: ").strip().upper()
        for s in self.students:
            if s.student_id == id_find:
                print("\n--- QUẢN LÝ HỌC PHẦN ---")
                print("1. Đăng ký môn học mới")
                print("2. Xóa môn học")
                sub_choice = input("Chọn chức năng (1-2): ").strip()
                if sub_choice == "1":
                    s.add_course()
                elif sub_choice == "2":
                    s.remove_course()
                else:
                    print("Lựa chọn không hợp lệ!")
                return
        print("Không tìm thấy sinh viên có ID này!")

    def update_all_gpa(self):
        print("\n--- TÍNH & CẬP NHẬT GPA ---")
        if len(self.students) == 0:
            print("Không có sinh viên nào trong hệ thống để cập nhật!")
            return
        for s in self.students:
            gpa = s.calculate_gpa()
            for c in s.courses:
                c.calculate_total_score()
                c.calculate_grade()
                c.update_status()
        print("Đã tiến hành tính toán và đồng bộ lại toàn bộ điểm hệ thống!")

    def show_statistics(self):
        print("\n--- THỐNG KÊ HỌC TẬP ---")
        if len(self.students) == 0:
            print("Hệ thống chưa có dữ liệu sinh viên!")
            return
            
        excellent = 0
        good = 0
        fair = 0
        average = 0
        weak = 0
        not_studied = 0
        
        for s in self.students:
            status = s.academic_status()
            if status == "Xuất sắc":
                excellent += 1
            elif status == "Giỏi":
                good += 1
            elif status == "Khá":
                fair += 1
            elif status == "Trung bình":
                average += 1
            elif status == "Yếu":
                weak += 1
            elif status == "Chưa học":
                not_studied += 1
                
        print(f"Tổng số sinh viên: {len(self.students)}")
        print(f"- Xuất sắc: {excellent} sinh viên")
        print(f"- Giỏi: {good} sinh viên")
        print(f"- Khá: {fair} sinh viên")
        print(f"- Trung bình: {average} sinh viên")
        print(f"- Yếu: {weak} sinh viên")
        print(f"- Chưa có môn học: {not_studied} sinh viên")

    def show_top_students(self):
        print("\n--- TOP SINH VIÊN CÓ GPA CAO NHẤT ---")
        if len(self.students) == 0:
            print("Danh sách sinh viên đang rỗng!")
            return
            
        sorted_students = sorted(self.students, key=lambda s: s.calculate_gpa(), reverse=True)
        
        limit = 5
        if len(sorted_students) < 5:
            limit = len(sorted_students)
            
        for rank in range(limit):
            s = sorted_students[rank]
            print(f"Top {rank+1} -> ID: {s.student_id} | Tên: {s.name} | GPA: {s.calculate_gpa()} | Học lực: {s.academic_status()}")


def main():
    manager = StudentManager()
    while True:
        print("\n================ MENU =================")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Thêm sinh viên")
        print("3. Cập nhật sinh viên")
        print("4. Xóa sinh viên")
        print("5. Quản lý học phần (Môn học)")
        print("6. Tính & Cập nhật GPA")
        print("7. Thống kê học tập")
        print("8. Top sinh viên")
        print("9. Thoát")
        print("=====================================")
        
        choice = input("Chọn chức năng: ").strip()
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_student()
            case "3":
                manager.update_student()
            case "4":
                manager.delete_student()
            case "5":
                manager.manage_student_courses()
            case "6":
                manager.update_all_gpa()
            case "7":
                manager.show_statistics()
            case "8":
                manager.show_top_students()
            case "9":
                print("Chương trình kết thúc. Cảm ơn bạn!")
                break
            case _:
                print("Lựa chọn không đúng, vui lòng nhập lại!")


if __name__ == "__main__":
    main()