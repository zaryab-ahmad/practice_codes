import random , string 

strings = """!@#$%^&*()QWERTYUIOPASDFGHJKL:"ZXCVBNM<>?zxcvbnm,./asdfghjkl;'qwertyuiop[]1234567890-=\""""
password = ''.join(random.choice(strings) for password in range(12))
print(password)