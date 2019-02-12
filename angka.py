#!/usr/bin/python

# angka = ['10','8','7','5']
op = ['+','-','*','/']

# temp = angka[0]

# for i in range(1,len(angka)):
# 	kecil = op[0] + angka[i]
# 	# print angka[i]
# 	for j in range(1,len(op)):
# 		if(abs(eval(temp+op[j]+angka[i])-24) < abs(eval(temp+kecil)-24)):
# 			kecil = op[j] + angka[i]

# 		temp += kecil

# 		if(temp[-2] == '+'  or temp[-2] == '-'):
# 			temp = '(' + temp + ')'


# print temp
# print eval(temp)


sauce = raw_input("what's it m'lord ")
angka = sauce.split(' ')

angka = [int(i) for i in angka]
angka.sort()
angka = [str(i) for i in angka]
angka = angka[::-1]
#baru

temp = [angka[0]]

for a in range(1,len(angka)):
	minim = op[0]
	for o in range(1,len(op)):
		if(abs(eval(''.join(temp) + op[o] + angka[a])-24) < abs(eval(''.join(temp) + minim + angka[a])-24)):
			minim = op[o]

	temp.append(minim)
	temp.append(angka[a])

	if(minim == '+' or minim == '-'):
		if(a < 3):
			temp.insert(0,'(')
			temp.append(')')

result = ''.join(temp)

if('*' not in result and '/' not in result):
	result = result.replace('(','')
	result = result.replace(')','')

print result
print eval(''.join(temp))