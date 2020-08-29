import random
import string

def create_random_url():
    return "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(30)
    )
