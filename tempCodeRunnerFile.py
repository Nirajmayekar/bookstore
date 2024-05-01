
    cloudfilename = request.files['cloudfilename']
    pdf_path = 'books/'+ cloudfilename.filename
    cloudfilename.save(pdf_path)
    name = pdf_path
    db.child('users').push({'name': bookname, 'filename': filename}) 
    
    storage.child(filename).put(name)
    url = storage.child(filename).get_url(None)