from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Dữ liệu danh sách sản phẩm
products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Keyboard", "price": 1000000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products")
def get_products(keyword: Optional[str] = None, max_price: Optional[float] = None):
    # 1. Ràng buộc & Bắt lỗi dữ liệu
    if max_price is not None and max_price < 0:
        return {"detail": "max_price không được âm"}
    
    # 2. Khởi tạo mảng kết quả ban đầu là toàn bộ danh sách
    filtered_products = products
    
    # 3. Lọc theo keyword (nếu có truyền)
    if keyword is not None:
        keyword_lower = keyword.lower()
        # Lọc các sản phẩm có tên chứa keyword (không phân biệt hoa thường)
        filtered_products = [
            product for product in filtered_products 
            if keyword_lower in product["name"].lower()
        ]
        
    # 4. Lọc theo mức giá tối đa (nếu có truyền)
    if max_price is not None:
        # Lọc các sản phẩm có giá nhỏ hơn hoặc bằng max_price
        filtered_products = [
            product for product in filtered_products 
            if product["price"] <= max_price
        ]
        
    # 5. Trả về kết quả
    return filtered_products
