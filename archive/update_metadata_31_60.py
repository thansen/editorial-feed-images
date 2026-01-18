#!/usr/bin/env python3
"""
Update metadata for images 31-60 with accurate descriptions
"""

import json

# Load metadata
with open('images_metadata.json', 'r') as f:
    metadata = json.load(f)

# Accurate metadata for each image based on actual content
updates = {
    30: {  # Entry 31: olympic-rings-red-gradient-1.jpg
        "title": "Blue Suitcase",
        "description": "A blue hard-shell suitcase with handle on a blue to cyan gradient background. The luggage casts a shadow creating depth.",
        "conceptual": ["travel", "journey", "vacation", "business-trip", "luggage", "mobility"],
        "subject": ["suitcase", "briefcase", "luggage", "handle", "hard-shell"],
        "style": ["3d-render", "clean", "minimal", "modern", "gradient"]
    },
    31: {  # Entry 32: golden-metallic-gears-yellow-gradient.jpg
        "title": "Blue Bust Silhouette",
        "description": "A blue classical bust silhouette on a light blue to cyan gradient background. The sculpture-style profile creates an elegant, minimalist composition.",
        "conceptual": ["art", "classical", "elegance", "culture", "history", "profile"],
        "subject": ["bust", "sculpture", "silhouette", "head", "profile", "statue"],
        "style": ["silhouette", "minimal", "gradient", "classical", "elegant", "modern"]
    },
    32: {  # Entry 33: green-gears-gradient-2.jpg
        "title": "White Wireless Earbuds",
        "description": "Two white wireless earbuds on an orange to pink gradient background. The in-ear headphones are positioned separately with visible speakers.",
        "conceptual": ["audio", "music", "technology", "wireless", "listening", "modern-tech"],
        "subject": ["earbuds", "headphones", "wireless", "audio-device", "speakers"],
        "style": ["product-photography", "clean", "gradient", "modern", "minimal"]
    },
    33: {  # Entry 34: teal-gears-gradient.jpg
        "title": "Earth Pixelating Effect",
        "description": "Earth disintegrating into pixel fragments on a blue to green gradient background. The digital fragmentation effect creates a dramatic technological visualization.",
        "conceptual": ["technology", "digital", "transformation", "data", "fragmentation", "climate"],
        "subject": ["earth", "globe", "pixels", "fragments", "planet", "continents"],
        "style": ["digital-art", "3d-render", "gradient", "surreal", "fragmented", "modern"]
    },
    34: {  # Entry 35: purple-gears-gradient.jpg
        "title": "Palm Trees Silhouette",
        "description": "Silhouetted palm trees on a cyan turquoise gradient background. The tropical tree fronds create a layered, peaceful composition.",
        "conceptual": ["tropical", "vacation", "relaxation", "paradise", "summer", "beach"],
        "subject": ["palm-trees", "trees", "silhouette", "fronds", "tropical-plants"],
        "style": ["silhouette", "minimal", "gradient", "tropical", "serene", "photographic"]
    },
    35: {  # Entry 36: yellow-gears-gradient.jpg
        "title": "Military Helmet",
        "description": "An olive green military helmet with brown leather strap on a yellow to green gradient background. The vintage-style combat helmet casts a distinct shadow.",
        "conceptual": ["military", "protection", "war", "history", "defense", "veteran"],
        "subject": ["helmet", "military-gear", "strap", "combat-helmet", "headgear"],
        "style": ["photographic", "realistic", "gradient", "vintage", "textured"]
    },
    36: {  # Entry 37: orange-gears-gradient.jpg
        "title": "Elephant and Donkey",
        "description": "A red elephant and blue donkey shaking hands on a red to blue gradient background. The 3D rendered political mascots are smiling in a friendly pose.",
        "conceptual": ["politics", "bipartisan", "unity", "democracy", "cooperation", "agreement"],
        "subject": ["elephant", "donkey", "animals", "mascots", "handshake"],
        "style": ["3d-render", "cartoon", "playful", "gradient", "friendly", "colorful"]
    },
    37: {  # Entry 38: pink-gears-gradient.jpg
        "title": "Milk Carton",
        "description": "A white and blue milk carton labeled 'Polled Millired' on a blue to white gradient background. The gable-top carton has a screw cap.",
        "conceptual": ["dairy", "nutrition", "food", "beverage", "grocery", "health"],
        "subject": ["milk-carton", "carton", "packaging", "container", "beverage-container"],
        "style": ["product-photography", "clean", "gradient", "realistic", "minimal"]
    },
    38: {  # Entry 39: coral-gears-gradient.jpg
        "title": "Businessman Banana Peel",
        "description": "A 3D rendered cartoon businessman about to slip on a banana peel on a red gradient background. The character wears a blue suit and red tie.",
        "conceptual": ["risk", "hazard", "mistake", "caution", "failure", "accident"],
        "subject": ["businessman", "banana-peel", "character", "suit", "slip"],
        "style": ["3d-render", "cartoon", "playful", "humorous", "colorful", "illustrative"]
    },
    39: {  # Entry 40: magenta-gears-gradient.jpg
        "title": "Water Droplets Glass",
        "description": "Water condensation droplets on a glass surface with blue tones. The droplets create various sizes with streams running down the surface.",
        "conceptual": ["freshness", "purity", "moisture", "condensation", "water", "clarity"],
        "subject": ["water-droplets", "condensation", "glass", "surface", "liquid"],
        "style": ["macro", "photographic", "textured", "realistic", "detailed", "blue-tones"]
    },
    40: {  # Entry 41: lime-gears-gradient.jpg
        "title": "Colorful Party Popper",
        "description": "A rainbow zigzag-patterned party popper exploding with colorful spirals and confetti on a pink to white gradient background. The celebration cone bursts with red, yellow, blue, and purple shapes.",
        "conceptual": ["celebration", "party", "joy", "festive", "fun", "excitement"],
        "subject": ["party-popper", "confetti", "spirals", "cone", "decorations"],
        "style": ["3d-render", "colorful", "playful", "gradient", "vibrant", "festive"]
    },
    41: {  # Entry 42: peach-gears-gradient.jpg
        "title": "Money Bag",
        "description": "A cream-colored money bag with dollar sign and orange tie on an orange to yellow gradient background. The 3D rendered sack has a cinched top.",
        "conceptual": ["wealth", "money", "savings", "finance", "prosperity", "reward"],
        "subject": ["money-bag", "sack", "dollar-sign", "bag", "currency"],
        "style": ["3d-render", "cartoon", "clean", "gradient", "simple", "illustrative"]
    },
    42: {  # Entry 43: forest-green-gears-gradient.jpg
        "title": "Growth Bar Chart",
        "description": "3D green and red bar chart with upward trending arrow on a green to yellow gradient background. The ascending bars show increasing growth with red indicators.",
        "conceptual": ["growth", "progress", "success", "finance", "analytics", "increase"],
        "subject": ["bar-chart", "graph", "arrow", "bars", "data-visualization"],
        "style": ["3d-render", "clean", "gradient", "infographic", "business", "modern"]
    },
    43: {  # Entry 44: lavender-gears-gradient.jpg
        "title": "Green Tech Pattern",
        "description": "Abstract green technological pattern with geometric shapes, circles, and lines on a solid green gradient. The digital interface elements create a futuristic tech composition.",
        "conceptual": ["technology", "digital", "innovation", "future", "data", "connectivity"],
        "subject": ["geometric-shapes", "circles", "lines", "patterns", "tech-elements"],
        "style": ["digital", "abstract", "geometric", "futuristic", "tech", "monochrome"]
    },
    44: {  # Entry 45: violet-gears-gradient.jpg
        "title": "Purple Tech Pattern",
        "description": "Abstract purple technological pattern with circular interfaces and diagonal lines on a solid purple gradient. The digital HUD-style elements create a cyberpunk aesthetic.",
        "conceptual": ["technology", "digital", "futuristic", "interface", "data", "cyber"],
        "subject": ["circles", "geometric-shapes", "lines", "patterns", "interface-elements"],
        "style": ["digital", "abstract", "futuristic", "tech", "cyberpunk", "monochrome"]
    },
    45: {  # Entry 46: sky-blue-gears-gradient.jpg
        "title": "Blue Layered Waves",
        "description": "Abstract layered blue waves creating depth on a blue gradient background. The flowing curved layers transition from dark to light blue.",
        "conceptual": ["flow", "layers", "depth", "waves", "movement", "fluidity"],
        "subject": ["waves", "curves", "layers", "abstract-shapes", "flowing-forms"],
        "style": ["abstract", "gradient", "layered", "smooth", "modern", "minimal"]
    },
    46: {  # Entry 47: rose-gears-gradient.jpg
        "title": "Green Curved Waves",
        "description": "Abstract layered green and yellow curved waves on a green to yellow gradient background. The smooth flowing layers create a sense of movement.",
        "conceptual": ["growth", "nature", "energy", "flow", "organic", "vitality"],
        "subject": ["waves", "curves", "layers", "abstract-shapes", "flowing-forms"],
        "style": ["abstract", "gradient", "smooth", "layered", "organic", "modern"]
    },
    47: {  # Entry 48: salmon-gears-gradient.jpg
        "title": "Red Layered Curves",
        "description": "Abstract red curved layers creating depth and dimension on a solid red background. The overlapping waves form an elegant abstract composition.",
        "conceptual": ["passion", "energy", "depth", "layers", "intensity", "boldness"],
        "subject": ["curves", "layers", "waves", "abstract-shapes", "geometric-forms"],
        "style": ["abstract", "minimal", "layered", "monochrome", "elegant", "modern"]
    },
    48: {  # Entry 49: aqua-gears-gradient.jpg
        "title": "Earth Night Lights",
        "description": "Earth at night showing city lights across North America on a deep blue to purple gradient. The illuminated urban areas create a glowing network pattern.",
        "conceptual": ["connectivity", "urbanization", "night", "civilization", "global", "infrastructure"],
        "subject": ["earth", "planet", "city-lights", "continents", "globe", "nighttime"],
        "style": ["photographic", "space-view", "gradient", "realistic", "dramatic", "illuminated"]
    },
    49: {  # Entry 50: cerulean-gears-gradient.jpg
        "title": "Earth Americas View",
        "description": "Earth showing the Americas on a blue to green gradient background. The planet displays North and South America with visible cloud patterns and oceans.",
        "conceptual": ["environment", "global", "earth", "nature", "planet", "geography"],
        "subject": ["earth", "planet", "continents", "americas", "clouds", "ocean"],
        "style": ["photographic", "realistic", "gradient", "space-view", "natural", "vibrant"]
    },
    50: {  # Entry 51: chartreuse-gears-gradient.jpg
        "title": "Yellow Chicken",
        "description": "A 3D rendered yellow chicken with red comb and wattle on an orange to yellow gradient background. The stylized rooster has a friendly expression.",
        "conceptual": ["farm", "poultry", "rural", "agriculture", "morning", "nature"],
        "subject": ["chicken", "rooster", "bird", "poultry", "farm-animal"],
        "style": ["3d-render", "cartoon", "clean", "gradient", "playful", "colorful"]
    },
    51: {  # Entry 52: indigo-gears-gradient.jpg
        "title": "Crying Emoji",
        "description": "A 3D rendered yellow crying emoji with blue tears streaming down on a blue to purple gradient background. The face shows intense sadness.",
        "conceptual": ["emotion", "sadness", "crying", "feelings", "expression", "grief"],
        "subject": ["emoji", "face", "tears", "emoticon", "expression"],
        "style": ["3d-render", "emoji", "gradient", "clean", "expressive", "modern"]
    },
    52: {  # Entry 53: gold-gears-gradient-1.jpg
        "title": "Grinning Emoji",
        "description": "A 3D rendered yellow grinning emoji with big smile and closed eyes on an orange gradient background. The happy face shows pure joy.",
        "conceptual": ["happiness", "joy", "positivity", "laughter", "emotion", "delight"],
        "subject": ["emoji", "face", "smile", "emoticon", "expression"],
        "style": ["3d-render", "emoji", "gradient", "clean", "cheerful", "simple"]
    },
    53: {  # Entry 54: amber-gears-gradient.jpg
        "title": "Milk Carton",
        "description": "A white and blue milk carton labeled 'Polled Millired' on a blue to white gradient background. The gable-top carton has a white screw cap.",
        "conceptual": ["dairy", "nutrition", "food", "beverage", "grocery", "health"],
        "subject": ["milk-carton", "carton", "packaging", "container", "beverage-container"],
        "style": ["product-photography", "clean", "gradient", "realistic", "minimal"]
    },
    54: {  # Entry 55: medical-syringe-teal-gradient.jpg
        "title": "Medical Syringe",
        "description": "A teal medical syringe with measurement markings on a solid teal gradient background. The injection device shows the plunger and needle clearly.",
        "conceptual": ["medicine", "healthcare", "vaccination", "injection", "medical", "treatment"],
        "subject": ["syringe", "needle", "medical-device", "injection", "plunger"],
        "style": ["product-photography", "clean", "monochrome", "medical", "minimal", "professional"]
    },
    55: {  # Entry 56: turquoise-gears-gradient.jpg
        "title": "Syringe with Markings",
        "description": "A turquoise medical syringe with black measurement markings on a turquoise gradient background. The detailed injection device shows calibration lines and plunger.",
        "conceptual": ["medicine", "healthcare", "vaccination", "dosage", "medical", "precision"],
        "subject": ["syringe", "needle", "medical-device", "measurements", "injection"],
        "style": ["product-photography", "clean", "monochrome", "detailed", "medical", "professional"]
    },
    56: {  # Entry 57: navy-gears-gradient.jpg
        "title": "Purple Briefcase",
        "description": "A lavender purple hard-shell briefcase on a pink to purple gradient background. The sleek luggage has a handle and casts a soft shadow.",
        "conceptual": ["business", "travel", "professional", "work", "journey", "corporate"],
        "subject": ["briefcase", "suitcase", "luggage", "handle", "hard-shell"],
        "style": ["3d-render", "clean", "minimal", "gradient", "modern", "professional"]
    },
    57: {  # Entry 58: plum-gears-gradient.jpg
        "title": "Orange Spiral Tunnel",
        "description": "A hypnotic orange and red spiral tunnel pattern on a gradient background. The concentric circular rings create an optical illusion of depth and movement.",
        "conceptual": ["depth", "infinity", "hypnotic", "movement", "focus", "vortex"],
        "subject": ["spiral", "tunnel", "circles", "rings", "pattern"],
        "style": ["abstract", "optical-illusion", "gradient", "geometric", "hypnotic", "radial"]
    },
    58: {  # Entry 59: steel-blue-gears-gradient.jpg
        "title": "Green Medical Cross",
        "description": "A 3D rendered green medical cross symbol on a solid green gradient background. The plus sign represents healthcare and first aid.",
        "conceptual": ["healthcare", "medical", "first-aid", "health", "care", "wellness"],
        "subject": ["cross", "plus-sign", "medical-symbol", "icon", "symbol"],
        "style": ["3d-render", "minimal", "clean", "monochrome", "symbolic", "medical"]
    },
    59: {  # Entry 60: olive-gears-gradient.jpg
        "title": "Cute Puppy Peeking",
        "description": "A 3D rendered orange cartoon puppy peeking over an edge on an orange gradient background. The adorable dog has big expressive eyes and a sweet smile.",
        "conceptual": ["cuteness", "pets", "innocence", "playfulness", "joy", "companion"],
        "subject": ["puppy", "dog", "animal", "pet", "character"],
        "style": ["3d-render", "cartoon", "cute", "gradient", "playful", "adorable"]
    }
}

# Update the metadata
for index, update_data in updates.items():
    if index < len(metadata):
        metadata[index]['title'] = update_data['title']
        metadata[index]['description'] = update_data['description']
        metadata[index]['tags']['conceptual'] = update_data['conceptual']
        metadata[index]['tags']['subject'] = update_data['subject']
        metadata[index]['tags']['style'] = update_data['style']
        # Keep existing colors and analyzed_colors

# Save updated metadata
with open('images_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print("✓ Updated entries 31-60 with accurate metadata")
print(f"✓ Saved to images_metadata.json")
print(f"\nSummary:")
print(f"  - Updated {len(updates)} entries")
print(f"  - Preserved originalFilename, newFilename, colors, and analyzed_colors")
print(f"  - Generated accurate titles, descriptions, and tags")
