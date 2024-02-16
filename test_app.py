import pytest

from app import validate_email_address


def test_valid_email_addresses():
    assert validate_email_address("example@example.com")
    assert validate_email_address("user.name+tag+sorting@example.com")
    assert validate_email_address("x@example.com")
    assert validate_email_address("example-indeed@strange-example.com")
    assert validate_email_address("email@example.co.uk")

def test_invalid_email_addresses():
    assert not validate_email_address("plainaddress")
    assert not validate_email_address("@missingusername.com")
    assert not validate_email_address("Joe Smith <email@example.com>")
    assert not validate_email_address("email.example.com")
    assert not validate_email_address("email@example@example.com")
    assert not validate_email_address(".email@example.com")
    assert not validate_email_address("email.@example.com")
    assert not validate_email_address("email..email@example.com")
    assert not validate_email_address("あいうえお@example.com")
    assert not validate_email_address("email@example.com (Joe Smith)")
    assert not validate_email_address("email@-example.com")
    assert not validate_email_address("email@example..com")

def test_edge_case_email_addresses():
    assert not validate_email_address("email@example")
    assert not validate_email_address("email@.com")
    assert not validate_email_address("@")
    assert not validate_email_address("email@.com.my")
    assert not validate_email_address("email@example.web")
    assert not validate_email_address("email@111.222.333.44444")
    assert not validate_email_address("email@example..com")
    assert not validate_email_address("email@.example.com")
    assert not validate_email_address("email@example_com")
    assert not validate_email_address("email@-example-.com")
