from flask import Flask, render_template
import os


app = Flask(__name__)
app.config['folder'] = 'static'


@app.route('/')
def home(): #直接拿base裡的資料，看之後要不要做隨機
    covinfo = [] #render進去的是一個list 隨便挑幾個網址
    for coll in base:
        covinfo.append(coll["cover_img"])    
    return render_template('bookmark_home.html', covinfo = covinfo, title='This is home')

@app.route('/<cname>')
def pg2(cname):
    info = mybookmarkinfo[cname]
    return render_template('bookmamrk_page2.html', colinfo = do.findinfo(root_pth,r), title='子網頁') #colinfo 是個dictionary

in bookmamrk_page2.html: 
第一區放該網址的縮圖
第二區:
recommendation system推薦類似的


if __name__ == "__main__": #處理書籤的時候:
    mybookmarkinfo = json.loads(檔案路徑) #load自己的dictionary
    googlebookmarkinfo = loads(input_file.read()) #load chrome那邊

    for 每個書籤: #開啟時先遍歷書籤
        if 沒封面(書籤網址不在key裡面):
        每個書籤load 封面，檔名再想想，都存到同一個資料夾好了 C槽or和mybookmarkinfo同個地方
        路徑存在另一個dictionary - mybookmarkinfo:
            key: 書籤網址
            value: 也是dictionary: ex:
                {'thumbroute':'C:\\example.png','tags':['學業用','休閒用'],'similar one':['http:eyny','https:keep.com']}
        
    app.run(debug=True)
'''
    註:現在有的東西:
    1.load書籤得到的dictionary
    2.mybookmarkinfo
'''


