# Bài tập chương này gồm 3 bài - bài tập 2, bài tập 3 và bài tập 4

## Bài tập 2
### Giải thích kết xuất của chương trình sau (Exercise2.cpp)
- Với (1) -> Không truyền tham số nào, dùng `func (float = 0, float = 0)`
    Xuất: So thuc: 0 0
- Với (2) -> Truyền tham số i là số nguyên, dùng `func (int, int = 0)`
    Xuất: So nguyen: 1 0
- Với (3) -> Truyền tham số f là số thực, dùng `func (float = 0, float = 0)`
    Xuất: So thuc: 1.5 0
- Với (4) -> Truyền tham số i, j là số nguyên, dùng `func (int, int = 0)`
    Xuất: So nguyen: 1 2
- Với (5): -> Truyền tham số f, g là số thực, dùng `func (float = 0, float = 0)`
    Xuất: So thuc: 1.5 2.5

## Bài tập 3
### a. Viết chương trình nhập vào một phân số, rút gọn phân số và xuất kết quả.
### b. Viết chương trình nhập vào hai phân số, tìm phân số lớn nhất và xuất kết quả.
### c. Viết chương trình nhập vào hai phân số. Tính tổng, hiệu, tích, thương giữa chúng và xuất kết quả.
### d. Viết chương trình nhập vào một ngày. Tìm ngày kế tiếp và xuất kết quả.

## Solution: 
Ở câu a, b, c em đã tạo 1 class Fraction với parameter là tử số và mẫu số, cùng với đó là các hàm dùng để xử lý fraction theo yêu cầu của đề bài. Input nhập vào có dạng a/b, dùng split để tách ra thành tử số và mẫu số, sau đó thì thực hiện theo yêu cầu.
Ở câu d em dùng thư viện datetime, nhập vào ngày tháng theo format day/month/year, split ra và lưu vào biến datetime, cộng timeline thêm 1 ngày rồi in ra

## Bài tập 4
### Cho một danh sách lưu thông tin của các nhân viên trong một công ty, thông tin gồm:
- Mã nhân viên (chuỗi, tối đa là 8 ký tự)
- Họ và tên (chuỗi, tối đa là 20 ký tự)
- Phòng ban (chuỗi, tối đa 10 ký tự)
- Lương cơ bản (số nguyên)
- Thưởng (số nguyên)
- Thực lãnh (số nguyên, trong đó thực lãnh = lương cơ bản + thưởng )
Hãy thực hiện các công việc sau:
### a.Tính tổng thực lãnh tháng của tất cả nhân viên trong công ty.
### b.In danh sách những nhân viên có mức lương cơ bản thấp nhất.
### c.Đếm số lượng nhân viên có mức thưởng >= 1200000.
### d.In danh sách các nhân viên tăng dần theo phòng ban, nếu phòng ban trùng nhau thì giảm dần theo mã nhân viên.

## Solution:
Em đã tạo 2 class là Employee và Company để sử dụng, class Company dùng để lưu trữ số lượng nhân viên, class Employee dùng để lưu các thông tin chi tiết của từng nhân viên. Sau đó viết các hàm cơ bản trong class Company để xử lý theo yêu cầu của đề bài.