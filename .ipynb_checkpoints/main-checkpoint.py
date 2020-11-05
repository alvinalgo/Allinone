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

def get_default_size(size):
    if size == '-1':
        size = '25'
    return int(size)

# APIs ------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html', title='All in One')

@app.route('/bookmarks/<sorting>/<size>')
@cross_origin()
def bookmarks(sorting, size):
    size = get_default_size(size)
    if sorting == 'recents':
        result = df.sort_values('date_added', ascending=False).iloc[:size].to_dict('records')
    elif sorting == 'randoms':
        result = random.sample(bookmarks, min(len(bookmarks), size))

    return  jsonify(result)

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

@app.route('/query_a_folder/<target_index>')
@cross_origin()
def query_a_folder(target_index):
    
    if target_index == '-1':    # home
        target_name = ''
        target_list = ['1', '2', '3']
    else:
        target = df_id.loc[target_index]
        target_name = target['name']
        target_list = target['children_id']
   
    result = df_id.loc[target_list].reset_index().to_dict('records')
    return jsonify({'name': target_name, 'children': result})

@app.route('/get_parents_and_self/<target_index>')
@cross_origin()
def get_parents_and_self(target_index):
    target_list = df_id.loc[target_index]['parents']
    result = df_id.loc[target_list].reset_index().to_dict('records')
    return jsonify(result)

# main -----------------------------------------------------
if __name__ == "__main__":
    
    df = pd.read_hdf('metadata.h5')
    df_id = df.set_index('id')
    
    indicator = df['img_url'].apply(bool)
    bookmarks = df.loc[indicator].to_dict('records')    #, ['name', 'url', 'guid']].to_dict('records')

    app.run(debug=True)