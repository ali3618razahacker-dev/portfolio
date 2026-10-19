import re, secrets, sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax", MAX_CONTENT_LENGTH=32 * 1024)
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def db():
    c = sqlite3.connect(config.DATABASE)
    c.execute("CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY, name TEXT, email TEXT, message TEXT, created TEXT DEFAULT CURRENT_TIMESTAMP)")
    return c

def token():
    session.setdefault("csrf", secrets.token_hex(16))
    return session["csrf"]

@app.context_processor
def inject():
    return dict(P=config.PROFILE, csrf_token=token)

@app.route("/")
def index():
    return render_template("index.html", skills=config.SKILLS, projects=config.PROJECTS, journey=config.JOURNEY, services=config.SERVICES)

@app.route("/contact", methods=["POST"])
def contact():
    f = request.form
    if not secrets.compare_digest(f.get("csrf", ""), session.get("csrf", "x")):
        flash("Session expired. Please try again.", "error")
    elif f.get("website"):  # honeypot
        flash("Message sent.", "ok")
    else:
        n, e, m = f.get("name", "").strip(), f.get("email", "").strip(), f.get("message", "").strip()
        if not (2 <= len(n) <= 80) or not EMAIL_RE.match(e) or len(e) > 120 or not (10 <= len(m) <= 2000):
            flash("Please enter a name, a valid email and a message of 10-2000 characters.", "error")
        else:
            try:
                with db() as c:
                    c.execute("INSERT INTO messages(name,email,message) VALUES(?,?,?)", (n, e, m))
                flash("Thanks! Your message was saved. It is stored locally and is not emailed automatically.", "ok")
            except sqlite3.Error:
                flash("Could not save your message. Please try again later.", "error")
    return redirect(url_for("index") + "#contact")

@app.errorhandler(404)
def nf(_):
    return render_template("404.html"), 404

@app.errorhandler(413)
def big(_):
    flash("Message too large.", "error")
    return redirect(url_for("index") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)
