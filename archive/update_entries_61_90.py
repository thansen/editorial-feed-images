#!/usr/bin/env python3
"""
Update metadata for entries 61-90 with accurate descriptions based on actual image content
"""

import json

# Load metadata
with open('/Users/tyler/Documents/github/editorial_feed_images/images_metadata.json', 'r') as f:
    data = json.load(f)

# Accurate descriptions based on actual images viewed
updates = {
    # Entry 61 - teal-suitcase-monochrome-gradient.jpg
    60: {
        "title": "Teal Suitcase",
        "description": "3D rendered teal hard-shell suitcase with handle and latches on a teal gradient background. The luggage represents travel and journey.",
        "conceptual": ["travel", "journey", "vacation", "mobility"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "minimal", "monochromatic"]
    },
    # Entry 62 - powder-blue-gears-gradient.jpg (ACTUALLY RED SUITCASE)
    61: {
        "title": "Red Suitcase",
        "description": "3D rendered red hard-shell suitcase with handle on a red gradient background. The vibrant luggage represents bold travel and adventure.",
        "conceptual": ["travel", "adventure", "journey", "bold"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "monochromatic", "vibrant"]
    },
    # Entry 63 - copper-gears-gradient.jpg (ACTUALLY CORAL/ORANGE SUITCASE)
    62: {
        "title": "Coral Orange Suitcase",
        "description": "3D rendered coral orange suitcase on an orange to yellow gradient background. The warm-toned luggage represents sunny destinations.",
        "conceptual": ["travel", "vacation", "warmth", "sunny"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "warm", "gradient"]
    },
    # Entry 64 - mustard-gears-gradient.jpg (ACTUALLY GREEN SUITCASE)
    63: {
        "title": "Green Suitcase",
        "description": "3D rendered green hard-shell suitcase on a green to yellow gradient background. The fresh-colored luggage represents eco-friendly travel.",
        "conceptual": ["travel", "eco-friendly", "fresh", "journey"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "fresh", "gradient"]
    },
    # Entry 65 - champagne-gold-gears-gradient.jpg (ACTUALLY ORANGE SUITCASE)
    64: {
        "title": "Orange Suitcase",
        "description": "3D rendered orange hard-shell suitcase on an orange gradient background. The bright luggage represents energetic travel.",
        "conceptual": ["travel", "energy", "adventure", "vibrant"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "monochromatic", "bold"]
    },
    # Entry 66 - teal-suitcase-variant-gradient.jpg (ACTUALLY TEAL GEARS)
    65: {
        "title": "Teal Gears",
        "description": "3D rendered teal mechanical gears of various sizes on a teal gradient background. The interlocking cogs represent systems and technology.",
        "conceptual": ["technology", "systems", "automation", "engineering"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "clean"]
    },
    # Entry 67 - red-gears-monochrome-gradient.jpg
    66: {
        "title": "Red Gears",
        "description": "3D rendered red and pink mechanical gears of various sizes on a red gradient background. The machinery represents energy and power systems.",
        "conceptual": ["technology", "energy", "power", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "bold"]
    },
    # Entry 68 - green-gears-monochrome-gradient.jpg
    67: {
        "title": "Green Gears",
        "description": "3D rendered green and lime mechanical gears of various sizes on a green gradient background. The machinery represents eco technology and sustainable systems.",
        "conceptual": ["technology", "sustainability", "eco-friendly", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "eco"]
    },
    # Entry 69 - golden-metallic-gears-premium-gradient.jpg
    68: {
        "title": "Golden Metallic Gears",
        "description": "3D rendered golden metallic gears of various sizes on a yellow gradient background. The premium machinery represents value and excellence.",
        "conceptual": ["technology", "excellence", "premium", "value"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render", "metal"],
        "style": ["modern", "technical", "3d-render", "luxurious", "metallic"]
    },
    # Entry 70 - virus-particle-green-gradient.jpg (ACTUALLY ORANGE GEARS)
    69: {
        "title": "Orange Gears",
        "description": "3D rendered orange mechanical gears of various sizes on an orange gradient background. The warm machinery represents energy and dynamic systems.",
        "conceptual": ["technology", "energy", "dynamic", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "warm"]
    },
    # Entry 71 - olympic-rings-red-solid.jpg
    70: {
        "title": "Olympic Rings Red",
        "description": "3D rendered Olympic rings in blue, yellow, black, green and red on a solid red background. The iconic interlocking rings represent international sports.",
        "conceptual": ["sports", "olympics", "unity", "competition", "international"],
        "subject": ["olympic-rings", "rings", "circles", "3d-render", "symbol"],
        "style": ["modern", "iconic", "3d-render", "bold", "solid"]
    },
    # Entry 72 - ice-blue-gears-gradient.jpg (ACTUALLY APPLE DEVICES)
    71: {
        "title": "Apple Devices Display",
        "description": "Multiple Apple devices including tablets and smartphones arranged on a blue gradient background showing app interfaces. The tech display represents mobile computing.",
        "conceptual": ["technology", "mobile", "digital", "computing", "apps"],
        "subject": ["tablets", "smartphones", "devices", "apple", "screens"],
        "style": ["modern", "tech", "photographic", "product", "blue"]
    },
    # Entry 73 - sunset-gold-gears-gradient.jpg (ACTUALLY AWARD STATUE)
    72: {
        "title": "Golden Award Statue",
        "description": "3D rendered golden award statue resembling an Oscar trophy on an orange gradient background. The prestigious award represents achievement and excellence.",
        "conceptual": ["achievement", "excellence", "award", "recognition", "success"],
        "subject": ["trophy", "award", "statue", "3d-render", "figure"],
        "style": ["modern", "elegant", "3d-render", "prestigious", "golden"]
    },
    # Entry 74 - lilac-gears-gradient.jpg (ACTUALLY STUFFED ANIMALS)
    73: {
        "title": "Political Party Mascots",
        "description": "Red plush elephant and blue plush donkey stuffed animals on a purple gradient background. The toys represent American political parties.",
        "conceptual": ["politics", "democracy", "parties", "america", "representation"],
        "subject": ["elephant", "donkey", "stuffed-animals", "toys", "mascots"],
        "style": ["playful", "symbolic", "photographic", "plush", "political"]
    },
    # Entry 75 - electric-blue-gears-gradient.jpg (ACTUALLY DNA HELIX)
    74: {
        "title": "DNA Double Helix",
        "description": "3D rendered DNA double helix structure in purple and pink on a purple gradient background. The molecular structure represents genetics and biology.",
        "conceptual": ["science", "genetics", "biology", "research", "dna"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "technical", "biological"]
    },
    # Entry 76 - neon-green-gears-gradient.jpg (ACTUALLY CIRCUIT BOARD CHIP)
    75: {
        "title": "Circuit Board Chip",
        "description": "Glowing green circuit board chip icon with pathways radiating from center on a green gradient background. The tech symbol represents computing and processors.",
        "conceptual": ["technology", "computing", "digital", "processing", "electronics"],
        "subject": ["chip", "circuit-board", "processor", "icon", "technology"],
        "style": ["modern", "glowing", "icon", "technical", "neon"]
    },
    # Entry 77 - mint-green-gears-gradient-1.jpg (ACTUALLY GAME CONTROLLER)
    76: {
        "title": "PlayStation Controller",
        "description": "Black PlayStation game controller on a pink gradient background. The gaming device represents video games and entertainment.",
        "conceptual": ["gaming", "entertainment", "play", "video-games", "leisure"],
        "subject": ["controller", "gamepad", "playstation", "device", "gaming"],
        "style": ["modern", "photographic", "product", "clean", "gaming"]
    },
    # Entry 78 - sage-green-gears-gradient.jpg (ACTUALLY DEMON CHARACTER)
    77: {
        "title": "Fantasy Demon Character",
        "description": "Digital art of a red demon or dark fantasy character with horned crown on a red gradient background. The creature represents dark fantasy and mythology.",
        "conceptual": ["fantasy", "mythology", "dark", "supernatural", "fiction"],
        "subject": ["demon", "character", "creature", "fantasy", "portrait"],
        "style": ["digital-art", "dark", "fantasy", "atmospheric", "illustration"]
    },
    # Entry 79 - baby-blue-gears-gradient.jpg (ACTUALLY SOCCER BALL WITH WORLD MAP)
    78: {
        "title": "World Map Soccer",
        "description": "Soccer ball with world map continents printed on it on a green background. The globe ball represents international football and world sports.",
        "conceptual": ["sports", "global", "soccer", "international", "unity"],
        "subject": ["soccer-ball", "globe", "world-map", "ball", "sports"],
        "style": ["photographic", "symbolic", "sports", "global", "creative"]
    },
    # Entry 80 - peacock-blue-gears-gradient.jpg (ACTUALLY BROKEN TV)
    79: {
        "title": "Broken TV Monitor",
        "description": "Broken CRT television with cracked screen and exposed circuit boards on a green gradient background. The damaged tech represents obsolescence and decay.",
        "conceptual": ["obsolescence", "technology", "broken", "decay", "e-waste"],
        "subject": ["television", "monitor", "screen", "circuit-board", "broken"],
        "style": ["photographic", "grungy", "damaged", "retro", "tech"]
    },
    # Entry 81 - coral-pink-gears-gradient.jpg (ACTUALLY DNA HELIX)
    80: {
        "title": "DNA Helix Purple",
        "description": "3D rendered DNA double helix structure in purple tones on a purple gradient background. The genetic structure represents life science and heredity.",
        "conceptual": ["science", "genetics", "biology", "heredity", "research"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "gradient", "biological"]
    },
    # Entry 82 - kelly-green-gears-gradient.jpg (ACTUALLY SOCCER BALL)
    81: {
        "title": "Soccer Ball",
        "description": "Classic black and white soccer ball on green turf or grass background. The football represents the world's most popular sport.",
        "conceptual": ["sports", "soccer", "football", "athletics", "competition"],
        "subject": ["soccer-ball", "ball", "football", "sports-equipment", "turf"],
        "style": ["photographic", "sports", "classic", "clean", "realistic"]
    },
    # Entry 83 - orchid-purple-gears-gradient.jpg (ACTUALLY SHOPPING CART)
    82: {
        "title": "Shopping Cart",
        "description": "3D rendered shopping cart with blue frame and orange handles on a blue gradient background. The cart represents e-commerce and retail.",
        "conceptual": ["shopping", "e-commerce", "retail", "consumerism", "purchase"],
        "subject": ["shopping-cart", "cart", "basket", "3d-render", "retail"],
        "style": ["modern", "clean", "3d-render", "minimal", "commercial"]
    },
    # Entry 84 - cherry-red-gears-gradient.jpg (ACTUALLY POLICE TAPE)
    83: {
        "title": "Police Caution Tape",
        "description": "Yellow and black striped police caution tape reading 'CAUTION POLICE' on an orange to red gradient background. The barrier tape represents law enforcement and crime scenes.",
        "conceptual": ["law-enforcement", "crime", "caution", "warning", "security", "investigation"],
        "subject": ["police-tape", "caution-tape", "barrier", "warning", "text"],
        "style": ["photographic", "realistic", "warning", "bold", "official"]
    },
    # Entry 85 - lemon-yellow-gears-gradient.jpg (ACTUALLY ROCK HAND GESTURE)
    84: {
        "title": "Rock Hand Sign",
        "description": "3D rendered metallic bronze hand making rock and roll horn gesture on a dark purple to red gradient background. The hand symbol represents music and rock culture.",
        "conceptual": ["music", "rock", "culture", "rebellion", "expression", "gesture"],
        "subject": ["hand", "gesture", "sign", "3d-render", "fingers"],
        "style": ["modern", "3d-render", "metallic", "bold", "cultural"]
    },
    # Entry 86 - ocean-blue-gears-gradient.jpg (ACTUALLY DNA HELIX)
    85: {
        "title": "DNA Helix Purple",
        "description": "3D rendered DNA double helix structure in purple on a purple gradient background. The genetic structure represents biology and science.",
        "conceptual": ["science", "genetics", "biology", "research", "dna", "heredity"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "technical", "monochromatic"]
    },
    # Entry 87 - fuchsia-gears-gradient.jpg (ACTUALLY HEART IN HANDS EMOJI)
    86: {
        "title": "Heart in Hands",
        "description": "3D rendered emoji of two hands holding a red heart on a pink gradient background. The caring gesture represents love and compassion.",
        "conceptual": ["love", "care", "compassion", "charity", "kindness", "support"],
        "subject": ["heart", "hands", "emoji", "3d-render", "gesture"],
        "style": ["modern", "3d-render", "emoji", "clean", "symbolic"]
    },
    # Entry 88 - vermillion-gears-gradient.jpg (ACTUALLY OLYMPIC RINGS)
    87: {
        "title": "Olympic Rings Coral",
        "description": "3D rendered Olympic rings in blue, yellow, black, green and red on a coral orange gradient background. The interlocking rings represent international sports.",
        "conceptual": ["sports", "olympics", "unity", "competition", "international", "athletics"],
        "subject": ["olympic-rings", "rings", "circles", "3d-render", "symbol"],
        "style": ["modern", "iconic", "3d-render", "clean", "symbolic"]
    },
    # Entry 89 - ruby-red-gears-gradient.jpg (ACTUALLY FIRE EMOJI)
    88: {
        "title": "Fire Emoji",
        "description": "3D rendered fire emoji with red and yellow flames on a red gradient background. The flame icon represents heat, passion, and trending content.",
        "conceptual": ["energy", "passion", "trending", "hot", "popular", "intense"],
        "subject": ["fire", "flame", "emoji", "3d-render", "icon"],
        "style": ["modern", "3d-render", "emoji", "clean", "bold"]
    },
    # Entry 90 - cardinal-red-gears-gradient.jpg (ACTUALLY DANCING WOMAN)
    89: {
        "title": "Dancing Woman Character",
        "description": "3D rendered cartoon woman with brown hair in red dress dancing joyfully with arms raised on a pink gradient background. The character represents celebration and happiness.",
        "conceptual": ["celebration", "joy", "happiness", "dance", "freedom", "expression"],
        "subject": ["woman", "character", "dancer", "3d-render", "figure"],
        "style": ["modern", "cartoon", "3d-render", "playful", "cheerful"]
    },
}

# Apply updates
for idx, update_data in updates.items():
    if idx < len(data):
        data[idx]["title"] = update_data["title"]
        data[idx]["description"] = update_data["description"]
        data[idx]["tags"]["conceptual"] = update_data["conceptual"]
        data[idx]["tags"]["subject"] = update_data["subject"]
        data[idx]["tags"]["style"] = update_data["style"]
        # Keep existing colors and analyzed_colors

# Save updated metadata
with open('/Users/tyler/Documents/github/editorial_feed_images/images_metadata.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Updated entries 61-90 (indices 60-89)")
print("Saved to images_metadata.json")
