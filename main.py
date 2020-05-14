from flask import Flask, render_template
import os
import dometa as do

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))

app = CustomFlask(__name__)  # This replaces your existing "app = Flask(__name__)"
app.config['folder'] = 'static'
# app.config['folder'] = '/'

# 網頁們 ------------------------------------------------------
@app.route('/')
def home():    # 再來要把圖片做超連結

    thumbnails = {topic: topics[topic]['thumbnail'] for topic in topics}
    # return render_template('home.html', thumbnails=thumbnails, title='This is home')
    return render_template('index.html', thumbnails=thumbnails, title='This is home')

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
    return render_template('page2.html', colinfo=do.findinfo(root_path,r), title='子網頁')    # colinfo 是個 dictionary

@app.route('/metadata')
def metadata():
    return topics

# main -----------------------------------------------------
if __name__ == "__main__":
    root_path = os.getcwd()
    rel_lib_path = os.path.join('static', 'Collections')    # path of 'Collections' in the relative format

    do.make_metadata(root_path, rel_lib_path)
    topics = do.read_metadata(root_path)
    app.run(debug=True)