import os
import sys
import shutil

#-------------------------------------------------------------------------------------------- OK
def judgeing_video(fn):
	for i in video_subtitle:
		if os.path.splitext(fn)[-1] == i :
			return(1)
	return(0)
def judgeing_pic(fn):
	for i in picture_subtitle:
		if os.path.splitext(fn)[-1] == i :			
			return(1)
	return(0)
#-------------------------------------------------------------------------------------------- OK
def folder_count(somedir): #return總共data數,圖片數,影片數
	data_count = 0
	video_count = 0
	picture_count = 0
	for dirPath, dirNames, fileNames in os.walk(somedir):
		# print(dirPath) #print資料夾路徑
	    for f in fileNames:
			# print(os.path.join(dirPath, f)) #全檔案的全路徑
	        if  judgeing_pic(f):
	        	picture_count+=1
	        elif judgeing_video(f):
	        	video_count+=1
	        data_count+=1
	return(data_count,picture_count,video_count)
def def_empty_folder(somedir): #目前只刪除第一層空資料夾
	filelist = os.listdir(somedir)
	for f in filelist:
		if folder_count(os.path.join(somedir,f))[0] == 0 and os.path.isdir(os.path.join(somedir,f)):
			shutil.rmtree(os.path.join(somedir,f))
#-------------------------------------------------------------------------------------------- 
def deal_with_comics(somedir):
	if not os.path.isdir(somedir+'\\(0)中文aH漫'):
		os.mkdir(somedir+'\\(0)中文aH漫')
	if not os.path.isdir(somedir+'\\(0)真人a蘿莉萌'):
		os.mkdir(somedir+'\\(0)真人a蘿莉萌')
	if not os.path.isdir(somedir+'\\(0)歐美a少女'):
		os.mkdir(somedir+'\\(0)歐美a少女')
	if not os.path.isdir(somedir+'\\(0)本地a美女'):
		os.mkdir(somedir+'\\(0)本地a美女')
	if not os.path.isdir(somedir+'\\(0)UP貼圖'):
		os.mkdir(somedir+'\\(0)UP貼圖')
	if not os.path.isdir(somedir+'\\(0)悟kong貼圖'):
		os.mkdir(somedir+'\\(0)悟kong貼圖')
	filelist = os.listdir(somedir)
	for f in filelist:
		if f.find('中文H漫畫貼圖') != -1:
			try:
				shutil.move(f,somedir+'\\(0)中文aH漫') 
			except:#它存在
				# os.remove(f) #刪掉原檔案	
				print('移動失敗檔案:'+ f)
		if f.find('真人蘿莉萌') != -1:
			try:
				shutil.move(f,somedir+'\\(0)真人a蘿莉萌') 
			except:#它存在
				# os.remove(f) #刪掉原檔案	
				print('移動失敗檔案:'+ f)
		if f.find('歐美少女') != -1:
			try:
				shutil.move(f,somedir+'\\(0)歐美a少女') 
			except:#它存在
				# os.remove(f) #刪掉原檔案
				print('移動失敗檔案:'+ f)
		if f.find('本地美女') != -1 or f.find('明星走光') != -1 or f.find('正妹美眉區') != -1:
			try:
				shutil.move(f,somedir+'\\(0)本地a美女') 
			except:#它存在
				# os.remove(f) #刪掉原檔案
				print('移動失敗檔案:'+ f)
		if f.find('UP01') != -1:
			try:
				shutil.move(f,somedir+'\\(0)UP貼圖') 
			except:#它存在
				# os.remove(f) #刪掉原檔案
				print('移動失敗檔案:'+ f)
		if f.find('wukong') != -1 or f.find('悟空') != -1:
			try:
				shutil.move(f,somedir+'\\(0)悟kong貼圖') 
			except:#它存在
				# os.remove(f) #刪掉原檔案
				print('移動失敗檔案:'+ f)

def trash_detect_del(file): #自動刪除廢物檔案
	if is.file(file):
		if is.picture(file):
			if 寬高任一<321:
				os.rm(file)
		elif not 影or html or txt:
			os.remove(file)

有'avatar'的必須刪
.js.下載


if __name__ == "__main__": 
	pathori = os.getcwd()
	print('Folder location:'+pathori)
	#-------------------------------------------------------------------開始處理
	deal_with_comics(pathori)


	# comic_writer_splitting() #分作家
	# 一個漫畫弄成一個html檔
	# 最後弄成一個html介面，點開圖就能看該漫畫(html)