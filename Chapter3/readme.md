# Chapter 3 — Exercises

## Nội dung thư mục

- `Exercise1.py` — Lớp `Student` (Tính điểm trung bình và xếp loại)
- `Exercise2.py` — Chu vi và diện tích đường tròn
- `Exercise3.py` — Khoảng cách giữa hai điểm (Hệ toạ độ 2D)
- `Exercise4.cpp` — Lớp `cArray`: mảng số nguyên, các thao tác (random, tìm âm lớn nhất, đếm tần suất, kiểm tra giảm dần, sắp xếp)
- `Exercise5.cpp` — Lớp `Student` (C++): so sánh GPA và tuổi giữa 2 sinh viên
- `Exercise6.py` — Lớp `ComplexNumber`: các phép toán trên số phức (cộng, trừ, nhân, chia)

---

## Chi tiết từng bài

### Exercise1.py (Python)
- Mô tả: Định nghĩa lớp `Student` với các thuộc tính `name`, `math`, `literature` và `average`. Có phương thức `classification()` để xếp loại theo điểm trung bình.
- Input (chạy tương tác):
	- Tên học sinh (string)
	- Điểm Toán (số nguyên)
	- Điểm Văn (số nguyên)
- Output: In ra điểm trung bình và xếp loại (ví dụ: `xuat sac`, `gioi`, `kha`, ...)
- Ghi chú: Giá trị điểm được chuyển sang `int` trong chương trình; nếu điểm trung bình ngoài khoảng hợp lệ, hàm trả `wrong input`.

### Exercise2.py (Python)
- Mô tả: Tính chu vi và diện tích của đường tròn.
- Input (chạy tương tác):
	- Nhập `x`, `y` (được yêu cầu trong chương trình nhưng không được sử dụng ở tính toán)
	- Bán kính `r` (float)
- Output: In `Chu vi duong tron` và `Dien tich duong tron`.
- Ghi chú: `x` và `y` trong mã hiện tại không ảnh hưởng đến kết quả; cần chỉ nhập bán kính để tính.

### Exercise3.py (Python)
- Mô tả: Tính khoảng cách Euclid giữa hai điểm A(x1, y1) và B(x2, y2).
- Input (chạy tương tác):
	- `x1`, `y1`, `x2`, `y2` (float)
- Output: In khoảng cách với 2 chữ số thập phân.

### Exercise4.cpp (C++)
- Mô tả: Lớp `cArray` tạo một mảng kích thước cố định (mặc định 15) với giá trị ngẫu nhiên trong khoảng [-100, 100]. Cung cấp các phương thức:
	- `printarr()` — in mảng
	- `max_neg()` — trả về phần tử âm lớn nhất (hoặc giá trị cờ nếu không có số âm)
	- `freqx(int x)` — đếm số lần xuất hiện của `x`
	- `des_arr()` — kiểm tra mảng có giảm dần không
	- `sortarr()` — sắp xếp mảng tăng dần (dùng `std::sort`)
- Chạy: chương trình sẽ khởi tạo mảng, in mảng, in âm lớn nhất (nếu có), yêu cầu nhập số cần đếm, kiểm tra giảm dần rồi in mảng đã sắp xếp.
- Biên dịch / chạy (trong WSL hoặc môi trường có g++):

```bash
g++ Exercise4.cpp -o exercise4
./exercise4
```

### Exercise5.cpp (C++)
- Mô tả: Lớp `Student` (phiên bản C++) có các trường `id`, `name`, `gender`, `birthYear`, `gpa`. Chương trình nhập thông tin cho 2 sinh viên, rồi:
	- In tên sinh viên có GPA cao hơn (hoặc ghi cả hai nếu bằng)
	- In tên sinh viên trẻ hơn (so sánh theo `birthYear`)
- Biên dịch / chạy:

```bash
g++ Exercise5.cpp -o exercise5
./exercise5
```

### Exercise6.py (Python)
- Mô tả: Lớp `ComplexNumber` đại diện số phức, hỗ trợ:
	- `input_complex()` để nhập phần thực và phần ảo
	- `display()` để in dạng a + bi
	- `add`, `subtract`, `multiply`, `divide` — trả về đối tượng `ComplexNumber` kết quả
- Chạy: khi chạy file tương tác, người dùng nhập hai số phức A và B, chương trình in kết quả các phép toán.
- Ghi chú: phép chia kiểm tra mẫu số khác 0, nếu bằng 0 sẽ ném `ZeroDivisionError`.
