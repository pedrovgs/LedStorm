import time
from led_strip import initialize, trigger_lightning
from rpi_ws281x import Color
from flask import Flask, request, jsonify

print("Let's start LedStorm server. You can stop this process by pressing CTRL + C")
print ("Initializing led strip")
stripes = initialize()
print ("Led strip initialized")
print ("Starting flask server")
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    body = request.json
    print ("Lightning request received with data = %s", body)
    lightning = body["lightnings"][0] 
    color = Color(lightning["r"], lightning["g"], lightning["b"])
    trigger_lightning(stripes, color)
    return 'First the lightning, now the thunder!'

app.run(host='0.0.0.0', port=80)