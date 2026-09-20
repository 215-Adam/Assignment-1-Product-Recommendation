from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
    for product in products:
    print(product)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
     recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        recommendations.append((product["name"], matches))

    recommendations.sort(key=lambda item: item[1], reverse=True)
    return recommendations



# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_preferences)

print("Recommended products:")
for name, matches in recommendations:
    print(f"{name}: {matches} matching tags")



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?

# 1. I used loops, sets, and set intersection. Loops go through every product. Sets remove
# duplicates and make comparisons fast. Intersection gives the shared tags, so len() of it
# is the match count without a nested loop.

# 2. With 1000+ products, this would slow down since it scores every product each time. I
# would build a dictionary mapping each tag to its products, so I only score products that
# share a tag with the customer.
