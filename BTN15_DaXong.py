
print("Thuật Toán Lập Lịch Firt Come Firt Serve")
n = int(input("Nhập Số Tiến Trình : "))
d = dict()

# Nhập Giữ Liệu
for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Nhập thời Gian Vào: " + str(i + 1) + ": "))
    b = int(input("Nhập Thời Gian Thực Hiện: " + str(i + 1) + ": "))
    l = [] # tạo một mảng
    l.append(a) # thêm các thời gian vào ,vào trong mảng
    l.append(b)# thêm các thời gian thực hiên vào mảng
    d[key] = l

d = sorted(d.items(), key=lambda item: item[1][0]) #sắp xếp tiến trình theo thứ tự nhập thời gian vào



ET = []   # Khởi tạo mảng chứa thời gian tiến trình hoàn thành  (Exit Time)
for i in range(len(d)):
    # Thời gian thực  hiện  = 0  thì thời gian thực hiện xong cũng = 0
    if (i == 0):
        ET.append(d[i][1][1]) # thêm dữ liệu vào mảng ET


    else:
        ET.append(ET[i - 1] + d[i][1][1])  # tính thời gian hoàn thành và lưu vào mảng
#                                               = tgian "hoàn thành " của tiến trình trước
#                                                    + Thời gian "thực hiện tiến" trình sau



TAT = []# Khởi tạo mảng chứa tổng thời gian cần để thực hiện từng tiến trình một (Turn Aroud Time)
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0]) # tongTG = thời gian "Thực Hoàn Thành" - "Thời Gian Đến"



WT = []# Khởi tạo mảng chứa thời gian đợi (Wait Time)
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])  # tính thời gian chờ đồng thời thêm vào mảng


# # thời gian chờ = thời gian "hoàn thành" của tiến trình trước - thời gian đến tiến trình sau


 #tinh thoi gian doi trung binh

avg_WT = 0
for i in WT:
    avg_WT += i
avg_WT = (avg_WT / n) # thời gian chừo trung bình  = TBC thời gian của các tiến trình



file = open("InPut.text","w") #Tạo File có tên là Input
tieude ="%13s|%20s|%25s|%30s|%30s|%15s|\n"%("Chuong Trinh","Thoi Gian Den","Thoi Gian Thuc Hien","Thoi Gian Hoàn Thành"
                                            ,"Tong Thoi Gian Can Su Dung","Thoi Gian Cho")
file.write(tieude) # ghi dữ liệu vào file
print(tieude) # in tiêu đề ra màn hình
for i in range(n):
    s = "%13s|%20s|%25s|%30s|%30s|%15s|\n"%(str(d[i][0]),str(d[i][1][0]), str(d[i][1][1]),
                                            str(ET[i]), str(TAT[i]),str(WT[i]))
    file.write(s) # Sau Khi Chạy  Sẽ Ghi Vào file
    print(s) #  Hiển Thị Dữ Liệu Ra Màn Hình

print("Thời Gian Đợi Trung Bình: ", avg_WT) # Hiển Thị Thời Gian Trung Bình
i= "Thoi Gian Doi TB:"+ str(avg_WT)     # Khởi Tạo Biến i Để Lưu Thời Gian TB của Tiến Trình Vào Trong File
file.write(i)
file.close()