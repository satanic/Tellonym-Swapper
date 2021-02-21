try:
	import requests
	import json
	from bs4 import BeautifulSoup
	import time
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)
except Exception as m:
	print("Something Went Wrong\n")
	print(m)
	input()
	exit()

co = 0
ff = 0
a = requests.session()

print("""
    ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
    ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
    ╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
    ░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
                              """, Fore.GREEN+"Credit @_agf - Soud#0737")
print(Fore.GREEN+"Tellonym Swap By Soud (Beta V0.3)")
noe = int(input(Fore.GREEN+"[Choose Mode]\n1) Login\n2) Login With Auth-Header\n>> "))
if noe == 1:
	username = input("\nUsername: ")
	password = input("Password: ")
	head = {
		'accept': 'application/json',
		'content-type': 'application/json;charset=utf-8',
		'origin': 'https://tellonym.me',
		'referer': 'https://tellonym.me/login',
		'tellonym-client': 'web:0.52.0',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1'
		}
	
	data = '{"deviceName":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Ve","deviceType":"web","lang":"en","captcha":"03AGdBq27dExbYY_tzKOIyeSMt0izSzNSiaJGJy9M0QZlhWlOV2RV7fzEfNOfYdJZ8sS6xBHaOQyZ-f-hi9PJp2-WoDTn6_6K0vjeLv09DHV3u3U6miPWCGCn_uZ7tsFDq8rDc7D14OR0eoW4DgmY6RfASu8ZfyYYAjDyRrl3to3wWyrpWE5fa3EK6V-R4UaZLuZPw7qtigL30yoqvgTL0S7CIubS7_9BHgRZVL37vOjA99qvPkiJAsf75TM0KNrNIZy1NelkmSQfc-ViElYgW3yBs6EzSnxhwpnEyljIXS3nvHDhmqWKvI8AajSGk2cQYFxslLYPNJmmnIqgCT6BYOzmUhiJr7ueFm7jNvQ1qLQh_qcBTGCqBoOFwMPnbrT3fkLkSIPW3hK-PiNdRrfwRguB9hVrwR0PNaZ4yMtG4fwGfiEwpjQyC9-DjP_3kpLoK1nW1INtIlu7yJzKlQFggAKS0R-VZDyLhkQ","email":"يوزرك","password":"باسك","limit":25}'
	
	req = a.post('https://api.tellonym.me/tokens/create', data=data, headers=head)
	if "Wrong credentials" in req.text:
		print(Fore.RED+"[-] Failed Login >> ", username)
		time.sleep(5)
		exit()
	elif "accessToken" in req.text:
		print(Fore.GREEN+"[+] Logged In >> ", username)
		t = json.loads(req.text)
		token = t["accessToken"]
		target = str(input("Target: "))
		input("Are You Ready? Click [Enter]")
		urll = "https://api.tellonym.me/accounts/settings"
		headd = {
		"Authorization": f"Bearer {token}",
		'accept': 'application/json',
		'content-type': 'application/json;charset=utf-8',
		'origin': 'https://tellonym.me',
		'referer': 'https://tellonym.me/login',
		'tellonym-client': 'web:0.52.0',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1'
		}
		dataa = {
			"snapchat":"",
			"displayName":"Soud69 Swap",
			"tintColor": 0,
			"twitter":"",
			"aboutMe":"Soud Was Here",
			"limit": 16,
			"username": target,
			"instagram":"_agf"
			}
		while 1:
			reqq = a.post(urll, json=dataa, headers=headd)
			if "Username is already in use. Please choose another one" in reqq.text:
				co += 1
				print(Fore.GREEN+f"Attempt {co} Spam {ff} User: {username}")
			elif "Ratelimit reached. Slow down" in reqq.text:
				print(Fore.RED+"[-] Blocked, Try again Later >> ", username)
				time.sleep(5)
				exit()
			else:
				co += 1
				print(Fore.GREEN+f"Swapped Done: {username} Attempt: {co}")
				print(Fore.GREEN+"Swap By\nhttps://instagram.com/_agf\nhttps://t.me/Soud69\nhttps://github.com/Soud69\nBye")
				break
		else:
			print("Error: ")
			print(req.text)
elif noe == 2:
	token = str(input("Enter Auth Token: "))
	headd = {
		"Authorization": f"Bearer {token}",
		'accept': 'application/json',
		'content-type': 'application/json;charset=utf-8',
		'origin': 'https://tellonym.me',
		'referer': 'https://tellonym.me/login',
		'tellonym-client': 'web:0.52.0',
		'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1'
	}
	gg = a.get("https://api.tellonym.me/accounts/myself?limit=25", headers=headd)
	if "TOKEN_INVALID" in gg.text:
		print(Fore.RED+"Wrong Token, Closing")
		time.sleep(3)
		exit()
	elif "displayName" in gg.text:
		print(Fore.GREEN+"Correct Token, Swapping now")
	username = str(input("Enter Your Username: "))
	target = str(input("Target: "))
	input("Are You Ready? Click [Enter]")
	urll = "https://api.tellonym.me/accounts/settings"
	headd = {
		"Host": "api.tellonym.me",
		"Accept": "application/json",
		"tellonym-client": "ios:2.63.5:481:14:iPhone13,3",
		"Authorization": f"Bearer {token}",
		"Accept-Language": "en-us",
		"Accept-Encoding": "gzip, deflate, br",
		"Content-Type": "application/json;charset=utf-8",
		"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
		"Connection": "keep-alive"
}
	dataa = {
		"snapchat":"",
		"displayName":"Soud69 Swap",
		"tintColor": 0,
		"twitter":"",
		"aboutMe":"Soud Was Here",
		"limit": 16,
		"username": target,
		"instagram":"_agf"
		}
	while 1:
		reqq = a.post(urll, json=dataa, headers=headd)
		if "Username is already in use. Please choose another one" in reqq.text:
			co += 1
			print(Fore.GREEN+f"Attempt {co} Spam {ff} User: {username}")
		elif "Ratelimit reached. Slow down" in reqq.text:
			print(Fore.RED+"[-] Blocked, Try again Later >> ", username)
			time.sleep(5)
			exit()
		else:
			co += 1
			print(Fore.GREEN+f"Swapped Done: {username} Attempt: {co}")
			print(Fore.GREEN+"Swap By\nhttps://instagram.com/_agf\nhttps://t.me/Soud69\nhttps://github.com/Soud69\nBye")
else:
	print("Wrony Mode, closing")
	exit()
