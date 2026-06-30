from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# Giả lập database chứa danh sách email đã tồn tại
db_emails = ["existing@gmail.com"]

# 1. Định nghĩa Model với Pydantic để validate dữ liệu
class Student(BaseModel):
    # Ràng buộc độ dài tối thiểu là 3 ký tự (Quy tắc 1)
    full_name: str = Field(..., min_length=3, description="Họ tên học viên, tối thiểu 3 ký tự")
    # Tự động validate chuẩn định dạng email (Quy tắc 2)
    email: EmailStr = Field(..., description="Email học viên bắt buộc và phải đúng định dạng")
    age: int
    course: str
    phone: str

# 2. Xây dựng Endpoint POST
@app.post("/students")
def create_student(student: Student):
    # Ràng buộc nghiệp vụ: Kiểm tra email đã tồn tại hay chưa (Bẫy 3)
    if student.email in db_emails:
        # Trả về đúng định dạng lỗi yêu cầu
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email đã tồn tại trong hệ thống"
        )
    
    # Nếu vượt qua mọi validate, tiến hành lưu vào DB giả lập
    db_emails.append(student.email)
    
    # Trả về kết quả thành công
    return {
        "message": "Đăng ký học viên thành công",
        "data": student
    }
