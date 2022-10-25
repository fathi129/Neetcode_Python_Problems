from flask import Flask,request,jsonify,json

app = Flask(__name__)

hello_list = ["Hello","World!!"]
hello_dict = {"Name":"Apple"}

@app.route('/')
def hello():
    return("Hello World..!!!")

@app.route('/jsondata')
def json_data():
    return jsonify(hello_dict)

@app.route('/listdata')
def list_data():
    return jsonify(hello_list)

@app.route('/normal')
def normal_list():
    return str(hello_list)

@app.route("/postdata",methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"






# @app.route('/postdata',methods=['POST'])
# def process_json():
#     content_type = request.headers.get()



if __name__ == "__main__": 
    app.run(debug=True)   
