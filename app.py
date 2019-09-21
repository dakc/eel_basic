import eel
import time
import ntplib
from time import ctime
from datetime import datetime

# expose to javascript
@eel.expose
def ask_python_from_js_get_time(server):
    now_time = ""
    try:
        ntp_client = ntplib.NTPClient()
        ntp_resp = ntp_client.request(server)
        ntp_time = datetime.strptime(ctime(ntp_resp.tx_time), "%a %b %d %H:%M:%S %Y")
        now_time = ntp_time.strftime("%Y/%m/%d %H:%M:%S")
    except:
        now_time = "Woops! something went wrong."
    finally:
        # return now_time
        # call javascript function
        eel.run_js_from_python(now_time)

# initialize the folder which contents html,js,css,etc
eel.init("web")

# start app
eel.start("html/index.html")