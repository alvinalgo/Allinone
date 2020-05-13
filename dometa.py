#確定OK
import os
import io
import json
import local_data_dealing.name_dealing as nd

def findinfo(root_pth,rel_col_pth):
    try:
        absrou = os.path.join(root_pth,rel_col_pth)
        print('absrou:',absrou)
        colinfo = {
            'cover_img': 'a',
            'imgs':[],
            'descript': 'This is collection description',
            'tags': ['Bad','Taiwan','Oldman'],
        }
        filelist = os.listdir(absrou)
        colinfo['cover_img'] = os.path.join(rel_col_pth,filelist[0]) #這邊找封面可以修正
        for f in filelist:
            if nd.judgeing_pic(f):
                colinfo['imgs'].append(os.path.join(rel_col_pth,f))
        return(colinfo)
    except: #error usually for favicon.ico
        print('--------------findinfo error--------------')
        print('root_pth:',root_pth)
        print('rel_col_pth:',rel_col_pth)
        pass
def makejson(somedir,info): #info:#dictionary
    submit = os.path.join(somedir,'metadata.json') #讀取回原來的檔案路徑
    with io.open(submit, 'w', encoding='utf8') as f:
        json.dump(info, f, ensure_ascii=False)
def loadmeta(somedir):
    json_filename = os.path.join(somedir,'metadata.json')
    with open(json_filename , 'r',encoding = 'utf8') as reader:
        jf = json.loads(reader.read()) #dictionary
    return(jf)
def make_metadata(root_pth,rel_lib_pth):
    ing = os.path.join(root_pth,rel_lib_pth)
    folderlist = os.listdir(ing)
    for f in folderlist:
        print(f) #只會有資料夾、檔案名
        makejson(os.path.join(ing,f),findinfo(root_pth,os.path.join(rel_lib_pth,f)))
def read_metadata(root_pth,rel_lib_pth):
    base = []
    ing = os.path.join(root_pth,rel_lib_pth)
    folderlist = os.listdir(ing)
    for f in folderlist:
        rr = os.path.join(ing,f)
        tt = loadmeta(rr)
        # print(tt) #成功了
        base.append(tt)
    # print(base[0]) #dictionary
    return base #list of dictionary

if __name__ == "__main__":
    root_pth = 'C:\\Users\\kurogikeikan\\codes\\Bootstrap project\\主程式'
    rel_lib_pth = os.path.join('static','Collections')
    # make_metadata(root_pth,rel_lib_pth)
    base = read_metadata(root_pth,rel_lib_pth)

