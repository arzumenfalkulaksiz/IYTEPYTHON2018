import string
import random
m=''.join(random.choice(string.ascii_uppercase) for _ in range(5))
print(m)
if (m==m[::-1]):
	print ('Bu text bir palindromdur.')
else:
	print('Bu text bir polindrom degildir.')