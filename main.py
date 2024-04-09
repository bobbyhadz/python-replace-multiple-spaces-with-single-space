# Replace multiple spaces with a single space in Python 

my_str = 'bobby   hadz  com'

# ✅ replace multiple whitespace characters with single space

result = " ".join(my_str.split())
print(repr(result))  # 👉️ 'bobby hadz com'