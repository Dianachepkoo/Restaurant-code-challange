from customer import Customer
from restaurant import Restaurant 

class Customer:
    def __init__(self, name):
        self.name = name

class Restaurant:
    def __init__(self, name):
        self.name = name

class Review:
    def __init__(self, customer, restaurant, rating=0):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

# Create instances
customer = Customer("Alice")
restaurant = Restaurant("Wonderful Eatery")

# Create an instance of the Review class
review = Review(customer, restaurant, rating=5)

# Print the attributes using vars
print(vars(review))