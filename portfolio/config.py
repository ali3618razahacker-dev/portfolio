"""ALL editable portfolio content lives here. Leave a URL as "" and its link stays hidden.
Never put a URL for something that doesn't exist yet."""
import os, secrets

BASE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(BASE, "instance"), exist_ok=True)

def _secret():
    if os.environ.get("SECRET_KEY"):
        return os.environ["SECRET_KEY"]
    p = os.path.join(BASE, "instance", "secret_key")
    if not os.path.exists(p):
        open(p, "w").write(secrets.token_hex(32))
    return open(p).read().strip()

SECRET_KEY = _secret()
DATABASE = os.path.join(BASE, "instance", "messages.db")

PROFILE = {
    "name": "Ali",
    "location": "Lahore, Pakistan",
    "tagline": "Python Developer | Web Developer | Game Dev | Cybersecurity Enthusiast",
    "intro": "I'm still learning, and I build things to understand how technology works underneath: web apps, networking tools, games and small hardware experiments.",
    "about": [
        "I'm a young aspiring software developer from Lahore. I like taking things apart, writing small tools, and finding out why they work.",
        "Alongside my technical studies I'm learning a traditional trade, which keeps me practical. My goal is to become capable at building useful software, earn through technical work, and one day start my own software house.",
        "I'm not a senior developer or a professional pentester. I'm a learner with hands-on experiments and a clear direction.",
    ],
    "email": "",      # EMAIL_ADDRESS
    "github": "",     # GITHUB_URL
    "linkedin": "",   # LINKEDIN_URL
    "youtube": "",    # YOUTUBE_URL
    "profile_image": "",  # e.g. "images/me.jpg" inside /static
}

SKILLS = {
    "Languages & Web": [("Python", "Intermediate"), ("Flask", "Learning"), ("Django", "Intermediate familiarity"), ("HTML / CSS / JS", "Basic"), ("Git & GitHub", "Basic")],
    "Systems & Security": [("Linux (Mint)", "Basic"), ("Cybersecurity", "Basic"), ("Networking / sockets", "Basic")],
    "Making Things": [("Godot (GDScript)", "Basic"), ("ESP32", "Beginner"), ("PC & laptop repair", "Basic"), ("AI & automation", "Exploring")],
}

# status: "Working" | "In progress" | "Concept" | "Experiment" | "Learning lab". Be honest.
PROJECTS = [
    {"title": "ESP32 Web GPIO Controller", "status": "Experiment", "tech": ["ESP32", "C++", "HTML/JS"],
     "desc": "An ESP32 hosts a Wi-Fi access point called ESP32-Control and serves a browser panel that switches GPIO pin 14 on and off. Experimental groundwork for IoT, not a smart-home product.",
     "repo": "", "demo": "", "image": ""},
    {"title": "Godot 3D Movement Prototype", "status": "Experiment", "tech": ["Godot", "GDScript"],
     "desc": "Basic 2D/3D games: CharacterBody3D movement, jumping, gravity, collisions and scene reloading.",
     "repo": "", "demo": "", "image": ""},
    {"title": "CLI Password Journal", "status": "Concept", "tech": ["Python", "File I/O"],
     "desc": "A command-line journal organising entries by date, title and content. No encryption is claimed.",
     "repo": "", "demo": "", "image": ""},
    {"title": "LAN File Transfer Tool", "status": "Concept", "tech": ["Python", "Sockets"],
     "desc": "A learning project on moving files between devices on one local network.",
     "repo": "", "demo": "", "image": ""},
    {"title": "TCP Chat Application", "status": "Learning lab", "tech": ["Python", "TCP", "Threading"],
     "desc": "Client-server chat to learn networking fundamentals and concurrent connections. Not production-grade.",
     "repo": "", "demo": "", "image": ""},
    {"title": "Expense Tracker", "status": "Concept", "tech": ["Python", "Matplotlib"],
     "desc": "Reads expense records, totals by category, finds the largest expense and handles malformed rows.",
     "repo": "", "demo": "", "image": ""},
    {"title": "Flask & Django Web Apps", "status": "Experiment", "tech": ["Flask", "Django", "SQL"],
     "desc": "Practice with login systems, database-backed apps, APIs and e-commerce layouts, partly AI-assisted. Not launched products.",
     "repo": "", "demo": "", "image": ""},
    {"title": "Cybersecurity & Linux Labs", "status": "Learning lab", "tech": ["Linux", "Networking"],
     "desc": "Finished Linux Basics for Hackers and reached about level 22 on OverTheWire Bandit. Lab practice, not professional pentesting.",
     "repo": "", "demo": "", "image": ""},
    {"title": "PC & Laptop Troubleshooting", "status": "Hands-on", "tech": ["Hardware", "Linux"],
     "desc": "Diagnosing faults, upgrading parts and replacing components, sometimes with AI help. No professional certification.",
     "repo": "", "demo": "", "image": ""},
]

JOURNEY = ["Python fundamentals and small scripts", "Networking: sockets, LAN tools, chat", "Linux and security lab practice",
           "Flask and Django web experiments", "Godot games and ESP32 hardware experiments", "AI workflow automation (exploring)"]

SERVICES = ["Python scripts and small automations", "Basic web development and website improvements", "Simple Flask/Django tools", "Basic PC and laptop troubleshooting"]
