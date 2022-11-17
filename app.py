import json
from flask import Flask,request


app = Flask(__name__)
my_data=[{"s1":"idan"},{"s2":"matan"},{"s3":"or"}]

def load_json():
    f = open('sample.json')
    data = json.load(f)

@app.route("/")
def home():
    return '<h1>please type your request in the URL'


@app.route("/data/<ind>")
@app.route("/data/")
def students(ind=-1):
    if int(ind) < 0:
        return my_data
    else:
        return my_data[int(ind)]

@app.route("/add/", methods=['POST'])
def add_student():
        # get the data from user
        data= request.json
        print(data["name"])
        print(data["age"])
        my_data.append({len(my_data):data['name']})
        save_json()
        load_json()
        return "student added"

@app.route("/del/<ind>", methods=['DELETE'])
def del_student(ind=-1):
        if int(ind) > -1:
            my_data.pop(int(ind))
        return "student del"

@app.route("/upd/<ind>", methods=['PUT'])
def upd_student(ind=-1):
        if int(ind) > -1:
            print(ind)
            data= request.json
            my_data[int(ind)]={len(my_data):data['name']}
        return "student update"

def save_json():
    json_object = json.dumps(my_data, indent=4)
 
# Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)



app.run(debug=True)