import os
import sys
import shutil
# ---------------------------------------------------------------判斷用 OK
def hello():
	print('Hey guys')

def exist_japanese(st):  #判斷字串裏頭有沒有日文
	for i in range(len(st)):
		if u'\u3040' <= st[i] <=u'\u309F' or u'\u30A0' <= st[i] <=u'\u30FF':
			return True
	else:
		return False

def exist_chinese(st):   #判斷字串裏頭有沒有中文
	for i in range(len(st)):
		if u'\u4e00' <= st[i] <=u'\u9fff':
			return True
	else:
		return False

def judgeing_video(fn): #判斷檔案是否為影片
	# video_subtitle = ('.mp4','.avi','.3gp','.wmv','.mod','.mpg','.mpeg','.mov','.rm','.rmvb','.MP4')
	for i in video_subtitle:
		if os.path.splitext(fn)[-1] == i :
			return(1)
	return(0)

def judgeing_pic(fn): #判斷檔案是否為圖片
	picture_subtitle = ('.jpg','.png','.gif','.jpeg','.bmp')
	for i in picture_subtitle:
		if os.path.splitext(fn)[-1] == i :			
			return(1)
	return(0)

# --------------------------------------------------------------- OK
def deal_with_subnames(somedir,subnames,dest): #處理副檔名，通用 OK
	if not os.path.isdir(somedir+'\\'+dest):
		os.mkdir(somedir+'\\'+dest)
	filelist = os.listdir(somedir)
	for f in filelist:
		# print(os.path.splitext(f))
		if os.path.splitext(f)[-1] in subnames:
			try:
				shutil.move(f,somedir+'\\'+dest)
			except :
				print('移動失敗檔案:'+ f)
			# if (os.path.exists(somedir+"\\rars\\"+f))!=1:
				# shutil.move(f,somedir+'\\rars') 
			# else:#它存在
				# os.remove(f) #刪掉原檔案

def deal_with_keyword(somedir,keyword,dest): #處理關鍵字，通用 OK
	if not os.path.isdir(somedir+'\\'+dest):
		os.mkdir(somedir+'\\'+dest)
	filelist = os.listdir(somedir)
	for f in filelist:
		if keyword in os.path.splitext(f)[-2]:
			try:
				# print('keyword = '+k+','+'name = '+os.path.splitext(f)[-2])
				shutil.move(f,somedir+'\\'+dest)
			except :
				print('移動失敗檔案:'+ f)

def deal_with_numofnames(somedir,num,dest): #處理檔名長度，通用OK
	if not os.path.isdir(somedir+'\\'+dest):
		os.mkdir(somedir+'\\'+dest)
	filelist = os.listdir(somedir)
	for f in filelist:
		# print(os.path.splitext(f)[-2])
		if len(os.path.splitext(f)[-2]) == num:
			try:
				shutil.move(f,somedir+'\\'+dest)
			except :
				print('移動失敗檔案:'+ f)

def deal_with_japanese(somedir): #只對第一層 移動檔案
	if not os.path.isdir(somedir+'\\FromJAP'):
		os.mkdir(somedir+'\\FromJAP')
	filelist = os.listdir(somedir)
	for f in filelist:
		if exist_japanese(f):
			try:
				shutil.move(f,somedir+'\\FromJAP') 
			except:#它存在
				print('移動失敗檔案:'+ f)
				# os.remove(f) #刪掉原檔案  #這裡刪不掉 好像是資料夾刪不掉 應該OK

def deal_with_chinese(somedir): #只對第一層 移動檔案
	if not os.path.isdir(somedir+'\\有中文檔名'):
		os.mkdir(somedir+'\\有中文檔名')
	filelist = os.listdir(somedir)
	for f in filelist:
		if exist_chinese(f):
			try:
				shutil.move(f,somedir+'\\有中文檔名') 
			except: #它存在
				print('移動失敗檔案:'+ f)

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
def del_empty_folder(somedir): #目前只刪除第一層空資料夾
	filelist = os.listdir(somedir)
	for f in filelist:
		if folder_count(os.path.join(somedir,f))[0] == 0 and os.path.isdir(os.path.join(somedir,f)):
			shutil.rmtree(os.path.join(somedir,f))

#-------------------------------------------------------------------------------------------- 
'''
def is_vango():
	('KTDS','ktds','MUM','mum','LOVE','love','FC2','fc2','259LUXU','259luxu')
	counter 3英4中
	SNIS-666
	SNIS-735
	KTDS999
	ask123
	ebod607
	nnpj
	love
	200GANA
	300
	MAAN - 027
	ipx
	mum
	KTDS939pl
	KTDS-939
	ss(小圖)不要
'''
#-------------------------------------------------------------------------------------------- 

if __name__ == "__main__": 
	pathori = os.getcwd()
	video_subtitle = ('.mp4','.avi','.3gp','.wmv','.mod','.mpg','.mpeg','.mov','.rm','.rmvb','.MP4')
	picture_subtitle = ('.jpg','.png','.gif','.jpeg','.bmp')
	print('Folder location:'+pathori)
	#-------------------------------------------------------------------副檔名處理
	# 先刪一輪空資料夾，還沒好 - 直接用檔案數判斷就好
	deal_with_subnames(pathori,['.gif','.webm','webp'],'GIFs') #gif.webm等動圖
	#-------------------------------------------------------------------特殊字串處理
	deal_with_keyword(pathori,'tumblr','Fromtumblr') 
	for w in ['_o','_n','StorySaver','FB_IMG_']: deal_with_keyword(pathori,w,'FromFBIG')
	#-------------------------------------------------------------------檔名語言分類
	deal_with_japanese(pathori)
	deal_with_chinese(pathori)
	#-------------------------------------------------------------------檔名長度處理
	deal_with_numofnames(pathori,22,'UUwukong')
	del_empty_folder(pathori)
	site = 'http://www.outofmemory.cn/'
	if "ww"  in site:
		print('site contains Words')	
	# 把numofnames移動的部分加上not is.dir


	#1.寫個函數清一輪空資料夾 2.清除太小的圖片

	
	# in html:
	# 清一輪，只留下寬跟高都>500的
	# os.path.getsize（filename）


	# 如果及時有喜歡的想打星星怎麼辦


	# >>> os.path.isdir("te")
	# >>> os.path.isfile("te")


	# 先把番號fit一個固定格式 ex:KTDS-931
    # 把番號、演遠、片名存成一個dictionary