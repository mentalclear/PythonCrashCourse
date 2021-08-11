# stripping from the right example
favorite_language = 'python '
print(favorite_language + "!")
print(favorite_language.rstrip() + "!")  # string is immutable.
print(favorite_language + "!")

# so the value needs to be reassigned
favorite_language = favorite_language.rstrip()
print(favorite_language + "!")

# stripping from the left
favorite_language = ' python '
print(favorite_language + "!")
favorite_language = favorite_language.lstrip()
print(favorite_language + "!")