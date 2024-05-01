from flask import Flask, request ,render_template

import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyAWOaPiHaD6r-iAYfcyoHQAGk5k4pESSPw",
  'authDomain': "bookstore-d7ad5.firebaseapp.com",
  'projectId': "bookstore-d7ad5",
  'storageBucket': "bookstore-d7ad5.appspot.com",
  'messagingSenderId': "971926094812",
  'appId': "1:971926094812:web:51b2fe0150d99984540519",
  'measurementId': "G-PWWSJK8SJY"
};

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
  if request.method == 'POST':
    bookname = request.form['bookname']
    filename = request.form['filename']
    cloudfilename = request.files['cloudfilename']
    pdf_path = 'books/'+ cloudfilename.filename
    cloudfilename.save(pdf_path)
    name = pdf_path
    db.child('users').push({'name': bookname, 'filename': filename}) 
    
    storage.child(filename).put(name)
    url = storage.child(filename).get_url(None)
    print(url)

    users = db.child('users').get()
    user = users.val()
    return render_template('index.html',u = user.values(), download_url=url)
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)