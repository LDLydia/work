quantity = int(input("จำนวนปืนที่รับเข้ามา: "))
cost_price = int(input("ต้นทุนของปืนที่รับเข้ามา: "))
sell_price = int(input("ราคาที่จะนำไปขายต่อ: "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน "))

tontun = quantity * cost_price
sellgun = quantity * sell_price
real_income = quantity * sell_price - quantity * cost_price
total_boss = real_income *(20/100)
total_minion1 = real_income - total_boss
total_minion2 = total_minion1 / team_members

print(f"ต้นทุนทั้งหมด {tontun} บาท")
print(f"รายรับทั้งหมด {sellgun} บาท")
print(f"รายได้สุทธิ {real_income} บาท")
print(f"จำนวนเงินที่หักให้บอส { total_boss } บาท")
print(f"จำนวนเงินที่ลูกน้องแต่ละคนจะได้ { total_minion2 } บาท")