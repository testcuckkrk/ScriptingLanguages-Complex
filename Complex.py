#!/usr/bin/python

from math import sqrt
import cmath

# Define the complex numbers class
class Complex:
	"""Class for complex numbers computations"""
	def __init__(self, real=0, imag=0):
		self.r = real
		self.i = imag

	def real(self):
		return self.r
	def imag(self):
		return self.i

	def conjugate(self):
		self.i = -self.i

	def __abs__(self):
		return sqrt(self.r*self.r + self.i*self.i)
	def __str__(self):
		return '(' + str(self.r) + ', ' + str(self.i) + 'i)'
	def __radd__(self, other):
		if isinstance(other, (int, float)):	
			real_temp = self.r + other
			imag_temp = self.i
			return Complex(real_temp, imag_temp)
		elif isinstance(other, Complex):	
			real_temp = self.r + other.r
			imag_temp = self.i + other.i
			return Complex(real_temp, imag_temp)
		else:
			raise TypeError("Don't know how to sum those types")
	def __add__(self, other):
		if isinstance(other, (int, float)):	
			return self.r + other
		elif isinstance(other, Complex):	
			real_temp = self.r + other.r
			imag_temp = self.i + other.i
			return Complex(real_temp, imag_temp)
		else:
			raise TypeError("Don't know how to sum those types")
	def __eq__(self, other):
		if isinstance(other, Complex):		
			return self.r == other.r and self.i == other.i
		else:
			raise TypeError("Don't know how to compare complex to other type")
	def __sub__(self, other):
		if isinstance(other, (int, float)):	
			return self.r - other
		elif isinstance(other, Complex):	
			real_temp = self.r - other.r
			imag_temp = self.i - other.i
			return Complex(real_temp, imag_temp)
		else:
			raise TypeError("Don't know how to subtract those types")
	def __mul__(self, other):
		# (a + bi)(c + di) = (ac - bd) + (bd + ad)i
		if isinstance(other, (int, float)):	
			real_temp = self.r*other
			imag_temp = self.i*other
			return Complex(real_temp, imag_temp)
		elif isinstance(other, Complex):
			real_temp = self.r*other.r - self.i*other.i
			imag_temp = self.i*other.r + self.r*other.i
			return Complex(real_temp, imag_temp)
		else:
			raise TypeError("Don't know how to multiply those types")
	def __div__(self, other):
		# (a + bi)/(c + di) = (ac + bd)/(c^2 + d^2) + (bc - ad)/(c^2 + d^2)i
		if isinstance(other, (int, float)):
			if other != 0:	
				real_temp = self.r/float(other)
				imag_temp = self.i/float(other)
				return Complex(real_temp, imag_temp)
			else:
				raise ZeroDivisionError("Cannot divide by zero!")
		elif isinstance(other, Complex):
			if other.r != 0 or other.i != 0:
				real_temp = (self.r*other.r + self.i*other.i)/(other.r**2 + other.i**2)
				imag_temp = (self.i*other.r - self.r*other.i)/(other.r**2 + other.i**2)
				return Complex(real_temp, imag_temp)
			else:
				raise ZeroDivisionError("Cannot divide by zero!")
		else:
			raise TypeError("Don't know how to multiply those types")
		
# Define two complex numbers
a = Complex(1, -1)	# my implementation
b = Complex(1, -1)	# my implementation
c = Complex(4, -4)	# my implementation
d = Complex(2, -2)	# my implementation
a_builtin = 1-1j	# builtin implementation
b_builtin = 1-1j	# builtin implementation
c_builtin = 4-4j	# builtin implementation
d_builtin = 2-2j	# builtin implementation

# Print a and b
print("Complex numbers to consider:")
print("a:" + str(a) + "\tb:" + str(b))
print("c:" + str(c) + "\td:" + str(d))
print("")

# Try to use the sum method
print("Testing sum() operator")
r_part_sum = sum([a, b, a])
print("sum([a, b, a]): " + str(r_part_sum))
print("builtin: " + str(sum([a_builtin, b_builtin, a_builtin])))
print("")

# Add to complex numbers together
print("Testing '+' operator")
print("a + b: " + str(a+b))
print("builtin: " + str(a_builtin + b_builtin))
print("")

# Subtract those numbers
print("Testing '-' operator")
print("a - b: " + str(a-b))
print("builtin: " + str(a_builtin - b_builtin))
print("")

# Compare those 2
print("Testing '==' operator")
print("a == b: " + str(a == b))
print("builtin: " + str(a_builtin == b_builtin))
print("")

# Calculate the absolute value
print("Testing abs() oberator")
print("abs(a): " + str(abs(a)))
print("builtin: " + str(abs(a_builtin)))
print("")

# Multply those 2
print("Testing '*' operator")
print("a*b: " + str(a*b))
print("builtin: " + str(a_builtin * b_builtin))
print("")

# Divide them by 2.0
print("Testing '/' operator")
print("a/2: " + str(a/2))
print("builtin: " + str(a_builtin / 2))
print("c/d: " + str(c/d))
print("builtin: " + str(c_builtin / d_builtin))
print("")
