import os
import re
import random
import pickle

import pandas as pd

from flask import Flask, render_template, jsonify
from flask_cors import cross_origin

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',    # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))

app = CustomFlask(__name__, static_url_path='')    # This replaces your existing "app = Flask(__name__)"
app.config['debug'] = True


# 網頁們 ------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html', title='All in One')

@app.route('/randoms')
@cross_origin()
def randoms():
    sample = random.sample(bookmarks, min(len(bookmarks), 18))
    return  jsonify(sample)

@app.route('/folders')
@cross_origin()
def folders():
    result = df[df['type'] == 'folder'].to_dict('records')
    return  jsonify(result)

@app.route('/full_list')
@cross_origin()
def full_list():
    result = df.sort_values(['type', 'date_added'], ascending=[True, False]).to_dict('records')
    return  jsonify(result)

@app.route('/explorer')
@cross_origin()
def explorer():
    
    target_index = ''
    
    if target_index == '':
        result = df_id.loc[['1', '2', '3']].to_dict('records')
        return jsonify(result)
    else:
        result = df_id.loc[target_index].to_dict('records')
        return jsonify(result)


# main -----------------------------------------------------
if __name__ == "__main__":
    
    df = pd.read_hdf('metadata.h5')
    df_id = df.set_index('id')
        
    indicator = df['img_url'].apply(bool)
    bookmarks = df.loc[indicator].to_dict('records')    #, ['name', 'url', 'guid']].to_dict('records')

    app.run(debug=True)