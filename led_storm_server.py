from flask import Flask, request
from led_strip import initialize, trigger_lightning
from model import Color, Lightning

print("Let's start LedStorm server. You can stop this process by pressing CTRL + C")
print("Initializing led strip")
stripes = initialize()
print("Led strip initialized")
print("Starting flask server")
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    body = request.json
    print("Lightning request received with data = %s", body)
    lightnings = []
    index = 0
    for lightning_request in body["lightnings"]:
        color = Color(
            lightning_request["r"],
            lightning_request["g"],
            lightning_request["b"])
        lightning = Lightning(stripes[index], color)
        lightnings.append(lightning)
        index = index + 1

    trigger_lightning(lightnings)
    return 'First the lightning, now the thunder!'


app.run(host='0.0.0.0', port=80)
