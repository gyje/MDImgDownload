import re
import os
import requests
import sys
import shutil
import time

md_file = sys.argv[1]

dir_base = f'./{md_file[0:-3]}/'

def findall_img(md_file):
	img_patten = r'\!\[.*\]\(.+\)'
	fob = open(md_file, 'r', encoding = 'utf-8')
	content = fob.read()
	matches = re.compile(img_patten).findall(content)
	fob.close()
	return matches
	
def imgDownload(img_name, img_type, img_url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	}
	if not os.path.exists(dir_base):
		os.mkdir(dir_base)
	fob = open(dir_base + f'{img_name}.' + img_type, 'wb')
	fob.write(requests.get(img_url, headers = headers).content)
	fob.close()
	
def parse_img(img_md):
	img_type = 'jpg'
	name_patten = r'\!\[.*\]'
	url_patten = r'!\[.*?\]\((.*?)\)'
	for k in ['.jpg' , '.jpeg' , '.png' , '.gif' , '.bmp']:
		if k in img_md:
			img_type = k[1:]
			break
	img_name = re.compile(name_patten).findall(img_md)[0][2:-1]
	if img_name == '':
		img_name = str(int(time.time()));print('fuck!图不命名')
	img_url = re.compile(url_patten).findall(img_md)[0]
	return img_name, img_type, img_url

def replace_md(str, old, new):
	return str.replace(old, new)
	
def main():
	fob = open(md_file, 'r', encoding = 'utf-8')
	content = fob.read()
	fob.close()
	for img_md in findall_img(md_file):
		img_name = parse_img(img_md)[0]
		img_type = parse_img(img_md)[1]
		img_url = parse_img(img_md)[2]
		imgDownload(img_name, img_type, img_url)
		new_img_md = '![' + img_name + '](/static/img/' + md_file[0:-3] + '/' + img_name + '.' + img_type + ')'
		content = replace_md(content, img_md, new_img_md)
	with open(md_file, 'w', encoding = 'utf-8') as fob:
		fob.write(content)
	shutil.copy('tinyjpg.py', dir_base)
	os.startfile(md_file[0:-3])
main()