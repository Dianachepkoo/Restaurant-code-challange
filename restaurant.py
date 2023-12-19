class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    def reviews(self):
        return self.reviews

    def customers(self):
        return list(set([review.customer() for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews])
        return total_ratings / len(self.reviews)
# Create instances of the Restaurant class
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Print the attributes using vars
print(vars(restaurant1))
print(vars(restaurant2))