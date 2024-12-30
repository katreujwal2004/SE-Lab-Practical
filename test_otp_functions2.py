"""
Unit tests for the OTPManager class.
This module tests OTP generation, validation, expiration, and edge cases such as invalid or expired OTPs.
"""

import time
from otp_functions import OTPManager

def test_generate_otp():
    """Test that an OTP is generated with the correct length and stored for the user."""
    otp_manager = OTPManager()
    otp = otp_manager.generate_otp("user1", length=6)
    assert len(otp) == 6
    assert otp.isdigit()
    assert "user1" in otp_manager.otp_storage

def test_validate_otp_success():
    """Test successful validation of a correct OTP."""
    otp_manager = OTPManager()
    otp = otp_manager.generate_otp("user1", length=6)
    assert otp_manager.validate_otp("user1", otp) is True

def test_validate_otp_failure_invalid_otp():
    """Test validation failure for an incorrect OTP."""
    otp_manager = OTPManager()
    otp_manager.generate_otp("user1", length=6)
    assert otp_manager.validate_otp("user1", "123456") is False, \
        "Validation should fail for an incorrect OTP"


def test_validate_otp_failure_expired_otp():
    """Test validation failure for an expired OTP."""
    otp_manager = OTPManager()
    otp = otp_manager.generate_otp("user1", length=6)
    time.sleep(2)  # Simulate a delay
    assert otp_manager.validate_otp("user1", otp, validity_period=1) is False  # OTP expired

def test_expire_otp():
    """Test manual expiration of an OTP."""
    otp_manager = OTPManager()
    otp_manager.generate_otp("user1", length=6)
    otp_manager.expire_otp("user1")
    assert "user1" not in otp_manager.otp_storage
