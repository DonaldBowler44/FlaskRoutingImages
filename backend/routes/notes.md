# upload = Upload(filename=file.filename, data=file.read())

<!-- <a href="{{ url_for('upload.serve_image', filename=image) }}" target="_blank"> -->

https://stackoverflow.com/questions/24577349/flask-download-a-file

https://www.reddit.com/r/flask/comments/5vul37/ask_flask_how_do_i_store_in_a_database_the/

https://flask.palletsprojects.com/en/0.12.x/patterns/fileuploads/

https://stackoverflow.com/questions/42036285/downloading-file-using-flask



<div class="app">
    <div class="images-section">

        {% for image in images %}
        <!-- <a href="{{ url_for('upload.serve_image', filename=image) }}" target="_blank"> -->
          <img src="{{ url_for('upload.single_image', filename=image) }}"/>
        <!-- </a> -->
        {% endfor %}
        
      </div>
    </div>


//{% set my_image = site.get('/myfolder').attachments.get('imagenameexample.jpg') %}

https://stackabuse.com/get-request-query-parameters-with-flask/

https://www.codegrepper.com/code-examples/python/flask+image+in+get+parameters

https://stackoverflow.com/questions/12034949/flask-how-to-get-url-for-dynamically-generated-image-file

https://pythonbasics.org/flask-template-data/

https://www.delftstack.com/howto/python-flask/flask-url_for/










