name = input("ชื่อ: ")
age = int(input("อายุ: "))
height = int(input("ส่วนสูง: "))
power_level = int(input("ระดับพลัง 1-10: "))
starter_pack_dollar = int(input("เงินติดตัว: "))

if age < 18:
    print("ไม่ผ่าน")
    print("อายุน้อยเกินไป")

elif height < 160:
    print("ไม่ผ่าน")
    print("ส่วนสูงไม่ถึงเกณฑ์")

elif starter_pack_dollar < 1000:
    print("ไม่ผ่าน")
    print("เงินติดตัวไม่พอ")

elif power_level <= 3:
    print("ไม่ผ่าน")
    print("พละกำลังน้อยเกินไป")

elif power_level <= 5:
    print(f"{name} ผ่านการคัดเลือก")
    print("ตำแหน่ง : คนเฝ้าประตู")

elif power_level <= 7:
    print(f"{name} ผ่านการคัดเลือก")
    print("ตำแหน่ง : ลูกน้อง")

elif power_level <= 9:
    print(f"{name} ผ่านการคัดเลือก")
    print("ตำแหน่ง : มือขวาบอส")

else:
    print(f"{name} ผ่านการคัดเลือก")
    print("ตำแหน่ง : บอสใหญ่")