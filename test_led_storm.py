# pylint: skip-file
from led_storm import show_lightning_if_needed
import pytest

def test_triggers_lightingn_if_distance_is_zero(mocker):
    spy = mocker.patch("led_storm.trigger_lightning")
    mocker.patch("led_storm.measure_distance_from_sensor", return_value=0)

    lightning_shown = show_lightning_if_needed()

    assert spy.call_count == 1
    assert lightning_shown == True

def test_does_not_trigger_lightingn_if_distance_is_far_enough(mocker):
    spy = mocker.patch("led_storm.trigger_lightning")
    mocker.patch("led_storm.measure_distance_from_sensor", return_value=51)

    lightning_shown = show_lightning_if_needed()

    assert spy.call_count == 0
    assert lightning_shown == False


def test_does_not_trigger_lightingn_if_distance_is_lower_than_zero(mocker):
    spy = mocker.patch("led_storm.trigger_lightning")
    mocker.patch("led_storm.measure_distance_from_sensor", return_value=-1)

    lightning_shown = show_lightning_if_needed()

    assert spy.call_count == 0
    assert lightning_shown == False


def test_triggers_lightingn_if_distance_is_close_enough(mocker):
    spy = mocker.patch("led_storm.trigger_lightning")
    mocker.patch("led_storm.measure_distance_from_sensor", return_value=50)

    lightning_shown = show_lightning_if_needed()

    assert spy.call_count == 1
    assert lightning_shown
