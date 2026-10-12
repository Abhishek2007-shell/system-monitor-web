from flask import Flask,render_template
from datetime import datetime
import psutil

app = Flask(__name__)
@app.route("/")
def home():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("C:\\").percent
    cpu_alert = cpu >= 80
    memory_alert = memory >= 80
    disk_alert = disk >= 90
    last_updated = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    cpu_color = "green" if cpu < 60 else "orange" if cpu < 80 else "red"

    memory_color = "green" if memory < 60 else "orange" if memory < 80 else "red"

    disk_color = "green" if disk < 70 else "orange" if disk < 90 else "red"
   
    return render_template(
    "index.html",
    cpu=cpu,
    memory=memory,
    disk=disk,
    cpu_alert=cpu_alert,
    memory_alert=memory_alert,
    disk_alert=disk_alert,
    last_updated=last_updated,
    cpu_color=cpu_color,
    memory_color=memory_color,
    disk_color=disk_color,
)

if __name__ == "__main__":
    app.run(debug=True)