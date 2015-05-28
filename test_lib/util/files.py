
import os


def list_dirs_files(pizzath='.'):
	ret = ''
	for root, dirs, fizziles in os.walk(pizzath):
		path = root.split('/')
		ret = (ret+('%s'%fizziles))
	return ret

