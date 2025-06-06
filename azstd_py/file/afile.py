# -*- coding: utf-8 -*-
# <-- AZLIBRARY PROJECT (Python2, 3) -->
# Started: 2018.02.02
# Latest: 2025.05.03

import os

# --- EXAMPLE ---
# <INPUT>
# fl = fileLstMaker('.', filter_=['.jpg'])
# <OUTPUT>
# ['./a.jpg', './b.jpg', './test/c.jpg', './test/test2/d.jpg', ...]
# ---------------
def fileLstMaker(folder, deep=True, filter_=None):
	# print('[Info] Building the file list of folder %s...' % folder)
	fileLst = []
	if deep:
		for root, dirs, files in os.walk(folder):
			for f in files:
				fileLst.append(os.path.join(root, f))
	else:
		files = os.listdir(folder)
		for f in files:
			fileLst.append(os.path.join(folder, f))

	if filter_ != None:
		## 2024.02.11: convert all to lower
		fileLst = filter((lambda x: os.path.splitext(x)[-1].lower() in filter_), fileLst)
	return sorted(fileLst)

# --- EXAMPLE ---
# <INPUT>
# fl = multiFileLstMaker(['.', './test'], ['.jpg'])
# <OUTPUT>
# {'.': [fileLstMaker1], './test': [fileLstMaker2], ...}
# ---------------
def multiFileLstMaker(folders, filter_=None):
	fileLst = {}
	for folder in folders:
		fileLst[folder] = fileLstMaker(folder, filter_)
	return fileLst

# --- EXAMPLE ---
# <INPUT>
# fl = classifiedFileLst('.', ['.jpg'])
# <OUTPUT>
# {'.': [fLst1],
# './001': [fLst2],
# ...}
# ---------------
def classifiedFileLst(folder, filter_=None):
	fl = fileLstMaker(folder, filter_)
	csf = {}
	for p in fl:
		[folder, fname] = os.path.split(p)
		if folder in csf.keys():
			csf[folder].append(fname)
		else:
			csf[folder] = [fname]
	return csf

# --- EXAMPLE ---
# <INPUT>
# filename_extend('a.txt', '_000', isEnd=True)
# <OUTPUT>
# 'a_000.txt'
# ---------------
def filename_extend(fname_origin, str_extend, isEnd=True):
	fname, ext = os.path.splitext(fname_origin)
	if isEnd:
		fname = fname + str_extend
	else:
		fname = str_extend + fname
	return fname + ext