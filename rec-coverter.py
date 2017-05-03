#!/usr/bin/env python
#coding: utf8

import os
import re
import subprocess

# астерикс должен писать файлы с именами двух типов:
# для очередей: main-ivr-74997070902-5623-810375177570161-1491827005.16092-20170410-15:23:42.wav
# для всех остальных: 5535-810375177570161-1491827005.16092-20170410-15:23:42.wav



sourcePath = '/var/spool/asterisk/monitor/'
#sourcePath = '/tmp/'
inputFiles = os.listdir(sourcePath)
destRootPath = '/var/www/pbx/calls/'
wavFiles = filter(lambda x: x.endswith('.wav'), inputFiles) 
#print wavs

def convert(contextPath,fromDatePath,sourceFile,desFile):
	    file[-1] = file[-1].split('.')[0]
	    mp3File =  '-'.join(file) + '.mp3'
	    mp3FilePath = destRootPath + contextPath + fromDatePath + mp3File
	    sourceFilePath = sourcePath + sourceFile
	    print sourceFilePath
	    print mp3FilePath
	    print "~~~~~~~~~~~~~~~~~~"
	    try:
	    	#pass
	    	subprocess.call('/usr/bin/lame -V3 ' + sourceFilePath + ' ' + mp3FilePath, shell=True)
	    	#AudioSegment.from_wav(sourceFilePath).export(mp3FilePath, format="mp3")
	    	#os.unlink(sourceFilePath)
	    except:
	    	if os.path.exists(destRootPath + contextPath + fromDatePath):
	    		print 'allert!'
	    	else:
	    		os.makedirs(destRootPath + contextPath + fromDatePath)
	    		subprocess.call('/usr/bin/lame -V3 ' + sourceFilePath + ' ' + mp3FilePath, shell=True)
	    		#AudioSegment.from_wav(sourceFilePath).export(mp3FilePath, format="mp3")


def prepare(file):
	count = 0
	for item in file:
		if re.search('[A-aZ-z]',item):
			count +=1
	count -= 1
	if count == 0:
		contextPath =  file[0] + '/'
	else:	
		contextPath =  '-'.join(file[:count]) + '/'
	fromDatePath = '/'.join([file[len(file)-2][:4], file[len(file)-2][4:-2]]) + '/' 
	del file[:count]
	return 	contextPath , fromDatePath , file


for files in wavFiles:
	file =  files.split('-')
	#print files
	if len(file) < 4:
		pass
	else:
		#if re.search('blind_transfer_mikhed', file[0]):
		(contextPath , fromDatePath , desFile) = prepare(file)
		convert(contextPath,fromDatePath,files,desFile)

















