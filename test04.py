import math
wind = float(input( 'ป้อนความกว้าง : '))
tall = float(input( 'ป้อนความสูง: '))
long = float(input('ป้อนความยาว : '))
area = 2 * (wind * tall + long * tall)
paint = math.ceil(area / 5 )
print('ความกว้าง {:.2f}เมตร ความสูง {:.2f} เมตร ความยาว {:.2f}เมตร ต้องใช้สีจำนวน{} เเกลอน'.format(wind,long,tall,paint))
print('ความกว้าง' +f'{float(wind):,.2f}'+ 'เมตร' + 'ความสูง'+f'{float(tall):,.2f}' +'เมตร ความยาว' +f'{float(tall):,.2f}' + 'เมตร ต้องใช้สี'+str(paint)+ 'เเกลอน')
print('ความกว้าง' ,f'{float(wind):,.2f}', 'เมตร' , 'ความสูง',f'{float(tall):,.2f}' ,'เมตร ความยาว' ,f'{float(tall):,.2f}' , 'เมตร ต้องใช้สี'+str(paint), 'เเกลอน')
print('ความกว้าง %s เมตร ความสูง %s เมตร ความยาว %s เมตร ต้องใช้สี %s เเกลอน'%(f'{float(wind):,.2f}',f'{float(tall):,.2f}',f'{float(tall):,.2f}',paint))
print(f'ความกว้าง {float(wind):,.2f}เมตร ยาว {float(long):,.2f}เมตร สูง{float(tall):.2f}เมตร ใช้สีจำนวน {paint}เเกลอน')