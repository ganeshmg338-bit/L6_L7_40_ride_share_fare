
from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)


# ==========================================
# BRANCH COVERAGE TESTS - RIDE SHARE FARE
# ==========================================


# 1. EXTRA DISTANCE FARE

def test_unknown_cab():
    try:
        extra_distance_fare("bike", 10, "city", False)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_valid_cab():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_negative_distance():
    try:
        extra_distance_fare("mini", -1, "city", False)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_non_negative_distance():
    assert extra_distance_fare("mini", 5, "city", False) == 0


def test_subscriber_true():
    assert extra_distance_fare("mini", 10, "city", True) == 24


def test_subscriber_false():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_suv_subscriber():
    assert extra_distance_fare("suv", 15, "city", True) == 36


def test_extra_distance_zero():
    assert extra_distance_fare("mini", 5, "city", False) == 0


def test_extra_distance_positive():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_city_zone():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_non_city_zone():
    assert extra_distance_fare("mini", 10, "outstation", False) == 90


def test_extra_distance_above_20():
    assert extra_distance_fare("mini", 30, "city", False) == 500


def test_extra_distance_below_20():
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_outstation_above_20():
    assert extra_distance_fare("mini", 30, "outstation", False) == 750


# 2. SEATS AND BAGS

def test_wheelchair_true():
    assert seats_and_bags_ok(2, 3, True) is True


def test_wheelchair_false():
    assert seats_and_bags_ok(2, 1, False) is True


def test_wheelchair_passengers_exceeded():
    assert seats_and_bags_ok(3, 1, True) is False


def test_passengers_above_four():
    assert seats_and_bags_ok(5, 1, False) is False


def test_passengers_within_limit():
    assert seats_and_bags_ok(4, 1, False) is True


def test_bags_within_limit():
    assert seats_and_bags_ok(3, 2, False) is True


def test_bags_above_limit():
    assert seats_and_bags_ok(3, 3, False) is False


# 3. PICKUP STATUS

def test_scheduled_pickup():
    assert pickup_status(10, True, False) == "on_time"


def test_non_scheduled_pickup():
    assert pickup_status(5, False, False) == "on_time"


def test_airport_pickup():
    assert pickup_status(20, False, True) == "on_time"


def test_non_airport_pickup():
    assert pickup_status(5, False, False) == "on_time"


def test_on_time_boundary():
    assert pickup_status(10, True, False) == "on_time"


def test_delayed_boundary():
    assert pickup_status(-4, True, False) == "delayed"


def test_missed_pickup():
    assert pickup_status(-6, True, False) == "missed"
