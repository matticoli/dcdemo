from flask import Flask, render_template
import psutil
from datetime import datetime
import json 

app = Flask(__name__)

df = {
    "cpu": [-1],
    "disk": [-1],
    "mem": [-1],
    "neti": [-1],
    "neto": [-1],
    "temp": [-1],
}

LOOP_TIME = datetime.now().timestamp()

def loop():
    if (datetime.now().timestamp() - LOOP_TIME) < 1000:
        df["cpu"] = [psutil.cpu_percent()]
        df["disk"] = [psutil.disk_usage("/").percent]
        df["mem"] = [psutil.virtual_memory().percent]
        df["neti"] = [psutil.net_io_counters().bytes_recv]
        df["neto"] = [psutil.net_io_counters().bytes_sent]
        if "sensors_temperature" in vars(psutil):
            df["temp"] = [psutil.sensors_temperature(fahrenheit=True)]
        t = datetime.now().timestamp()

@app.route("/")
def demo():
    loop()
    return render_template("./dcdemo.html", **{
        "cpu": df["cpu"][-1],
        "disk": df["disk"][-1],
        "temp": df["temp"][-1],
        "mem": df["mem"][-1],
        "neti": df["neti"][-1],
        "neto": df["neto"][-1],
        "data": json.dumps(df)
    })

    
app.run(host="0.0.0.0", debug=True)