from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="static", template_folder="C:\Users\pawar\OneDrive\Documents\Desktop\project-root\templates")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
