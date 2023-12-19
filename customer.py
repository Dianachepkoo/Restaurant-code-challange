
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def num_reviews(self):
        return len(self.reviews)


    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]

# Create instances of the Customer class
mary = Customer("Mary", "John")
john = Customer("John", "Doe")
stacy = Customer("Stacy", "Ashley")
diana = Customer("Diana", "William")

customer1= mary
customer2=john
customer3=stacy
# Print the attributes using vars
print(vars(mary))
print(vars(john))
print(vars(stacy))
print(vars(diana))

for customer in Customer.all():
    print(vars(customer))