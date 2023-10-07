def func (**args):
	return args

print (func (short='dict', longer='dictionary'))

add = lambda x, y: x * y
print (add (2, 5))
print (add ('q', 5))

print ((lambda x, y: x * y)(2, 6))

fun = lambda *args: args
print (fun (2, 56, 78.56))


def speed (km, hour = 1):
    a = km * hour
    return a

otvet = speed(int(input('Скорость - ')), int(input('Время - ')))
km = str((lambda a: "километр" if a == 1 else "километров")(otvet))
print ("Вы проедете: " + str(otvet) + " " + km)