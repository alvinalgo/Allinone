#遞迴刪除空資料夾 OK
#刪除小圖片 OK
#TUM小圖刪除(根據名字) OK

import os
import re
from PIL import Image

def del_small_img(pic,thdpixel): #input 圖片位址，太小的刪除
	if Image.open(pic).size[0] < thdpixel or Image.open(pic).size[1] < thdpixel: #0是寬，1是高
		os.remove(pic)
		print('刪除小圖:'+ pic)

# for f in os.listdir(path)
path = os.path.join(os.getcwd(),"mid.jpg")
del_small_img(path,300) #目前經驗用300pix當thereshold

def delete_gap_dir(dir): #遞迴刪除空資料夾
	if os.path.isdir(dir):
		for d in os.listdir(dir):
			delete_gap_dir(os.path.join(dir, d))
		if not os.listdir(dir):
			os.rmdir(dir)
			print('移除空目錄: '+dir)
delete_gap_dir(os.getcwd())
print('刪除完畢')

#還要刪除沒有影、圖的資料夾

#TUM小圖刪除
def tumblr_get_high(somedir): #刪除input資料夾內(第一層)的tumblr小圖
	tum_local_filter = re.compile('tumblr_[a-zA-Z0-9]+\_\d+\.(?:jpg|png|gif)')
	imageset = []
	tumdict = {}
	for d in os.listdir(somedir):
		x = tum_local_filter.findall(d)
		if len(x)!=0:
			imageset.append(x[0]) #輸入:str, x是長度為1的 list，內容是檔名+副檔名
	for img in set(imageset): #set裡面已經刪除重複的東西了		
		x = re.search('(tumblr_[a-zA-Z0-9]+)\_(\d+)\.((?:jpg|png|gif)+)',img)
		ID = x.group(1)
		size = x.group(2)
		sidename = x.group(3)
		if not tumdict.__contains__(ID):
			tumdict[ID] = size
			print('key:' + ID + ' / ' + 'value:' + tumdict[ID] + ' updated')
		elif int(size) > int(tumdict[ID]): #已經有了，比較新來的大小
			os.remove(os.path.join(somedir,ID+'_'+tumdict[ID]+'.'+sidename))
			tumdict[ID] = size
			print('key:' + ID + ' / ' + 'value:' + tumdict[ID] + ' updated')
		elif int(size) < int(tumdict[ID]): #本來的比較大，就不要加入
			#print('有了有了有了不要append')
			os.remove(os.path.join(somedir,img))


if __name__ == '__main__':
	path = os.getcwd()
	tumblr_get_high(path)



