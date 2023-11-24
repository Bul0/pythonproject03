#ให้ทำโปรเเกรมป้อนจำนวนเงิน เเละจำนวนคนทางเเป้นพิมพ์ เเละเเสดงผลออกมาว่า
#จำนวนเงิน ??? บาท จำนวนคน ???? คน ต้องหารกันคนละ ??? บาท
#ให้เเสดงผลโดยใช้ print ทั้ง 5 เเบบ
money = input('ป้อนจำนวนเงิน : ')
person = input ('ป้อนจำนวนคน : ')
print('..................................')
print(f'จำนวนเงิน {money}บาท จำนวนคน {person} คน ต้องหารกันคนละ {float(money)/int(person)} บาท')
print('จำนวนเงิน' ,money,' บาท จำนวนคน',person, 'คน ต้องหารกันคนละ' ,float(money)/int(person), 'บาท')
print('จำนวนเงิน' +money+ 'บาท จำนวนคน' +person+'  คน ต้องหารกันคนละ' +str(float(money)/int(person))+ 'บาท')
print('จำนวนเงิน {} บาท จำนวนคน {} คน ต้องหารกันคนละ {:.2f} บาท '.format(money,person,float(money)/int(person)))
print('จำนวนเงิน %s บาท จำนวนคน %s คน ต้องหารกันคนละ %.2f  บาท '%(money,person,float(money)/int(person)))