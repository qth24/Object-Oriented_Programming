class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def set_real(self, real):
        self.real = real

    def set_imag(self, imag):
        self.imag = imag

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    def input_complex(self):
        self.real = float(input("Enter real part: "))
        self.imag = float(input("Enter imaginary part: "))

    def display(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {abs(self.imag)}i")

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def divide(self, other):
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number!")
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)


if __name__ == "__main__":
    print("=== Complex Number Program ===")
    print("- Enter complex number A:")
    A = ComplexNumber()
    A.input_complex()

    print("- Enter complex number B:")
    B = ComplexNumber()
    B.input_complex()

    print("\n> A =", end=" "); A.display()
    print("> B =", end=" "); B.display()

    print("\n--- Results ---")
    print("> A + B =", end=" "); A.add(B).display()
    print("> A - B =", end=" "); A.subtract(B).display()
    print("> A * B =", end=" "); A.multiply(B).display()
    print("> A / B =", end=" "); A.divide(B).display()
