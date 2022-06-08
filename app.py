from flask import Flask

from flask import request, render_template

import re

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("email_text.html")
@app.route("/email", methods=["GET", "POST"])
def emails():
    if request.method == "POST":
        def listToString(s): 
            str1 = " ," 
            return (str1.join(s))
        data = request.form['data']
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", data)
        data = listToString(emails)
        return render_template("email_text.html", list=data)



if __name__ == "__main__":
    app.run()