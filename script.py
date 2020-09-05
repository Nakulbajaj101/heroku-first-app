from flask import Flask, render_template

app=Flask(__name__)

@app.route('/') #home page
def home():
    return render_template("main.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/volcanoes/')
def volcanoes():
    return render_template("firstBaseMap.html")
if __name__=="__main__":
    app.run(debug=True)