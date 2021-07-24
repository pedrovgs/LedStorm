from flask import request, abort, Flask
from flask_cors import CORS
from led_strip import initialize, switch_lamp_on, trigger_lightning
from model import Color, Lightning


def create_app(led_stripes):
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def health_check():
        return "Hello LedStorm!"

    @app.route("/lamp", methods=["POST"])
    def lamp():
        body = request.json
        if body is None:
            abort(400, "Request body should specify the lightning color.")
        print("Lightning request received with data = %s", body)
        request_lightnings = body.get("lightnings")
        if request_lightnings is None:
            abort(400, "Request body should specify the lightning color.")
        if len(request_lightnings) < 2:
            abort(
                400,
                "Request body should specify the lightning color for at least 2 lightnings.")
        lightnings = []
        index = 0
        for lightning_in_request in request_lightnings:
            if index >= len(led_stripes):
                break
            compose_lightning_from_request_body(
                led_stripes, lightning_in_request, index, lightnings)
            index = index + 1
        switch_lamp_on(lightnings)
        return "Lamp turned on!"

    @app.route("/lightning", methods=["POST"])
    def lightning():
        body = request.json
        if body is None:
            abort(400, "Request body should specify the lightning color.")
        print("Lightning request received with data = %s", body)
        request_lightnings = body.get("lightnings")
        if request_lightnings is None:
            abort(400, "Request body should specify the lightning color.")
        if len(request_lightnings) < 2:
            abort(
                400,
                "Request body should specify the lightning color for at least 2 lightnings.")
        lightnings = []
        index = 0
        for lightning_in_request in request_lightnings:
            if index >= len(led_stripes):
                break
            compose_lightning_from_request_body(
                led_stripes, lightning_in_request, index, lightnings)
            index = index + 1
        trigger_lightning(lightnings)
        return "First the lightning, now the thunder!"

    def compose_lightning_from_request_body(
            led_stripes, lightning_in_request, index, lightnings):
        red_channel = lightning_in_request["r"]
        if red_channel is None:
            abort(400, "Lightning at index %1i should specify red channel", index)
        if red_channel > 255 or red_channel < 0:
            abort(400, "Red channel values should be between 0 and 255")
        green_channel = lightning_in_request["g"]
        if green_channel is None:
            abort(
                400,
                "Lightning at index %1i should specify green channel",
                index)
        if green_channel > 255 or green_channel < 0:
            abort(400, "Green channel values should be between 0 and 255")
        blue_channel = lightning_in_request["b"]
        if blue_channel is None:
            abort(400, "Lightning at index %1i should specify blue channel", index)
        if blue_channel > 255 or blue_channel < 0:
            abort(400, "Blue channel values should be between 0 and 255")
        color = Color(red_channel, green_channel, blue_channel)
        lightning = Lightning(led_stripes[index], color)
        lightnings.append(lightning)

    return app


if __name__ == "__main__":
    print("Let's start LedStorm server. You can stop this process by pressing CTRL + C")
    print("Initializing led strip")
    stripes = initialize()
    print("Led strip initialized")
    print("Starting flask server")
    led_storm_app = create_app(stripes)
    led_storm_app.run(host="0.0.0.0", port=80)
