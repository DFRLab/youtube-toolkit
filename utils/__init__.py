# -*- coding: utf-8 -*-

# Import modules
import time

'''

Creating functions

'''

# new line
def nl():
	print ('')

# preparing driver
def preparing_driver():
	'''
	'''
	nl()
	print ('> Preparing driver...')
	time.sleep(10)
	print ('> done.')
	nl()

# get access to goggle's account manually
def sign_in_process():
	'''
	'''
	nl()
	print ("> Get access to Goggle's account manually...")
	sign_in_response = ' '.join(
		input('> Sign in completed? [Y]/N: ').lower().split()
	).strip()
	while sign_in_response != 'y':
		sign_in_response = ' '.join(
			input('> Sign in completed? [Y]/N: ').lower().split()
		).strip()

