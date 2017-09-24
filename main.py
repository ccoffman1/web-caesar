from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


page_header = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin 0 auto;
                width 540px;
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
"""

form = """
        <form action="/" method="POST">
            <label>
                Rotate by:
                <input type="text" name="rot" value="0" />
            </label>
            <br>

            <input type="textarea" name="text" />

            <br>
            <input type="submit" name="my-form" value="Send" />
        </form>

        <p> Encoded Text: </p>

"""    
        


page_footer = """
    </body>
</html>
"""




@app.route("/")
def my_form():
    return page_header + form + page_footer



@app.route("/", methods=['POST'])


def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    text = rotate_string(text,rot)


    return page_header + form + "<h1>" + text + "</h1>" + page_footer





app.run()