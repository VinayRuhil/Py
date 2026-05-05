
# =========================
# ALL SETS PYTHON PRACTICAL
# =========================

# ---------- SET 1 ----------
# Q1: Tuple program
def set1_q1():
    products = ()
    n = int(input("Enter number of products: "))
    for i in range(n):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        products = products + ((name, price),)
    print("\nProducts:")
    for p in products:
        print("Name:", p[0], "Price:", p[1])
    total = sum(p[1] for p in products)
    print("Total Price:", total)

# Q2: Product class
class Product:
    def __init__(self, pid, name, brand, price, discount):
        self.pid = pid
        self.name = name
        self.brand = brand
        self.price = price
        self.discount = discount

    def Price(self):
        print("Price:", self.price)

    def Discount(self):
        disc_amt = self.price * self.discount / 100
        print("Discount Amount:", disc_amt)
        return disc_amt

    def Pay_amount(self):
        final = self.price - (self.price * self.discount / 100)
        print("Final Amount:", final)


# ---------- SET 2 ----------
def set2_q1():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if a > b:
        if a > c:
            print("Greatest is:", a)
        else:
            print("Greatest is:", c)
    else:
        if b > c:
            print("Greatest is:", b)
        else:
            print("Greatest is:", c)


class Employee:
    def __init__(self, emp_id, name, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary

    def emp_details(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Designation:", self.designation)

    def salary_details(self):
        print("Salary:", self.salary)


class Department(Employee):
    def __init__(self, emp_id, name, designation, salary, dept_id, dept_name):
        super().__init__(emp_id, name, designation, salary)
        self.dept_id = dept_id
        self.dept_name = dept_name

    def salary_increment(self):
        bonus = 0.2 * self.salary
        print("Salary with Bonus:", self.salary + bonus)


# ---------- SET 3 ----------
def set3_q1():
    num = int(input("Enter number: "))
    power = len(str(num))
    temp = num
    sum_val = 0

    while temp > 0:
        digit = temp % 10
        sum_val += digit ** power
        temp //= 10

    if num == sum_val:
        print("Armstrong Number")
    else:
        print("Not Armstrong")


class Flight:
    def __init__(self, fid, name, from_loc, to_loc, distance, fare):
        self.fid = fid
        self.name = name
        self.from_loc = from_loc
        self.to_loc = to_loc
        self.distance = distance
        self.fare = fare

    def flight_info(self):
        print(self.fid, self.name, self.from_loc, self.to_loc)

    def fare_info(self):
        if self.distance >= 2000:
            new_fare = self.fare - (0.30 * self.fare)
        else:
            new_fare = self.fare - (0.15 * self.fare)
        print("Final Fare:", new_fare)


# ---------- SET 4 ----------
def set4_q1():
    s = input("Enter string: ")
    rev = s[::-1]
    print("Reversed:", rev)

    if s == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

    print("Length:", len(s))


class Shape:
    def __init__(self, name, dimension):
        self.name = name
        self.dimension = dimension

    def show_shape(self):
        print(self.name, "-", self.dimension)


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle", "2D")
        self.base = base
        self.height = height

    def area_triangle(self):
        print("Area:", 0.5 * self.base * self.height)

    def peri_triangle(self):
        print("Perimeter:", 3 * self.base)


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square", "2D")
        self.side = side

    def area_sqr(self):
        print("Area:", self.side ** 2)

    def peri_sqr(self):
        print("Perimeter:", 4 * self.side)


# ---------- SET 5 ----------
def set5_q1():
    emp = {
        "E001": "Amit",
        "E002": "Puja",
        "E003": "Kunal",
        "E004": "Sandhya",
        "E005": "Sunil"
    }

    emp["E002"] = "Pooja"
    print("E003 Name:", emp["E003"])
    emp.pop("E004")
    print(emp)


class Customer:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.products = {}

    def Customer_Detail(self):
        print("ID:", self.cid)
        print("Name:", self.name)
        print("Products:", self.products)

    def Pay_Details(self):
        total = sum(self.products.values())
        discount = 0.2 * total if total >= 200 else 0
        print("Total:", total)
        print("Discount:", discount)
        print("Final:", total - discount)


# ---------- SET 6 ----------
import numpy as np

def set6_q1():
    a = np.array([[10,14,32],
                  [12,16,18],
                  [14,13,15]])

    b = np.array([[21,22,23],
                  [24,25,26],
                  [27,28,29]])

    c = np.zeros((3,3))

    for i in range(3):
        for j in range(3):
            c[i][j] = a[i][j] + b[i][j]

    print("Result:\n", c)


class List_Info:
    def __init__(self, n1, n2, n3, n4, n5):
        self.lst = [n1, n2, n3, n4, n5]

    def addition(self):
        print("Sum:", sum(self.lst))

    def product(self):
        prod = 1
        for i in self.lst:
            prod *= i
        print("Product:", prod)

    def maximum(self):
        print("Max:", max(self.lst))

    def minimum(self):
        print("Min:", min(self.lst))


print("Python Practical File Loaded Successfully!")
