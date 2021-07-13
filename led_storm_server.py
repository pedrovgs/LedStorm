import time
from led_strip import initialize, trigger_lightning
from model import Color, Lightning
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
    lightnings = []
    index = 0
    for lightningRequest in body["lightnings"]:
        color = Color(lightningRequest["r"], lightningRequest["g"], lightningRequest["b"])
        lightning = Lightning(stripes[index], color)
        lightnings.append(lightning)
        index = index + 1
    
    trigger_lightning(lightnings)
    return 'First the lightning, now the thunder!'

app.run(host='0.0.0.0', port=80)