# mylibrary.py

def get_attractions_data():
    """Returns the main database of attractions with detailed criteria."""
    return [
        {
            "id": 1,
            "name": "Transformers: The Ride 3D",
            "categories": ["rides", "simulator rides", "thrill rides"],
            "is_free": False,
            "price": 15,
            "age_groups": ["Kids", "Teens", "Adults"],
            "description": "An immersive 3D simulator ride through a battle between the Autobots and Decepticons at Universal Studios Singapore. Park admission is required.",
            "image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/92/a8/2b/fb-img-1504750573426.jpg?w=1200&h=-1&s=1"
        },
        {
            "id": 2,
            "name": "Battlestar Galactica: HUMAN vs. CYLON",
            "categories": ["rides", "roller coasters", "thrill rides"],
            "is_free": False,
            "price": 82,
            "age_groups": ["Teens", "Adults"],
            "description": "A high-speed dueling roller coaster with two tracks inspired by the HUMAN and CYLON forces. Park admission is required.",
            "image": "https://www.rwsentosa.com/-/jssmedia/project/non-gaming/rwsentosa/attractions/universal-studios-singapore/rides/uss-lost-world-ride-dino-soarin-_1440x760.jpg?mw=1200"
        },
        {
            "id": 3,
            "name": "Revenge of the Mummy",
            "categories": ["rides", "roller coasters", "dark rides", "thrill rides"],
            "is_free": False,
            "price": 50,
            "age_groups": ["Teens", "Adults"],
            "description": "An indoor roller coaster that takes riders through dark scenes inspired by the Mummy films. Park admission is required.",
            "image": "https://thumbs.dreamstime.com/b/entrance-to-revenge-mummy-indoor-dark-ride-ancient-egypt-universal-studios-singapore-38650264.jpg"
        },
        {
            "id": 4,
            "name": "Jurassic Park Rapids Adventure",
            "categories": ["rides", "water rides", "family rides"],
            "is_free": False,
            "price": 48,
            "age_groups": ["Kids", "Teens", "Adults"],
            "description": "A river raft ride through a dinosaur habitat with rapids and a splashdown. Park admission is required.",
            "image": "https://i.ytimg.com/vi/wjyruWe0zMc/maxresdefault.jpg"
        },
        {
            "id": 5,
            "name": "Sesame Street Spaghetti Space Chase",
            "categories": ["rides", "dark rides", "family rides"],
            "is_free": False,
            "price": 73,
            "age_groups": ["Kids", "Teens", "Adults"],
            "description": "A family-friendly indoor ride following Elmo and friends on a space adventure. Park admission is required.",
            "image": "https://farm9.staticflickr.com/8231/8477331289_a0bbd4e9bb_b.jpg"
        },
        {
            "id": 6,
            "name": "Canopy Flyer",
            "categories": ["rides", "aerial rides", "family rides"],
            "is_free": False,
            "price": 39,
            "age_groups": ["Kids", "Teens", "Adults"],
            "description": "A suspended ride offering an aerial view of the Lost World area. Park admission is required.",
            "image": "https://www.rwsentosa.com/-/jssmedia/project/non-gaming/rwsentosa/attractions/universal-studios-singapore/rides/uss-lost-world-ride-dino-soarin-_1440x760.jpg?mw=1200"
        },
        {
            "id": 7,
            "name": "Puss In Boots' Giant Journey",
            "categories": ["rides", "roller coasters", "family rides"],
            "is_free": True,
            "price": 0,
            "age_groups": ["Kids", "Teens", "Adults"],
            "description": "A family roller coaster that follows Puss in Boots and Kitty Softpaws on a fairytale adventure. Park admission is required.",
            "image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/40/Puss_in_Boots%27_Giant_Journey_1.jpg/960px-Puss_in_Boots%27_Giant_Journey_1.jpg",
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