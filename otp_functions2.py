import random
import time

class OTPManager:
    def __init__(self):
        self.otp_storage = {}

    def generate_otp(self, user_id, length=6):
        """Generate an OTP of the specified length and store it with a timestamp."""
        otp = ''.join(random.choices("0123456789", k=length))
        self.otp_storage[user_id] = {"otp": otp, "timestamp": time.time()}
        return otp

    def validate_otp(self, user_id, otp, validity_period=300):
        """Validate an OTP within the given validity period (default: 300 seconds)."""
        if user_id not in self.otp_storage:
            return False
        stored_otp = self.otp_storage[user_id]["otp"]
        timestamp = self.otp_storage[user_id]["timestamp"]
        if stored_otp == otp and (time.time() - timestamp) <= validity_period:
            return True
        return False

    def expire_otp(self, user_id):
        """Manually expire the OTP for a user."""
        if user_id in self.otp_storage:
            del self.otp_storage[user_id]
