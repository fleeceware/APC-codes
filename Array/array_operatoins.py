import array

# Signed char
a = array.array('b', [-5, 0, 100])
print("b:", a)

# Unsigned char
a = array.array('B', [0, 200, 255])
print("B:", a)

# Signed int
a = array.array('i', [-10, 0, 1000])
print("i:", a)

# Unsigned int
a = array.array('I', [0, 500, 10000])
print("I:", a)

# Signed long
a = array.array('l', [-1000, 0, 2000])
print("l:", a)

# Unsigned long
a = array.array('L', [0, 4000, 50000])
print("L:", a)

# Signed long long
a = array.array('q', [-999999, 0, 999999])
print("q:", a)

# Unsigned long long
a = array.array('Q', [0, 123456789, 987654321])
print("Q:", a)

# Float (4 bytes)
a = array.array('f', [1.5, -2.5, 3.5])
print("f:", a)

# Double (8 bytes)
a = array.array('d', [3.14159, 2.71828])
print("d:", a)

