
from app import app
import webbrowser

webbrowser.open_new_tab("http://127.0.0.1:5000")

if _name_ == "_main_":
    app.run()
