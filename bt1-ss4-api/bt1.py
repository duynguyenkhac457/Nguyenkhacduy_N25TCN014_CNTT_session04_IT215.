from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop Dell", "price": 15000000},
    {"id": 2, "name": "Chuột Logitech", "price": 500000},
    {"id": 3, "name": "Bàn phím cơ", "price": 1200000}
]

# Sửa lỗi: Thêm {} để định nghĩa Path Parameter
@app.get("/product/{product_id}")
def get_product_detail(product_id: int):
    # Duyệt qua danh sách sản phẩm để tìm id tương ứng
    for product in products:
        if product["id"] == product_id:
            return product
            
    # Nếu vòng lặp kết thúc mà không tìm thấy
    return {
        "message": "Không tìm thấy sản phẩm"
    }
