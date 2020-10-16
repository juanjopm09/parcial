#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
studentsDB = [
 {
 'id':'T00055671',
 'name':'Juan Perez',
 'course':'Machine Learning'
 },
 {
 'id':'T00045678',
 'name':'Maria Martinez',
 'course':'Software Engineer'
 }
 ]

@app.route('/students/',methods=['GET'])
def get_all_students():
    return jsonify({'students': studentsDB})

@app.route('/students/<stdId>',methods=['GET'])
def get_students(stdId):
    usr = [std for std in studentsDB if (std['id'] == stdId)]
    return jsonify({'est': usr})

@app.route('/students/<stdId>',methods=['PUT'])
def update_students(stdId):
    row = [est for est in studentsDB if (est['id'] == stdId)]
    if 'name' in request.json:
        row[0]['name'] = request.json['name']
    if 'course' in request.json:
        row[0]['course'] = request.json['course']
    return jsonify({'est': row[0]})

@app.route('/students/',methods=['POST'])
def create_student():
    dat = {
    'id': request.json['id'],
    'name': request.json['name'],
    'course': request.json['course']
    }
    studentsDB.append(dat)
    return jsonify(dat)

@app.route('/students/<stdId>',methods=['DELETE'])
def deleteEmp(stdId):
    row = [est for est in studentsDB if (est['id'] == stdId)]
    if len(row) == 0:
       abort(404)
    studentsDB.remove(row[0])
    return jsonify({'response': 'Success'})

if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:


pip install Flask


# In[ ]:




