import tinify
import glob
import os

tinify.key = '****************' # replace your key

def zip_down(img_name):
	try:
		source = tinify.from_file(img_name)
		source.to_file(img_name)
		print(img_name, 'success')
	except Exception as e:
		print(img_name, e)

def main():
	files = glob.glob('*.*')
	for f in files:
		if f[-2:] == 'py':
			continue
		zip_down(f)
	input('process success')
	os.remove('tinyjpg.py')
main()