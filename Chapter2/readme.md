# Chapter 2 — Exercises

## Nội dung thư mục

- `Exercise1+2.py` — Lớp và hàm xử lý phân số: cộng, trừ, nhân, chia; tổng danh sách phân số; tìm phân số lớn nhất
- `Exercise3.py` — Các phép toán trên ma trận: cộng, trừ, nhân (với kiểm tra kích thước)
- `Exercise4.py` — Lớp `Student` (Python): lưu thông tin sinh viên và tính điểm trung bình, in danh sách

---

## Chi tiết từng bài

### Exercise1+2.py (Python)
- Mô tả: Định nghĩa lớp `Fraction` và các hàm thao tác:
	- `add`, `subtract`, `multiple`, `devide` cho hai phân số
	- `sum_list(fractions)` để tính tổng một danh sách phân số
	- `max_frac(fractions)` để tìm phân số lớn nhất theo giá trị thực
- Input (chạy tương tác):
	- Nhập hai phân số theo định dạng `a/b` (a và b là số nguyên, b != 0)
	- Sau đó nhập số lượng phân số và từng phân số để tính tổng danh sách và tìm phần tử lớn nhất
- Output: In kết quả tổng, hiệu, tích, thương của hai phân số; in tổng của danh sách và phân số lớn nhất.
- Ghi chú: Kết quả được rút gọn bằng gcd; nếu kết quả là số nguyên thì in dạng nguyên, nếu là phân số thì in `p/q`.

### Exercise3.py (Python)
- Mô tả: Hàm nhập ma trận và thực hiện các phép:
	- Cộng và trừ hai ma trận có cùng kích thước
	- Nhân hai ma trận nếu cột của A = hàng của B
- Input (chạy tương tác):
	- Nhập `r1 c1` rồi `r1` dòng, mỗi dòng `c1` số nguyên cho ma trận A
	- Nhập `r2 c2` rồi `r2` dòng cho ma trận B
- Output: In ma trận tổng/hiệu nếu khả thi; in ma trận tích nếu khả thi; nếu không khả thi sẽ in thông báo tương ứng.

### Exercise4.py (Python)
- Mô tả: Lớp `Student` lưu các trường `id`, `name`, `gender`, `math`, `physics`, `chemist` và tính `average`.
- Input (chạy tương tác):
	- Nhập số lượng sinh viên `n`, sau đó nhập `n` dòng theo định dạng CSV: `ID,Name,Gender,Math,Physics,Chemist`
- Output: In danh sách sinh viên kèm điểm trung bình.
