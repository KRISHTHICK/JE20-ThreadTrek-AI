def generate_outfit(destination, activity, weather):
    if activity == "Beach":
        return "Light cotton shirt, floral shorts, sandals, and a sunhat 🏖️"
    elif activity == "Trekking":
        return "Breathable trek pants, moisture-wicking tee, windcheater, and trail shoes 🥾"
    elif activity == "Temple Visit":
        return "Modest linen kurta, full-length trousers, and covered shoes 🕌"
    elif activity == "Business":
        return "Neutral blazer, collared shirt, slacks, and loafers 👔"
    else:
        return "Comfy jeans, graphic tee, sneakers, and sunglasses 😎"
