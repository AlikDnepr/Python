empty_str = str()  # ""
print(empty_str)  #

# ASCII
print(ord("a"))
print(chr(97))

print("Hello!")
print("Hello" + " World!")
print("Hello" " World" "!")
print("Hello" * 20)

example_str = "foo"
print(len(example_str))

example_str = "0123456789"
print(example_str[0])
print(example_str[-1])
print(example_str[5])
print(example_str[9])
# print(example_str[10])  # rice IndexError exception
print(example_str[:5])
print(example_str[5:])
print(example_str[:-1])
print(example_str[:-11])  # ""
print(example_str[-3:])
print(example_str[::2])
print(example_str[::100])

d = "Hello\nWorld!"
print(d)

str1 = "this is string example....example two!!!"
str2 = "exam"

print(str2 in str1)

print(str1.replace(str2, "BOOM"))
print(str1.replace(str2, "BOOM", 1))

print("capitalize".capitalize())
print(str1.title())
print("LOWER CASE".lower())
print("upper case".upper())
print("eXaMpLe".swapcase())

print(str1.endswith("!!!"))
print(str1.startswith("this"))

print(str1.find(str2))
print(str1.find(str2, 10))
print(str1.find(str2, 16))
print(str1.rfind(str2))
print(str1.find(str2, 50))  # -1

print(str1.index(str2))
print(str1.index(str2, 10))
print(str1.index(str2, 16))
print(str1.rindex(str2))
# print(str1.index(str2, 50))  # rice ValueError exception

print(str1.count(str2))

print("".isalnum())
print("abc123".isalnum())
print("abc 123".isalnum())

print("".isalpha())
print("abcabc".isalpha())
print("abc abc!".isalpha())

print("".isdigit())
print("123".isdigit())
print("abc123".isdigit())

print("".isupper())
print("".islower())
print("UPPER CASE".isupper())
print("lower case".islower())

print("".isspace())
print("   ".isspace())

print("".istitle())
print("This is an example".istitle())


print("  \n This is an example \n  ".strip())
print("  \n This is an example \n  ".lstrip())
print("  \n This is an example \n  ".rstrip())

print("g.,typexample][3".strip("][3.,gtyp"))


# .splitlines()
multiline_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(multiline_text)
print(multiline_text.splitlines())

# .split()
example_str = "Split this line please."
print(example_str.split())

# .join()
example_list = ["Join", "this", "list", "please."]
print(" ".join(example_list))