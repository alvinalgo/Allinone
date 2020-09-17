import os
import re
import random

import pandas as pd

from flask import Flask, render_template, jsonify
from flask_cors import cross_origin

# import dometa as do

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',    # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))

app = CustomFlask(__name__, static_url_path='')    # This replaces your existing "app = Flask(__name__)"
# app.config['folder'] = '/'
app.config['folder'] = 'static'
app.config['debug'] = True


# 網頁們 ------------------------------------------------------
@app.route('/')
def home():    # 再來要把圖片做超連結
    return render_template('index.html', title='This is home')

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

@app.route('/subpage/<cname>')
def subpage(cname):
    # r = 'static\\Collections\\FBIMG'
    r = os.path.join(app.config['folder'], 'Collections', cname)
    return render_template('page2.html', colinfo=do.findinfo(root_path, r), title='子網頁')    # colinfo 是個 dictionary

@app.route('/metadata')
@cross_origin()
def metadata():
    img_list = os.listdir('static/images')
    img_list = [img for img in img_list if not re.match('^\..*', img)]
    sample = random.sample(img_list, min(len(img_list), 18))
    result = [f'http://127.0.0.1:5000/images/{s}' for s in sample]
    
    return  jsonify(result)#{'list': bookmarks[:9]})

# main -----------------------------------------------------
if __name__ == "__main__":
    
    df = pd.read_hdf('metadata.h5')
    bookmarks = df[['name', 'url', 'img_url']].to_dict('records')
    # print(bookmarks[:9])
    
#     do.make_metadata(root_path, rel_lib_path)
#     topics = do.read_metadata(root_path)
    app.run(debug=True)