import random
from datetime import datetime

def generate_tracking_number():
    """
    Example:
    LGS20260629124587
    """
    date = datetime.now().strftime("%Y%m%d")
    random_number = random.randint(100000, 999999)

    return f"LGS{date}{random_number}"
