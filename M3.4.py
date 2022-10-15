
import json
data_pass = {'testlog':'testpasswd'}
with open('pass.json', 'w') as f:
	json.dump(data_pass, f)
secret_info = 'Давайте будем изучать Pyton вместе'

def order_pass():
	with open('pass.json', 'r') as f:
		data_pass = json.load(f)
while True:
	q1 = input('Вход или регистрация?')
	if q1 == 'вход':
		log = input('Введите логин: ')
		passwd = input('Введите пароль: ')
		if log in data_pass.keys():
			if data_pass[log] == passwd:
				print('Успешный вход!')
				print(secret_info)
		else:
			print('Неверный логин')
	elif q1 == 'регистрация':
		log = input('Введите логин: ')
		passwd = input('Введите пароль: ')
		if log in data_pass.keys():
			print('Логин занят')
		else:
			data_pass[log] = passwd
			print('Регистрация успешна')
		with open('pass.json', 'a') as f:
			json.dump(data_pass, f)


