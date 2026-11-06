
import pytest

from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)


# ==========================================
# CODE COVERAGE TESTS - RIDE SHARE FARE
# ==========================================


# 1. EXTRA DISTANCE FARE TESTS

def test_unknown_cab_type():
    with pytest.raises(ValueError, match="unknown cab type"):
        extra_distance_fare("bike", 10, "city", False)


def test_negative_distance():
    with pytest.raises(ValueError, match="invalid distance"):
        extra_distance_fare("mini", -5, "city", False)


def test_within_included_distance():
    assert extra_distance_fare("sedan", 5, "city", False) == 0


def test_subscriber_non_suv():
    assert extra_distance_fare("mini", 10, "city", True) == 24


def test_subscriber_suv():
    assert extra_distance_fare("suv", 15, "city", True) == 36


def test_city_fare():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_outstation_fare():
    assert extra_distance_fare("mini", 10, "outstation", False) == 90


def test_city_extra_distance_above_20():
    assert extra_distance_fare("mini", 30, "city", False) == 500


def test_outstation_extra_distance_above_20():
    assert extra_distance_fare("mini", 30, "outstation", False) == 750


# 2. SEATS AND BAGS TESTS

def test_wheelchair_passengers_allowed():
    assert seats_and_bags_ok(2, 3, True) is True


def test_wheelchair_passengers_not_allowed():
    assert seats_and_bags_ok(3, 1, True) is False


def test_more_than_four_passengers():
    assert seats_and_bags_ok(5, 1, False) is False


def test_valid_seats_and_bags():
    assert seats_and_bags_ok(4, 2, False) is True


def test_too_many_bags():
    assert seats_and_bags_ok(3, 3, False) is False


# 3. PICKUP STATUS TESTS

def test_scheduled_airport_on_time():
    assert pickup_status(20, True, True) == "on_time"


def test_non_scheduled_pickup_on_time():
    assert pickup_status(5, False, False) == "on_time"


def test_delayed_pickup():
    assert pickup_status(5, True, False) == "delayed"


def test_missed_pickup():
    assert pickup_status(-11, False, False) == "missed"
