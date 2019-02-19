import random
import string


class BaseDataGenerator:
    @staticmethod
    def generate_random_string(string_length):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(string_length))