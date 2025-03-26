from flask import Flask, render_template
import psutil
import matplotlib
import matplotlib.ticker as mtick
from pandas import DataFrame as DF

app = Flask(__name__)

@app.route("/")
def demo():
    print(psutil.net_io_counters().bytes_sent)
    return render_template("./dcdemo.html", **{
        "cpu": str(psutil.cpu_percent()),
        "disk": str(psutil.disk_usage("/").percent),
        "mem": psutil.virtual_memory().percent,
        "net": f"{psutil.net_io_counters().bytes_sent} {psutil.net_io_counters().bytes_recv}",
        
    })
    
app.run(debug=True)