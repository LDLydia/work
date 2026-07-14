quantity = int(input("จำนวนปืนที่รับมาขาย (กระบอก): "))
cost_price = int(input("ต้นทุนของปืนที่รับมา (บาท/กระบอก): "))
sell_price = int(input("ราคาที่จะนำไปขายต่อ (บาท/กระบอก): "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน (คน): "))

print("-------------------------------------------")

total = quantity * cost_price
total_sell = sell_price * quantity
profit = total_sell - total
boss = profit * 20/100
last = profit - boss
final = last / team_members

print(f"""ต้นทุน {total} บาท \n 
      รายรับทั้งหมด {total_sell} บาท \n 
      กำไรสุทธิ {profit} บาท \n 
      จำนวนเงินที่หักให้บอส {boss} บาท 
      จำนวนเงินที่ลูกน้องแต่ละคนได้ {final} บาท""")
