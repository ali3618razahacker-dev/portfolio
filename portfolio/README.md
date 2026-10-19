# Ali's Portfolio (Flask)

## Setup (Linux Mint)
    sudo apt install python3-venv -y
    cd portfolio
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py
Open http://127.0.0.1:5000

## Notes
- **Internet needed for the 3D scene:** Three.js (r128) loads from cdnjs. Offline or without WebGL, a CSS fallback shows instead. For full offline use, download three.min.js into `static/js/` and point `index.html` at it.
- **All content** (bio, skills, projects, links) is in `config.py`. Empty URLs hide their links. Fill in `email`, `github`, `linkedin`, `youtube` there.
- **Images:** put files in `static/images/` and set e.g. `"image": "images/shot.png"` on a project, or `profile_image`. Use real screenshots only.
- **Project status** is a field. Change `Concept` to `Working` only when the code really runs, and add `repo`/`demo` only when they exist.
- **Contact form:** CSRF token, honeypot and server-side validation. Messages go to SQLite (`instance/messages.db`) and are NOT emailed. Read them with:
      sqlite3 instance/messages.db "select * from messages;"
- Secret key is generated into `instance/secret_key` (git-ignored) or taken from `SECRET_KEY`.
- **Deploy later:** use gunicorn (`pip install gunicorn; gunicorn app:app`) on PythonAnywhere, Render or a VPS. Set `SECRET_KEY` and turn off debug.
