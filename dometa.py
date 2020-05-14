# 確定 OK
import os
import json
import local_data_dealing.name_dealing as nd


def make_metadata(root_path, rel_lib_path):
    def get_metadata_from_path(root_path, rel_col_path):
        """find the metadata of some folder.
        """
        try:
            full_path = os.path.join(root_path, rel_col_path)    # absolute route
            print('full_path:', full_path)

            topic = {
                'thumbnail': 'a',
                'imgs': [],
                'description': 'This is collection description',
                'tags': ['Bad','Taiwan','Oldman']
            }

            filelist = os.listdir(full_path)
            topic['thumbnail'] = os.path.join(rel_col_path, filelist[0])    # 這邊找封面可以修正
            for f in filelist:
                if nd.judgeing_pic(f):
                    topic['imgs'].append(os.path.join(rel_col_path, f))
            return topic
        except:    # error usually for favicon.ico
            print('--------------findinfo error--------------')
            print('root_path:', root_path)
            print('rel_col_path:', rel_col_path)
            pass
    
    topic_path = os.path.join(root_path, rel_lib_path)
    folderlist = next(os.walk(topic_path))[1]
    print(topic_path, folderlist)
    topics = {folder: get_metadata_from_path(root_path, os.path.join(rel_lib_path,folder))
                    for folder in folderlist}
    with open('metadata.json', 'w', encoding='utf8') as f:
        json.dump(topics, f)
        
def read_metadata(root_path):
    metadata_path = os.path.join(root_path, 'metadata.json')
    with open(metadata_path, encoding='utf8') as f:
        j = json.load(f)
    return j