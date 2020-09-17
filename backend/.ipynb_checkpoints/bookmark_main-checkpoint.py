from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['folder'] = 'static'

@app.route('/')
def home(): #直接拿base裡的資料，看之後要不要做隨機
    covinfo = [] #render進去的是一個list 隨便挑幾個網址
    for coll in base:
        covinfo.append(coll["cover_img"])    
    return render_template('bookmark_home.html', covinfo=covinfo, title='This is home')

@app.route('/subpage/<cname>')
def subpage(cname):
    info = mybookmarkinfo[cname]
    return render_template('bookmamrk_page2.html', colinfo=do.findinfo(root_pth,r), title='子網頁')
    #colinfo 是個dictionary

    # in bookmamrk_page2.html: 
    # 第一區放該網址的縮圖
    # 第二區:
    # recommendation system 推薦類似的

if __name__ == "__main__":    # 處理書籤的時候:
    # mybookmarkinfo = json.loads(檔案路徑)    # load已有的database
    googlebookmarkinfo = load_bookmarks(XDD)    # load chrome 那邊, 會是一個 
    dataframe
    app.run(debug=True)

    ## load thumb_imgs
    for idx,xxx in enumerate(googlebookmarkinfo): # 開啟時先遍歷書籤
        if 沒封面: #和已有的database比對，之後再做
            # 每個書籤load封面，檔名可用 id or guid，都存到同一個資料夾            
            route = download_thumb_img(googlebookmarkinfo['url'][idx]) # ex: 'C:/example.png'
            thumb_routes.append(route)
    googlebookmarkinfo['thumb_img_route'] = thumb_routes # list of route後再append進去data_frame
    
    

to-do:
web_page
1. UI

bookmark_dealing
1.download_thumb_img()
2.recommendation system to get similar one

