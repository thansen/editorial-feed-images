#!/usr/bin/env python3
"""
Update metadata for entries 61-90 with accurate descriptions based on actual image content
Entry 61 = index 60, Entry 90 = index 89
"""

import json

# Load metadata
with open('/Users/tyler/Documents/github/editorial_feed_images/images_metadata.json', 'r') as f:
    data = json.load(f)

print(f"Total entries in metadata: {len(data)}")
print(f"\nVerifying entries 61-90 (indices 60-89):")
print(f"Entry 61 (index 60): {data[60]['newFilename']}")
print(f"Entry 90 (index 89): {data[89]['newFilename']}")

# Accurate descriptions based on actual images viewed
# Entry number: index in array is entry_number - 1

# Entry 61 (index 60) - teal-suitcase-monochrome-gradient.jpg - TEAL SUITCASE ✓
data[60].update({
    "title": "Teal Suitcase",
    "description": "3D rendered teal hard-shell suitcase with handle and latches on a teal gradient background. The luggage represents travel and journey.",
    "tags": {
        **data[60]["tags"],
        "conceptual": ["travel", "journey", "vacation", "mobility"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "minimal", "monochromatic"]
    }
})

# Entry 62 (index 61) - powder-blue-gears-gradient.jpg - RED SUITCASE
data[61].update({
    "title": "Red Suitcase",
    "description": "3D rendered red hard-shell suitcase with handle on a red gradient background. The vibrant luggage represents bold travel and adventure.",
    "tags": {
        **data[61]["tags"],
        "conceptual": ["travel", "adventure", "journey", "bold"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "monochromatic", "vibrant"]
    }
})

# Entry 63 (index 62) - copper-gears-gradient.jpg - CORAL/ORANGE SUITCASE
data[62].update({
    "title": "Coral Orange Suitcase",
    "description": "3D rendered coral orange suitcase on an orange to yellow gradient background. The warm-toned luggage represents sunny destinations.",
    "tags": {
        **data[62]["tags"],
        "conceptual": ["travel", "vacation", "warmth", "sunny"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "warm", "gradient"]
    }
})

# Entry 64 (index 63) - mustard-gears-gradient.jpg - GREEN SUITCASE
data[63].update({
    "title": "Green Suitcase",
    "description": "3D rendered green hard-shell suitcase on a green to yellow gradient background. The fresh-colored luggage represents eco-friendly travel.",
    "tags": {
        **data[63]["tags"],
        "conceptual": ["travel", "eco-friendly", "fresh", "journey"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "fresh", "gradient"]
    }
})

# Entry 65 (index 64) - champagne-gold-gears-gradient.jpg - ORANGE SUITCASE
data[64].update({
    "title": "Orange Suitcase",
    "description": "3D rendered orange hard-shell suitcase on an orange gradient background. The bright luggage represents energetic travel.",
    "tags": {
        **data[64]["tags"],
        "conceptual": ["travel", "energy", "adventure", "vibrant"],
        "subject": ["suitcase", "luggage", "travel-bag", "3d-render"],
        "style": ["modern", "clean", "3d-render", "monochromatic", "bold"]
    }
})

# Entry 66 (index 65) - teal-suitcase-variant-gradient.jpg - TEAL GEARS
data[65].update({
    "title": "Teal Gears",
    "description": "3D rendered teal mechanical gears of various sizes on a teal gradient background. The interlocking cogs represent systems and technology.",
    "tags": {
        **data[65]["tags"],
        "conceptual": ["technology", "systems", "automation", "engineering"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "clean"]
    }
})

# Entry 67 (index 66) - red-gears-monochrome-gradient.jpg - RED GEARS ✓
data[66].update({
    "title": "Red Gears",
    "description": "3D rendered red and pink mechanical gears of various sizes on a red gradient background. The machinery represents energy and power systems.",
    "tags": {
        **data[66]["tags"],
        "conceptual": ["technology", "energy", "power", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "bold"]
    }
})

# Entry 68 (index 67) - green-gears-monochrome-gradient.jpg - GREEN GEARS ✓
data[67].update({
    "title": "Green Gears",
    "description": "3D rendered green and lime mechanical gears of various sizes on a green gradient background. The machinery represents eco technology and sustainable systems.",
    "tags": {
        **data[67]["tags"],
        "conceptual": ["technology", "sustainability", "eco-friendly", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "eco"]
    }
})

# Entry 69 (index 68) - golden-metallic-gears-premium-gradient.jpg - GOLDEN GEARS ✓
data[68].update({
    "title": "Golden Metallic Gears",
    "description": "3D rendered golden metallic gears of various sizes on a yellow gradient background. The premium machinery represents value and excellence.",
    "tags": {
        **data[68]["tags"],
        "conceptual": ["technology", "excellence", "premium", "value"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render", "metal"],
        "style": ["modern", "technical", "3d-render", "luxurious", "metallic"]
    }
})

# Entry 70 (index 69) - virus-particle-green-yellow-gradient.jpg - ORANGE GEARS
data[69].update({
    "title": "Orange Gears",
    "description": "3D rendered orange mechanical gears of various sizes on an orange gradient background. The warm machinery represents energy and dynamic systems.",
    "tags": {
        **data[69]["tags"],
        "conceptual": ["technology", "energy", "dynamic", "systems"],
        "subject": ["gears", "cogs", "mechanical-parts", "3d-render"],
        "style": ["modern", "technical", "3d-render", "monochromatic", "warm"]
    }
})

# Entry 71 (index 70) - olympic-rings-red-solid.jpg - OLYMPIC RINGS ✓
data[70].update({
    "title": "Olympic Rings Red",
    "description": "3D rendered Olympic rings in blue, yellow, black, green and red on a solid red background. The iconic interlocking rings represent international sports.",
    "tags": {
        **data[70]["tags"],
        "conceptual": ["sports", "olympics", "unity", "competition", "international"],
        "subject": ["olympic-rings", "rings", "circles", "3d-render", "symbol"],
        "style": ["modern", "iconic", "3d-render", "bold", "solid"]
    }
})

# Entry 72 (index 71) - ice-blue-gears-gradient.jpg - APPLE DEVICES
data[71].update({
    "title": "Apple Devices Display",
    "description": "Multiple Apple devices including tablets and smartphones arranged on a blue gradient background showing app interfaces. The tech display represents mobile computing.",
    "tags": {
        **data[71]["tags"],
        "conceptual": ["technology", "mobile", "digital", "computing", "apps"],
        "subject": ["tablets", "smartphones", "devices", "apple", "screens"],
        "style": ["modern", "tech", "photographic", "product", "blue"]
    }
})

# Entry 73 (index 72) - sunset-gold-gears-gradient.jpg - AWARD STATUE
data[72].update({
    "title": "Golden Award Statue",
    "description": "3D rendered golden award statue resembling an Oscar trophy on an orange gradient background. The prestigious award represents achievement and excellence.",
    "tags": {
        **data[72]["tags"],
        "conceptual": ["achievement", "excellence", "award", "recognition", "success"],
        "subject": ["trophy", "award", "statue", "3d-render", "figure"],
        "style": ["modern", "elegant", "3d-render", "prestigious", "golden"]
    }
})

# Entry 74 (index 73) - lilac-gears-gradient.jpg - STUFFED ANIMALS (ELEPHANT & DONKEY)
data[73].update({
    "title": "Political Party Mascots",
    "description": "Red plush elephant and blue plush donkey stuffed animals on a purple gradient background. The toys represent American political parties.",
    "tags": {
        **data[73]["tags"],
        "conceptual": ["politics", "democracy", "parties", "america", "representation"],
        "subject": ["elephant", "donkey", "stuffed-animals", "toys", "mascots"],
        "style": ["playful", "symbolic", "photographic", "plush", "political"]
    }
})

# Entry 75 (index 74) - electric-blue-gears-gradient.jpg - DNA HELIX
data[74].update({
    "title": "DNA Double Helix",
    "description": "3D rendered DNA double helix structure in purple and pink on a purple gradient background. The molecular structure represents genetics and biology.",
    "tags": {
        **data[74]["tags"],
        "conceptual": ["science", "genetics", "biology", "research", "dna"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "technical", "biological"]
    }
})

# Entry 76 (index 75) - neon-green-gears-gradient.jpg - CIRCUIT BOARD CHIP
data[75].update({
    "title": "Circuit Board Chip",
    "description": "Glowing green circuit board chip icon with pathways radiating from center on a green gradient background. The tech symbol represents computing and processors.",
    "tags": {
        **data[75]["tags"],
        "conceptual": ["technology", "computing", "digital", "processing", "electronics"],
        "subject": ["chip", "circuit-board", "processor", "icon", "technology"],
        "style": ["modern", "glowing", "icon", "technical", "neon"]
    }
})

# Entry 77 (index 76) - mint-green-gears-gradient-1.jpg - PLAYSTATION CONTROLLER
data[76].update({
    "title": "PlayStation Controller",
    "description": "Black PlayStation game controller on a pink gradient background. The gaming device represents video games and entertainment.",
    "tags": {
        **data[76]["tags"],
        "conceptual": ["gaming", "entertainment", "play", "video-games", "leisure"],
        "subject": ["controller", "gamepad", "playstation", "device", "gaming"],
        "style": ["modern", "photographic", "product", "clean", "gaming"]
    }
})

# Entry 78 (index 77) - sage-green-gears-gradient.jpg - DEMON CHARACTER
data[77].update({
    "title": "Fantasy Demon Character",
    "description": "Digital art of a red demon or dark fantasy character with horned crown on a red gradient background. The creature represents dark fantasy and mythology.",
    "tags": {
        **data[77]["tags"],
        "conceptual": ["fantasy", "mythology", "dark", "supernatural", "fiction"],
        "subject": ["demon", "character", "creature", "fantasy", "portrait"],
        "style": ["digital-art", "dark", "fantasy", "atmospheric", "illustration"]
    }
})

# Entry 79 (index 78) - baby-blue-gears-gradient.jpg - SOCCER BALL WITH WORLD MAP
data[78].update({
    "title": "World Map Soccer",
    "description": "Soccer ball with world map continents printed on it on a green background. The globe ball represents international football and world sports.",
    "tags": {
        **data[78]["tags"],
        "conceptual": ["sports", "global", "soccer", "international", "unity"],
        "subject": ["soccer-ball", "globe", "world-map", "ball", "sports"],
        "style": ["photographic", "symbolic", "sports", "global", "creative"]
    }
})

# Entry 80 (index 79) - peacock-blue-gears-gradient.jpg - BROKEN TV
data[79].update({
    "title": "Broken TV Monitor",
    "description": "Broken CRT television with cracked screen and exposed circuit boards on a green gradient background. The damaged tech represents obsolescence and decay.",
    "tags": {
        **data[79]["tags"],
        "conceptual": ["obsolescence", "technology", "broken", "decay", "e-waste"],
        "subject": ["television", "monitor", "screen", "circuit-board", "broken"],
        "style": ["photographic", "grungy", "damaged", "retro", "tech"]
    }
})

# Entry 81 (index 80) - coral-pink-gears-gradient.jpg - DNA HELIX
data[80].update({
    "title": "DNA Helix Purple",
    "description": "3D rendered DNA double helix structure in purple tones on a purple gradient background. The genetic structure represents life science and heredity.",
    "tags": {
        **data[80]["tags"],
        "conceptual": ["science", "genetics", "biology", "heredity", "research"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "gradient", "biological"]
    }
})

# Entry 82 (index 81) - kelly-green-gears-gradient.jpg - SOCCER BALL
data[81].update({
    "title": "Soccer Ball",
    "description": "Classic black and white soccer ball on green turf or grass background. The football represents the world's most popular sport.",
    "tags": {
        **data[81]["tags"],
        "conceptual": ["sports", "soccer", "football", "athletics", "competition"],
        "subject": ["soccer-ball", "ball", "football", "sports-equipment", "turf"],
        "style": ["photographic", "sports", "classic", "clean", "realistic"]
    }
})

# Entry 83 (index 82) - orchid-purple-gears-gradient.jpg - SHOPPING CART
data[82].update({
    "title": "Shopping Cart",
    "description": "3D rendered shopping cart with blue frame and orange handles on a blue gradient background. The cart represents e-commerce and retail.",
    "tags": {
        **data[82]["tags"],
        "conceptual": ["shopping", "e-commerce", "retail", "consumerism", "purchase"],
        "subject": ["shopping-cart", "cart", "basket", "3d-render", "retail"],
        "style": ["modern", "clean", "3d-render", "minimal", "commercial"]
    }
})

# Entry 84 (index 83) - cherry-red-gears-gradient.jpg - POLICE TAPE
data[83].update({
    "title": "Police Caution Tape",
    "description": "Yellow and black striped police caution tape reading 'CAUTION POLICE' on an orange to red gradient background. The barrier tape represents law enforcement and crime scenes.",
    "tags": {
        **data[83]["tags"],
        "conceptual": ["law-enforcement", "crime", "caution", "warning", "security", "investigation"],
        "subject": ["police-tape", "caution-tape", "barrier", "warning", "text"],
        "style": ["photographic", "realistic", "warning", "bold", "official"]
    }
})

# Entry 85 (index 84) - lemon-yellow-gears-gradient.jpg - ROCK HAND GESTURE
data[84].update({
    "title": "Rock Hand Sign",
    "description": "3D rendered metallic bronze hand making rock and roll horn gesture on a dark purple to red gradient background. The hand symbol represents music and rock culture.",
    "tags": {
        **data[84]["tags"],
        "conceptual": ["music", "rock", "culture", "rebellion", "expression", "gesture"],
        "subject": ["hand", "gesture", "sign", "3d-render", "fingers"],
        "style": ["modern", "3d-render", "metallic", "bold", "cultural"]
    }
})

# Entry 86 (index 85) - ocean-blue-gears-gradient.jpg - DNA HELIX
data[85].update({
    "title": "DNA Helix Purple",
    "description": "3D rendered DNA double helix structure in purple on a purple gradient background. The genetic structure represents biology and science.",
    "tags": {
        **data[85]["tags"],
        "conceptual": ["science", "genetics", "biology", "research", "dna", "heredity"],
        "subject": ["dna", "helix", "molecule", "structure", "3d-render"],
        "style": ["modern", "scientific", "3d-render", "technical", "monochromatic"]
    }
})

# Entry 87 (index 86) - fuchsia-gears-gradient.jpg - HEART IN HANDS EMOJI
data[86].update({
    "title": "Heart in Hands",
    "description": "3D rendered emoji of two hands holding a red heart on a pink gradient background. The caring gesture represents love and compassion.",
    "tags": {
        **data[86]["tags"],
        "conceptual": ["love", "care", "compassion", "charity", "kindness", "support"],
        "subject": ["heart", "hands", "emoji", "3d-render", "gesture"],
        "style": ["modern", "3d-render", "emoji", "clean", "symbolic"]
    }
})

# Entry 88 (index 87) - vermillion-gears-gradient.jpg - OLYMPIC RINGS
data[87].update({
    "title": "Olympic Rings Coral",
    "description": "3D rendered Olympic rings in blue, yellow, black, green and red on a coral orange gradient background. The interlocking rings represent international sports.",
    "tags": {
        **data[87]["tags"],
        "conceptual": ["sports", "olympics", "unity", "competition", "international", "athletics"],
        "subject": ["olympic-rings", "rings", "circles", "3d-render", "symbol"],
        "style": ["modern", "iconic", "3d-render", "clean", "symbolic"]
    }
})

# Entry 89 (index 88) - ruby-red-gears-gradient.jpg - FIRE EMOJI
data[88].update({
    "title": "Fire Emoji",
    "description": "3D rendered fire emoji with red and yellow flames on a red gradient background. The flame icon represents heat, passion, and trending content.",
    "tags": {
        **data[88]["tags"],
        "conceptual": ["energy", "passion", "trending", "hot", "popular", "intense"],
        "subject": ["fire", "flame", "emoji", "3d-render", "icon"],
        "style": ["modern", "3d-render", "emoji", "clean", "bold"]
    }
})

# Entry 90 (index 89) - cardinal-red-gears-gradient.jpg - DANCING WOMAN
data[89].update({
    "title": "Dancing Woman Character",
    "description": "3D rendered cartoon woman with brown hair in red dress dancing joyfully with arms raised on a pink gradient background. The character represents celebration and happiness.",
    "tags": {
        **data[89]["tags"],
        "conceptual": ["celebration", "joy", "happiness", "dance", "freedom", "expression"],
        "subject": ["woman", "character", "dancer", "3d-render", "figure"],
        "style": ["modern", "cartoon", "3d-render", "playful", "cheerful"]
    }
})

# Save updated metadata
with open('/Users/tyler/Documents/github/editorial_feed_images/images_metadata.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\n✓ Updated entries 61-90 (indices 60-89) with accurate descriptions")
print(f"✓ Saved to images_metadata.json")
print(f"\nSample verification:")
print(f"Entry 61: {data[60]['title']} - {data[60]['newFilename']}")
print(f"Entry 90: {data[89]['title']} - {data[89]['newFilename']}")
