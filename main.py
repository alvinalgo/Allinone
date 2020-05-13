from flask import Flask, render_template
import os
import dometa as do

app = Flask(__name__)
app.config['folder'] = 'static'
# app.config['folder'] = '/'

#網頁們------------------------------------------------------
@app.route('/')
def home(): #再來要把圖片做超連結
    covinfo = []
    for coll in base:
        covinfo.append(coll["cover_img"])
    # return render_template('home.html', covinfo = covinfo, title='This is home')
    return render_template('index.html', covinfo = covinfo, title='This is home')

@app.route('/test')
def test():
    testdict = [
	{
		'author': 'Lynn',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'September 3, 2018'
	},
	{
        'author': 'Lydia',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 6, 2018'
	}
    ]
    return render_template('test.html', posts=testdict, title='For test')

@app.route('/<cname>')
def pg2(cname):
    # r = 'static\\Collections\\FBIMG'
    r = os.path.join(app.config['folder'],'Collections',cname)
    return render_template('page2.html', colinfo = do.findinfo(root_pth,r), title='子網頁') #colinfo 是個dictionary

if __name__ == "__main__":
    root_pth = 'C:\\Users\\kurogikeikan\\codes\\Bootstrap project\\主程式'
    rel_lib_pth = os.path.join('static','Collections')
    do.make_metadata(root_pth,rel_lib_pth)
    base = do.read_metadata(root_pth,rel_lib_pth)
    app.run(debug=True)



