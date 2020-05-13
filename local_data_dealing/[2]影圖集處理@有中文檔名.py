import os
import sys
import shutil


def walktry(somedir):
	for x in os.walk(somedir):
		print(x)
def is_trash(fn):
	for x in trashwords:
		if fn.find(x) != -1:
			print(x)
			return(1)
	return(0)
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
#-------------------------------------------------------------------------------------------- 主體
def movingchall(somedir): #主體 - 分幾影幾圖移動資料夾
	filelist = os.listdir(somedir)
	if not os.path.isdir(somedir+'\\圖Collection'): #創圖Collection資料夾
		os.mkdir(somedir+'\\圖Collection')
	if not os.path.isdir(somedir+'\\1影多圖'): #創1影多圖資料夾
		os.mkdir(somedir+'\\1影多圖')
	if not os.path.isdir(somedir+'\\2影以上'): #創2影以上
		os.mkdir(somedir+'\\2影以上')
	#-----------------------------
	for f in filelist: #對第一層掃描
		# print(os.path.join(somedir,f))
		if f in ['1影多圖','2影以上','圖Collection']:
			print('跳過三本柱資料夾')
			continue
		fd_count = folder_count(os.path.join(somedir,f))
		# print(folder_count(os.path.join(somedir,f))) #印出圖片影片數目&總數
		if fd_count[0]!=0 and os.path.isdir(os.path.join(somedir,f)):#資料夾有東西且為一個資料夾非檔案
			if fd_count[2] == 0: #沒有影片只有照片，先整個弄到子資料夾再MOVE到圖collection	
				for dirPath, dirNames, fileNames in os.walk(os.path.join(somedir,f)): #for 所有子資料夾裡的圖
					for cf in fileNames:
						try:
							shutil.move(os.path.join(dirPath,cf),os.path.join(somedir,f)) #全部移動到該子資料夾
						except:
							pass
				try:
					shutil.move(os.path.join(somedir,f),somedir+'\\圖collection')
				except:
					print("已有檔案")
				continue
			if fd_count[2] == 1: #1影
				if fd_count[1] < 7: #1影少圖，命名後全拿出來
					pic_rename_count = 1
					for dirPath, dirNames, fileNames in os.walk(os.path.join(somedir,f)): #for 所有子資料夾裡的圖
						for cf in fileNames:
							if judgeing_pic(cf):
								# print('XXXXXXXXXXXXXXXXXX這裡是1影少圖XXXXXXXXXXXXXXXXXXXXXX')
								# print(os.path.join(dirPath,cf))
								if(os.path.isfile(os.path.join(somedir,f+str(pic_rename_count)+os.path.splitext(cf)[-1]))):
									os.remove(os.path.join(somedir,f+str(pic_rename_count)+os.path.splitext(cf)[-1]))
								os.rename(os.path.join(dirPath,cf),f+str(pic_rename_count)+os.path.splitext(cf)[-1]) #圖片命名後自動搬到getcwd
								pic_rename_count += 1
							elif judgeing_video(cf):
								if(os.path.isfile(os.path.join(somedir,f+os.path.splitext(cf)[-1]))):
									os.remove(os.path.join(somedir,f+os.path.splitext(cf)[-1]))
								os.rename(os.path.join(dirPath,cf),f+os.path.splitext(cf)[-1]) #影片命名後會自動搬到getcwd
					continue				
					# for fouttomo in os.listdir(os.path.join(somedir,f)): #子資料夾裡的全部移動到母目錄(getcwd) #rename已經做好了@@
					# 	if os.path.isdir(fouttomo) == 0:
					# 		shutil.move(os.path.join(somedir,f,fouttomo),somedir)
					# 		print('就是我')
				else : #1影多圖，先整個弄到子資料夾再MOVE到圖1影多圖
					for dirPath, dirNames, fileNames in os.walk(os.path.join(somedir,f)):
						for cf in fileNames:
							try:
								shutil.move(os.path.join(dirPath,cf),os.path.join(somedir,f)) 	#全部移動到該子資料夾
							except:
								pass
					try:
						shutil.move(os.path.join(somedir,f),somedir+'\\1影多圖')
					except:
						print("已有檔案")
					continue
			if fd_count[2] > 1: #2影以上全部不要動，全都弄到下一層目錄→資料夾放到2影以上資料夾
				for dirPath, dirNames, fileNames in os.walk(os.path.join(somedir,f)): #for 所有子資料夾裡的圖
					for cf in fileNames:
						try:
							shutil.move(os.path.join(dirPath,cf),os.path.join(somedir,f)) 	#全部移動到該子資料夾
						except:
							pass
					try:
						shutil.move(os.path.join(somedir,f),somedir+'\\2影以上')	
					except:
						pass									
				continue		
#--------------------------------------------------------------------------------------------
def first_trash_fish(somedir): #處理宣傳、附送、url、html刪除、新建文件夾、魚訊、宣传
	filelist = os.listdir(somedir)
	for dirPath, dirNames, fileNames in os.walk(somedir): #for 所有檔案
		for cf in fileNames:
			if is_trash(cf):
				print('拉基',cf)
				#os.remove(os.path.join(somedir,f))
	# shutil.move(os.path.join(somedir,f),somedir+'\\圖collection')

#--------------------------------------------------------------------------------------------
if __name__ == "__main__": 
	pathori = os.getcwd()
	global video_subtitle,picture_subtitle
	video_subtitle = ('.mp4','.avi','.3gp','.wmv','.mod','.mpg','.mpeg','.mov','.rm','.rmvb','.MP4')
	picture_subtitle = ('.jpg','.png','.gif','.jpeg','.bmp')
	trashwords = ('宣傳','附送','新建文件夾','魚訊','宣传','url')#'html'看看要不要
	print('Folder location:'+pathori)
	#----------------------------------------------------------------------------------------
	# first_trash_fish(pathori) 把圖跟影綁在一起好做刪除?之後挑選用?
	movingchall(pathori)
	def_empty_folder(pathori)
	# walktry(pathori)
	# os.path.getsize（filename）
	# os.remove(f) #刪掉原檔案	