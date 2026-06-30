from fastapi import FastAPI

app = FastAPI()

orders = [
    {"id": 1, "customer_name": "Nguyen Van An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Tran Thi Binh", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Le Thu Huong", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Pham Thi Dung", "total": 320000, "status": "pending"}
]

@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    # Danh sách các trạng thái hợp lệ theo yêu cầu
    valid_statuses = ["pending", "paid", "cancelled"]
    
    # Kiểm tra xem trạng thái truyền vào có hợp lệ không
    if status not in valid_statuses:
        return {"message": "Trạng thái đơn hàng không hợp lệ"}
    
    # Khởi tạo một mảng rỗng để chứa các đơn hàng đã lọc
    filtered_orders = []
    
    # Duyệt qua từng đơn hàng và kiểm tra trạng thái
    for order in orders:
        if order["status"] == status:
            filtered_orders.append(order)
            
    return filtered_orders

    # Lưu ý: Thay vì dùng vòng lặp for, bạn cũng có thể viết ngắn gọn bằng List Comprehension:
    # return [order for order in orders if order["status"] == status]
