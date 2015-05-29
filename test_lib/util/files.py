
import os

"""
	Utils for file operations
"""

def list_dirs_files(path='', file_scope=None):
	if file_scope is None:
		file_scope = os.path.abspath(__file__)
	path  = '%s%s'%(file_scope, path)
	return ', '.join(os.listdir(path))

