default_int_val = int()
print(default_int_val)  # 0

int_in_str_val = "10"
print(int(int_in_str_val))  # 10
print(int(int_in_str_val, 2))  # 2
print(int(int_in_str_val, 8))  # 8

neg_int_val = int("-10")
print(neg_int_val)  # -10
abs_int_val = abs(neg_int_val)
print(abs_int_val)  # 10


# int("1a2")  # rice ValueError exception
print(int("1a2", 20))  # 602

print(0b10)  # 2
print(0o10)  # 8
print(0x10)  # 16

float_in_str_val = "15.01"
# int(float_in_str_val)  # rice ValueError exception
float_in_str_val = float(float_in_str_val)
print(float_in_str_val, type(float_in_str_val))
float_in_str_val = int(float_in_str_val)
print(float_in_str_val, type(float_in_str_val))

int_val = 10
print(bin(int_val))  # 0b1010  base 2
print(oct(int_val))  # 0o12  base 8
print(hex(int_val))  # 0xa  base 16
