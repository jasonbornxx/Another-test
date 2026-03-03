import os
import json
from streetlevel import yandex

locations = [
    {"name": "Almaty", "lat": 43.249064, "lon": 76.941999},
    {"name": "Moscow City", "lat": 55.748366, "lon": 37.538354}
]

# We save the data directly into the Android app's asset folder
assets_dir = "app/src/main/assets"
os.makedirs(f"{assets_dir}/images", exist_ok=True)

website_data = []
for loc in locations:
    pano = yandex.find_panorama(loc["lat"], loc["lon"])
    if pano:
        img_filename = f"images/{pano.id}.jpg"
        yandex.download_panorama(pano, f"{assets_dir}/{img_filename}", zoom=2)
        website_data.append({
            "name": loc["name"],
            "image_url": img_filename,
            "date": pano.date.strftime("%B %Y") if pano.date else "Unknown"
        })

with open(f"{assets_dir}/data.json", "w") as f:
    json.dump(website_data, f)
