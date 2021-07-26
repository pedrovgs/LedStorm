# pylint: skip-file
from model import Color, Lightning
from led_storm_server import create_app
import pytest

STRIPES = ["strip1", "strip2"]


def test_health_check():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_static_js_files():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/32ad95b9cf9832e7.js')
        assert response.status_code == 200

def test_static_wasm_files():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/77f0df3d5db9f6a4.wasm')
        assert response.status_code == 200

def test_does_not_show_ligtning_if_request_body_is_empty():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 400


def test_does_not_show_ligtning_if_request_body_is_malformed():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/', json={"light": []})
        assert response.status_code == 400


def test_does_not_show_ligtning_if_request_does_not_specify_at_least_two_lightnings():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.post('/', json={"lightnings": []})
        assert response.status_code == 400


def test_does_not_show_ligtning_if_request_contains_only_one_lightning_info():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.post(
            '/', json={"lightnings": [{"r": 255, "g": 255, "b": 255}]})
        assert response.status_code == 400


def test_does_not_show_ligtning_if_request_values_are_out_of_rgb_range():
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.post(
            '/', json={"lightnings": [{"r": 255, "g": 255, "b": 255}, {"r": 255, "g": 255, "b": 300}]})
        assert response.status_code == 400


def test_shows_lightning_using_the_request_params_if_the_body_is_valid(mocker):
    spy = mocker.patch("led_storm_server.trigger_lightning")
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        response = test_client.post(
            '/', json={"lightnings": [{"r": 255, "g": 255, "b": 255}, {"r": 255, "g": 255, "b": 255}]})
        assert spy.call_count == 1
        assert response.status_code == 200


def test_uses_request_params_to_define_lightnings(mocker):
    spy = mocker.patch("led_storm_server.trigger_lightning")
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        lightning_1 = {"r": 1, "g": 2, "b": 3}
        lightning_2 = {"r": 4, "g": 5, "b": 6}
        request_body = {"lightnings": [lightning_1, lightning_2]}

        response = test_client.post('/', json=request_body)

        expected_lightning_1 = Lightning(
            STRIPES[0],
            Color(
                lightning_1["r"],
                lightning_1["g"],
                lightning_1["b"]))
        expected_lightning_2 = Lightning(
            STRIPES[1],
            Color(
                lightning_2["r"],
                lightning_2["g"],
                lightning_2["b"]))
        expeted_trigger_param = [expected_lightning_1, expected_lightning_2]
        assert response.status_code == 200
        spy.assert_called_once_with(expeted_trigger_param)


def test_ignores_other_lightning_definitions_after_the_second_one(mocker):
    spy = mocker.patch("led_storm_server.trigger_lightning")
    flask_app = create_led_storm_app()
    with flask_app.test_client() as test_client:
        lightning_1 = {"r": 1, "g": 2, "b": 3}
        lightning_2 = {"r": 4, "g": 5, "b": 6}
        lightning_3 = {"r": 7, "g": 8, "b": 9}
        request_body = {"lightnings": [lightning_1, lightning_2, lightning_3]}

        response = test_client.post('/', json=request_body)

        expected_lightning_1 = Lightning(
            STRIPES[0],
            Color(
                lightning_1["r"],
                lightning_1["g"],
                lightning_1["b"]))
        expected_lightning_2 = Lightning(
            STRIPES[1],
            Color(
                lightning_2["r"],
                lightning_2["g"],
                lightning_2["b"]))
        expeted_trigger_param = [expected_lightning_1, expected_lightning_2]
        assert response.status_code == 200
        spy.assert_called_once_with(expeted_trigger_param)


def create_led_storm_app():
    return create_app(STRIPES)
