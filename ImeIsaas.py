import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = ('https://www-roblcx.com/groups/5718175/DoptFuc-Store')

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra
	password = ''.join(random.choice(chars) for i in range(8))

	requests.post(url, allow_redirects = True, data = {
		'username': username,
		'password': password
	})



	print ("sending username %s and %s password" % (username,password));
