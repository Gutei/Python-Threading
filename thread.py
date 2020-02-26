from threading import Thread
import time

a = {}

def test_thread(q):
	i = 0
	while True:
		i += 1
		time.sleep(.009)

		a['{}{}'.format(i, q)] = i

def main():
	daftarList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	for i in daftarList:
		Thread(target=test_thread, args=i).start()
	while True:
		print(a)

if __name__ == '__main__':
	main()
