#!/usr/bin/env python3
"""
Map analyzed images to correct metadata entries and update
"""
import json

# Load metadata
with open('images_metadata.json', 'r') as f:
    data = json.load(f)

# Find entries by filename and update them
filename_updates = {
    "teal-suitcase-monochrome-gradient.jpg": {
        "title": "Teal Suitcase",
        "description": "3D rendered teal hard-shell suitcase with handle and latches on a teal gradient background. The luggage represents travel and journey.",
        "conceptual": ["travel", "journey", "vacation", "mobility"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "minimal", "monochromatic"]
    },
    "powder-blue-gears-gradient.jpg": {
        "title": "Red Suitcase",
        "description": "3D rendered red hard-shell suitcase with handle on a red gradient background. The vibrant luggage represents bold travel and adventure.",
        "conceptual": ["travel", "adventure", "journey", "bold"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "monochromatic", "vibrant"]
    },
    "copper-gears-gradient.jpg": {
        "title": "Coral Orange Suitcase",
        "description": "3D rendered coral orange suitcase on an orange to yellow gradient background. The warm-toned luggage represents sunny destinations.",
        "conceptual": ["travel", "vacation", "warmth", "sunny"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "warm", "gradient"]
    },
    "mustard-gears-gradient.jpg": {
        "title": "Green Suitcase",
        "description": "3D rendered green hard-shell suitcase on a green to yellow gradient background. The fresh-colored luggage represents eco-friendly travel.",
        "conceptual": ["travel", "eco-friendly", "fresh", "journey"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "fresh", "gradient"]
    },
    "champagne-gold-gears-gradient.jpg": {
        "title": "Orange Suitcase",
        "description": "3D rendered orange hard-shell suitcase on an orange gradient background. The bright luggage represents energetic travel.",
        "conceptual": ["travel", "energy", "adventure", "vibrant"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "monochromatic", "bold"]
    },
    "teal-suitcase-variant-gradient.jpg": {
        "title": "Teal Gears",
        "description": "3D rendered teal mechanical gears of various sizes on a teal gradient background. The interlocking cogs represent systems and technology.",
        "conceptual": ["technology", "systems", "automation", "engineering"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "clean"]
    },
    "red-gears-monochrome-gradient.jpg": {
        "title": "Red Gears",
        "description": "3D rendered red and pink mechanical gears of various sizes on a red gradient background. The machinery represents energy and power systems.",
        "conceptual": ["technology", "energy", "power", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "bold"]
    },
    "green-gears-monochrome-gradient.jpg": {
        "title": "Green Gears",
        "description": "3D rendered green and lime mechanical gears of various sizes on a green gradient background. The machinery represents eco technology and sustainable systems.",
        "conceptual": ["technology", "sustainability", "eco-friendly", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "eco"]
    },
    "golden-metallic-gears-premium-gradient.jpg": {
        "title": "Golden Metallic Gears",
        "description": "3D rendered golden metallic gears of various sizes on a yellow gradient background. The premium machinery represents value and excellence.",
        "conceptual": ["technology", "excellence", "premium", "value"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render", "metal"],
        "style": ["modern", "technical", "3d-render", "luxurious", "metallic"]
    },
    "virus-particle-green-yellow-gradient.jpg": {
        "title": "Orange Gears",
        "description": "3D rendered orange mechanical gears of various sizes on an orange gradient background. The warm machinery represents energy and dynamic systems.",
        "conceptual": ["technology", "energy", "dynamic", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "warm"]
    },
    "olympic-rings-red-solid.jpg": {
        "title": "Olympic Rings Red",
        "description": "3D rendered Olympic rings in blue, yellow, black, green and red on a solid red background. The iconic interlocking rings represent international sports.",
        "conceptual": ["sports", "olympics", "unity", "competition", "international"],
        "subject": ["olympic-rings", "rings", "circles", "3d-render", "symbol"],
        "style": ["modern", "iconic", "3d-render", "bold", "solid"]
    },
    "ice-blue-gears-gradient.jpg": {
        "title": "Apple Devices Display",
        "description": "Multiple Apple devices including tablets and smartphones arranged on a blue gradient background showing app interfaces. The tech display represents mobile computing.",
        "conceptual": ["technology", "mobile", "digital", "computing", "apps"],
        "subject": ["tablets", "smartphones", "devices", "apple", "screens"],
        "style": ["modern", "tech", "photographic", "product", "blue"]
    },
    "sunset-gold-gears-gradient.jpg": {
        "title": "Golden Award Statue",
        "description": "3D rendered golden award statue resembling an Oscar trophy on an orange gradient background. The prestigious award represents achievement and excellence.",
        "conceptual": ["achievement", "excellence", "award", "recognition", "success"],
        "subject": ["trophy", "award", "statue", "3d-render", "figure"],
        "style": ["modern", "elegant", "3d-render", "prestigious", "golden"]
    },
    "lilac-gears-gradient.jpg": {
        "title": "Political Party Mascots",
        "description": "Red plush elephant and blue plush donkey stuffed animals on a purple gradient background. The toys represent American political parties.",
        "conceptual": ["politics", "democracy", "parties", "america", "representation"],
        "subject": ["elephant", "donkey", "stuffed-animals", "toys", "mascots"],
        "style": ["playful", "symbolic", "photographic", "plush", "political"]
    },
    "electric-blue-gears-gradient.jpg": {
        "title": "DNA Double Helix",
        "description": "3D rendered DNA double helix structure in purple and pink on a purple gradient background. The molecular structure represents genetics and biology.",
        "conceptual": ["science", "genetics", "biology", "research", "dna"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "technical", "biological"]
    },
    "neon-green-gears-gradient.jpg": {
        "title": "Circuit Board Chip",
        "description": "Glowing green circuit board chip icon with pathways radiating from center on a green gradient background. The tech symbol represents computing and processors.",
        "conceptual": ["technology", "computing", "digital", "processing", "electronics"],
        "subject": ["chip", "circuit-board", "processor", "icon", "technology"],
        "style": ["modern", "glowing", "icon", "technical", "neon"]
    },
    "mint-green-gears-gradient-1.jpg": {
        "title": "PlayStation Controller",
        "description": "Black PlayStation game controller on a pink gradient background. The gaming device represents video games and entertainment.",
        "conceptual": ["gaming", "entertainment", "play", "video-games", "leisure"],
        "subject": ["controller", "gamepad", "playstation", "device", "gaming"],
        "style": ["modern", "photographic", "product", "clean", "gaming"]
    },
    "sage-green-gears-gradient.jpg": {
        "title": "Fantasy Demon Character",
        "description": "Digital art of a red demon or dark fantasy character with horned crown on a red gradient background. The creature represents dark fantasy and mythology.",
        "conceptual": ["fantasy", "mythology", "dark", "supernatural", "fiction"],
        "subject": ["demon", "character", "creature", "fantasy", "portrait"],
        "style": ["digital-art", "dark", "fantasy", "atmospheric", "illustration"]
    },
    "baby-blue-gears-gradient.jpg": {
        "title": "World Map Soccer",
        "description": "Soccer ball with world map continents printed on it on a green background. The globe ball represents international football and world sports.",
        "conceptual": ["sports", "global", "soccer", "international", "unity"],
        "subject": ["soccer-ball", "globe", "world-map", "ball", "sports"],
        "style": ["photographic", "symbolic", "sports", "global", "creative"]
    },
    "peacock-blue-gears-gradient.jpg": {
        "title": "Broken TV Monitor",
        "description": "Broken CRT television with cracked screen and exposed circuit boards on a green gradient background. The damaged tech represents obsolescence and decay.",
        "conceptual": ["obsolescence", "technology", "broken", "decay", "e-waste"],
        "subject": ["television", "monitor", "screen", "circuit-board", "broken"],
        "style": ["photographic", "grungy", "damaged", "retro", "tech"]
    },
    "coral-pink-gears-gradient.jpg": {
        "title": "DNA Helix Purple",
        "description": "3D rendered DNA double helix structure in purple tones on a purple gradient background. The genetic structure represents life science and heredity.",
        "conceptual": ["science", "genetics", "biology", "heredity", "research"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "gradient", "biological"]
    },
    "kelly-green-gears-gradient.jpg": {
        "title": "Soccer Ball",
        "description": "Classic black and white soccer ball on green turf or grass background. The football represents the world's most popular sport.",
        "conceptual": ["sports", "soccer", "football", "athletics", "competition"],
        "subject": ["soccer-ball", "ball", "football", "sports-equipment", "turf"],
        "style": ["photographic", "sports", "classic", "clean", "realistic"]
    },
    "orchid-purple-gears-gradient.jpg": {
        "title": "Shopping Cart",
        "description": "3D rendered shopping cart with blue frame and orange handles on a blue gradient background. The cart represents e-commerce and retail.",
        "conceptual": ["shopping", "e-commerce", "retail", "consumerism", "purchase"],
        "subject": ["shopping-cart", "cart", "basket", "3d-render", "retail"],
        "style": ["modern", "clean", "3d-render", "minimal", "commercial"]
    },
    "cherry-red-gears-gradient.jpg": {
        "title": "Police Caution Tape",
        "description": "Yellow and black striped police caution tape reading 'CAUTION POLICE' on an orange to red gradient background. The barrier tape represents law enforcement and crime scenes.",
        "conceptual": ["law-enforcement", "crime", "caution", "warning", "security", "investigation"],
        "subject": ["police-tape", "caution-tape", "barrier", "warning", "text"],
        "style": ["photographic", "realistic", "warning", "bold", "official"]
    },
    "lemon-yellow-gears-gradient.jpg": {
        "title": "Rock Hand Sign",
        "description": "3D rendered metallic bronze hand making rock and roll horn gesture on a dark purple to red gradient background. The hand symbol represents music and rock culture.",
        "conceptual": ["music", "rock", "culture", "rebellion", "expression", "gesture"],
        "subject": ["hand", "gesture", "sign", "3d-render", "fingers"],
        "style": ["modern", "3d-render", "metallic", "bold", "cultural"]
    },
    "ocean-blue-gears-gradient.jpg": {
        "title": "DNA Helix Purple",
        "description": "3D rendered DNA double helix structure in purple on a purple gradient background. The genetic structure represents biology and science.",
        "conceptual": ["science", "genetics", "biology", "research", "dna", "heredity"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "technical", "monochromatic"]
    },
    "fuchsia-gears-gradient.jpg": {
        "title": "Heart in Hands",
        "description": "3D rendered emoji of two hands holding a red heart on a pink gradient background. The caring gesture represents love and compassion.",
        "conceptual": ["love", "care", "compassion", "charity", "kindness", "support"],
        "subject": ["heart", "hands", "emoji", "3d-render", "gesture"],
        "style": ["modern", "3d-render", "emoji", "clean", "symbolic"]
    },
    "vermillion-gears-gradient.jpg": {
        "title": "Olympic Rings Coral",
        "description": "3D rendered Olympic rings in blue, yellow, black, green and red on a coral orange gradient background. The interlocking rings represent international sports.",
        "conceptual": ["sports", "olympics", "unity", "competition", "international", "athletics"],
        "subject": ["olympic-rings", "rings", "circles", "3d-render", "symbol"],
        "style": ["modern", "iconic", "3d-render", "clean", "symbolic"]
    },
    "ruby-red-gears-gradient.jpg": {
        "title": "Fire Emoji",
        "description": "3D rendered fire emoji with red and yellow flames on a red gradient background. The flame icon represents heat, passion, and trending content.",
        "conceptual": ["energy", "passion", "trending", "hot", "popular", "intense"],
        "subject": ["fire", "flame", "emoji", "3d-render", "icon"],
        "style": ["modern", "3d-render", "emoji", "clean", "bold"]
    },
    "cardinal-red-gears-gradient.jpg": {
        "title": "Dancing Woman Character",
        "description": "3D rendered cartoon woman with brown hair in red dress dancing joyfully with arms raised on a pink gradient background. The character represents celebration and happiness.",
        "conceptual": ["celebration", "joy", "happiness", "dance", "freedom", "expression"],
        "subject": ["woman", "character", "dancer", "3d-render", "figure"],
        "style": ["modern", "cartoon", "3d-render", "playful", "cheerful"]
    },
}

# Find and update entries by filename
updated_count = 0
entries_in_range = []

for i, entry in enumerate(data):
    filename = entry['newFilename']
    if filename in filename_updates:
        update = filename_updates[filename]
        entry['title'] = update['title']
        entry['description'] = update['description']
        entry['tags']['conceptual'] = update['conceptual']
        entry['tags']['subject'] = update['subject']
        entry['tags']['style'] = update['style']
        updated_count += 1

        # Track if this is in entries 61-90
        if 60 <= i <= 89:
            entries_in_range.append(i+1)

        print(f"✓ Updated entry {i+1}: {filename} -> {update['title']}")

# Save updated metadata
with open('images_metadata.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n{'='*80}")
print(f"✓ Updated {updated_count} entries with accurate descriptions")
print(f"✓ Entries in range 61-90 that were updated: {entries_in_range}")
print(f"✓ Saved to images_metadata.json")
