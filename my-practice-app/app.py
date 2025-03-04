from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/test")
def test():
    return "ok"

@app.route("/saveUser")
def saveUser():
    
    id = request.args.get('id')
    pw = request.args.get('pw')

    return "ok"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/id-class")
def id_class():
    return render_template("id-class.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/front")
def front():
    return render_template("front.html")

@app.route("/js-basic")
def js_basic():
    return render_template("js-basic.html")

@app.route("/detail-todo")
def detail_todo():
    
    todo_id = request.args.get('todoid')

    
    return render_template(
            "detail-todo.html",
            todo_id=todo_id
        )

if __name__ == "__main__":
    app.run(debug=True)
