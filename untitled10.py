Num = input("Nhập các số bạn muốn, ngăn cách bằng dấu phẩy (viết các số và dấu phẩy liền nhau): ")
List = list(map(int, Num.split(",")))
from functools import reduce
Repeat = reduce(lambda New_List, x: New_List + [x] if x not in New_List else New_List, List, [])
#New_List này là giả sử một danh sách mới, cái danh sách mới sẽ thêm phần tử [x] vào nếu chưa có phần tử x ở trong New_List, nếu có rồi thì thôi
print(Repeat)