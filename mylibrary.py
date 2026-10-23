# mylibrary.py

def get_attractions_data():
    """Returns the main database of attractions with detailed criteria."""
    return [
        {
            "id": 1,
            "name": "Gardens by the Bay 123",
            "categories": ["nature", "great views", "shows"],
            "is_free": False,
            "price": 28,
            "age_groups": ["Kids", "Teens", "Adults", "Seniors"],
            "description": "Futuristic park featuring giant Supertree structures and dramatic climate-controlled conservatories.",
            "image": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=600&q=80"
        },
        {
            "id": 2,
            "name": "Marina Bay Sands SkyPark",
            "categories": ["great views"],
            "is_free": False,
            "price": 32,
            "age_groups": ["Teens", "Adults", "Seniors"],
            "description": "Observation deck offering stunning panoramic views of the city skyline and harbor.",
            "image": "https://images.unsplash.com/photo-1565967511849-76a60a516170?auto=format&fit=crop&w=600&q=80"
        },
        {
            "id": 3,
            "name": "Spectra - Light & Water Show",
            "categories": ["shows", "great views"],
            "is_free": True,
            "price": 0,
            "age_groups": ["Kids", "Teens", "Adults", "Seniors"],
            "description": "A free, outdoor light and water show displayed over the water at Event Plaza.",
            "image": "https://images.unsplash.com/photo-1508873696983-2df505f9e85f?auto=format&fit=crop&w=600&q=80"
        },
        {
            "id": 4,
            "name": "Botanic Gardens",
            "categories": ["nature"],
            "is_free": True,
            "price": 0,
            "age_groups": ["Kids", "Teens", "Adults", "Seniors"],
            "description": "UNESCO World Heritage site with lush green tropical flora, lakes, and walking trails.",
            "image": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=600&q=80"
        },
        {
            "id": 5,
            "name": "Universal Studios",
            "categories": ["shows", "theme park"],
            "is_free": False,
            "price": 82,
            "age_groups": ["Kids", "Teens", "Adults"],
            "description": "Thrilling rides, live shows, and movie-themed attractions for the entire family.",
            "image": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=600&q=80"
        },
        {
            "id": 6,
            "name": "Night Safari",
            "categories": ["nature", "shows"],
            "is_free": False,
            "price": 55,
            "age_groups": ["Kids", "Teens", "Adults", "Seniors"],
            "description": "The world's first nocturnal zoo featuring wildlife habitats and night creature shows.",
            "image": "https://images.unsplash.com/photo-1534567153574-2b12153a87f0?auto=format&fit=crop&w=600&q=80"
        }
    ]


def get_recommendations(attractions, selected_categories, max_price=None, free_only=False, target_age=None):
    """
    Filters attractions based on categories, budget, free option, and age suitability.
    Returns a list of recommended attraction dictionaries.
    """
    recommended = []

    for item in attractions:
        # Check category match (if categories selected, match ANY selected category)
        category_match = True
        if selected_categories:
            category_match = any(cat in item["categories"] for cat in selected_categories)

        # Check free filter
        free_match = True
        if free_only:
            free_match = item["is_free"]

        # Check max price filter
        price_match = True
        if max_price is not None and not free_only:
            price_match = item["price"] <= max_price

        # Check age suitability
        age_match = True
        if target_age and target_age != "All Ages":
            age_match = target_age in item["age_groups"]

        # Combine all filter criteria
        if category_match and free_match and price_match and age_match:
            recommended.append(item)

    return recommended