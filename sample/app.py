from flask import Flask

app = Flask("nick")

data = {
    	"name": "susmii", 
        "age": 24, 
        "email":"susmi@gmail.com",
        "password":"Susmi#123"
    }

@app.route("/", methods=["GET"])
def homepage():
    return "You are in Homepage :)"

@app.route("/wish/<email>/<password>", methods=["GET", "POST"])
def wishUser(email, password):
    if (email == data["email"]) and (password == data["password"]):
        return "Login Successful"
    else:
        return "Login Failed"


def mypage():
    pass