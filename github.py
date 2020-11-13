from flask import Flask,render_template,request
import requests

app = Flask(__name__)
url_without_api = "https://api.github.com/users/"

@app.route("/" , methods = ["GET","POST"])
def index():
    if request.method == "POST":
        git_user = request.form.get("git_user")
        user_response = requests.get(url_without_api+git_user)
        json_info = user_response.json()

        repo_response = requests.get(url_without_api+git_user+"/repos")
        json_repos = repo_response.json()

        if "message" in json_info:
            return render_template("index.html", error = "Ups ! User not found.")
        else:
            return render_template("index.html",profile = json_info , repo_info=json_repos)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)