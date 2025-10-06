# Chapter 1 — Exercises

## Nội dung thư mục

- `Exercise2.cpp` — Ví dụ nạp chồng hàm (overload) và tham số mặc định (C++)
- `Exercise3.py` — Lớp `Fraction` và các phép toán trên phân số; xử lý ngày (next day)
- `Exercise4.py` — Lớp `Employee` và `Company`: quản lý nhân viên, tính tổng lương, tìm lương thấp nhất, thống kê thưởng, in danh sách sắp xếp

---

## Chi tiết từng bài

### Exercise2.cpp (C++)
- Mô tả: File minh họa nạp chồng hàm (function overloading) giữa hai hàm `func` với kiểu tham số khác nhau (int vs float) và tham số mặc định.
- Hành vi khi chạy (theo nội dung `main`):
    - `func()` gọi phiên bản `float` với giá trị mặc định -> in "So thuc: 0 0"
    - `func(i)` khi `i` là int -> gọi phiên bản `int` -> in "So nguyen: 1 0"
    - `func(f)` khi `f` là float -> gọi phiên bản `float` -> in "So thuc: 1.5 0"
    - `func(i, j)` với cả hai int -> in "So nguyen: 1 2"
    - `func(f, g)` với cả hai float -> in "So thuc: 1.5 2.5"
- Biên dịch / chạy (trong WSL hoặc môi trường có g++):

```bash
g++ Exercise2.cpp -o exercise2
./exercise2
```

### Exercise3.py (Python)
- Mô tả: Định nghĩa lớp `Fraction` và các hàm phụ trợ:
    - `shorten()` rút gọn phân số
    - `compare(frac1, frac2)` so sánh hai phân số
    - `add`, `subtract`, `multiple`, `devide` — các phép toán hai phân số
    - Ngoài ra có chức năng nhập một ngày theo định dạng `dd/mm/yyyy` và in ra ngày kế tiếp
- Input (chạy tương tác):
    - Nhập hai phân số `a/b` để thực hiện các phép toán và so sánh
    - Nhập một ngày `day/month/year` để in ngày kế tiếp
- Output: In kết quả rút gọn, phép toán, phân số lớn hơn, và ngày kế tiếp.
- Ghi chú: Chương trình sử dụng `math.gcd` để rút gọn; kiểm tra chia cho 0 trong phép chia.

### Exercise4.py (Python)
- Mô tả: Hai lớp `Employee` và `Company`. `Company` lưu danh sách nhân viên và cung cấp:
    - `all_net_sal()` — tổng thực lãnh (lương + thưởng)
    - `lowest_sal()` — danh sách tên nhân viên có lương cơ bản thấp nhất
    - `bonus_morethan_1200()` — đếm số nhân viên có thưởng >= 1_200_000
    - `print_sorted_employees()` — in danh sách nhân viên sắp xếp theo (phòng ban tăng dần, mã giảm dần)
- Input (hiện tại): chương trình khởi tạo sẵn một vài nhân viên mẫu trong `__main__`; có thể dễ dàng thay bằng nhập tương tác hoặc đọc file.
- Output: In tổng lương, danh sách nhân viên có lương thấp nhất, số nhân viên có thưởng lớn, và danh sách đã sắp xếp.
