def Reverse(str):
	if str == '':
		return str

	else:
		return Reverse(str[1:]) + str[0]

print(Reverse('Live not on evil'))
