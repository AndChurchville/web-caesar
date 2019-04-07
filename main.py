from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <!-- create your form here -->
            <form action="/" method="POST">
            <label for="rot">Rotate By:</label>
            <input type="text" name="rot" id="rot" value="0">
            <textarea name="text" id="text"></textarea>
            <button type="sumbit">Submit Text</button>
        </body>
    </html>
    """


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST']) 
def encrypt():
    rotation_value = int(request.form["rot"])
    user_text = request.form["text"]
    encrypted = rotate_string(user_text, rotation_value)
    result = "<h1>" + encrypted + "</h1>"
    return result

app.run()