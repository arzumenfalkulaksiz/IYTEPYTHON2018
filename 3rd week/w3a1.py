from datetime import datetime
import random
year=random.choice(range(0,3000))
print(year)
if ('int(year)/400'.isdigit() or 'int(year)/4'.isdigit() or int(year)/100==float):
	print ('Bu bir artik yildir.')
else:
	print('Bu bir normal yildir.')
