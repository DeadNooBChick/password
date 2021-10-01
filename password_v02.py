pw = 'a123456'
i = 3
int(i)
while i > 0:
	pw_in = input('請輸入密碼: ')
	if pw == pw_in:
		print('密碼正確')
		break
	else:
		i = i - 1
		print ('密碼錯誤,你還有', i, '次機會')