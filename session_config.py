from flask_session import Session

def configure_session(app):
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    app.secret_key = "teste_qi_employ"
    Session(app)