#!/usr/bin/env python3
"""
Script to update the first 30 entries in images_metadata.json with accurate descriptions
based on actual image analysis.
"""

import json

# Load the existing metadata
with open('images_metadata.json', 'r') as f:
    data = json.load(f)

# Updated metadata for first 30 images based on actual image analysis
updated_entries = [
    {
        "title": "Olympic Rings Pink",
        "description": "3D rendered Olympic rings in their traditional colors (blue, yellow, black, green, red) displayed on a vibrant pink to red gradient background. The iconic interlocking rings create depth with subtle shadows.",
        "conceptual": ["sports", "competition", "unity", "international", "excellence", "achievement"],
        "subject": ["olympic-rings", "circles", "interlocking", "3d-render", "symbol"],
        "style": ["modern", "clean", "3d-render", "minimalist", "vibrant", "gradient"]
    },
    {
        "title": "Silver Rocket Launch",
        "description": "3D rendered silver rocket ship with red nose cone and blue circular window, launching with yellow and orange flame exhaust on a pink to orange gradient background. The rocket symbolizes innovation and space exploration.",
        "conceptual": ["innovation", "launch", "startup", "growth", "exploration", "technology"],
        "subject": ["rocket", "spacecraft", "flame", "3d-render", "vehicle"],
        "style": ["modern", "3d-render", "playful", "dynamic", "vibrant", "gradient"]
    },
    {
        "title": "American Football Brown",
        "description": "3D rendered brown leather American football with white lacing and stripes on a light to dark blue gradient background. The football is positioned at an angle showing its distinctive oval shape and textured surface.",
        "conceptual": ["sports", "competition", "american", "athletics", "teamwork", "game"],
        "subject": ["football", "ball", "leather", "3d-render", "sports-equipment"],
        "style": ["realistic", "3d-render", "clean", "modern", "gradient", "minimalist"]
    },
    {
        "title": "Baseball Bat Wood",
        "description": "Wooden baseball bat and white baseball with red stitching on a light to dark blue gradient background. The bat shows natural wood grain texture and the baseball displays traditional curved seam pattern.",
        "conceptual": ["sports", "baseball", "american", "game", "recreation", "athletics"],
        "subject": ["baseball-bat", "baseball", "bat", "ball", "sports-equipment"],
        "style": ["realistic", "clean", "modern", "gradient", "minimalist", "3d-render"]
    },
    {
        "title": "Blue Purple Gears",
        "description": "Multiple 3D rendered mechanical gears in various sizes arranged on a blue to purple gradient background. The interlocking cogwheels feature toothed edges and cylindrical centers, creating a sense of mechanical complexity.",
        "conceptual": ["mechanics", "engineering", "industry", "technology", "machinery", "system"],
        "subject": ["gears", "cogwheels", "mechanism", "3d-render", "machinery"],
        "style": ["modern", "3d-render", "technical", "gradient", "clean", "minimalist"]
    },
    {
        "title": "White Rain Cloud",
        "description": "3D rendered white cumulus cloud with three blue raindrops falling beneath it on a light to dark blue gradient background. The soft, fluffy cloud casts a subtle shadow on the gradient surface below.",
        "conceptual": ["weather", "rain", "nature", "precipitation", "climate", "atmosphere"],
        "subject": ["cloud", "raindrops", "weather", "3d-render", "sky"],
        "style": ["minimalist", "3d-render", "soft", "clean", "gradient", "modern"]
    },
    {
        "title": "Robotic Arm Blue",
        "description": "3D rendered metallic silver and blue robotic arm with articulated joints and cylindrical segments on a blue gradient background. The industrial robot arm shows modern mechanical engineering with smooth surfaces and precise joints.",
        "conceptual": ["automation", "robotics", "technology", "industry", "manufacturing", "artificial-intelligence"],
        "subject": ["robotic-arm", "robot", "machinery", "3d-render", "mechanical"],
        "style": ["modern", "3d-render", "technical", "sleek", "gradient", "industrial"]
    },
    {
        "title": "Praying Hands Orange",
        "description": "3D rendered orange hands pressed together in prayer position with blue sleeve cuffs on a light to dark blue gradient background. The emoji-style hands are shown in a traditional prayer or gratitude gesture.",
        "conceptual": ["prayer", "faith", "gratitude", "spirituality", "hope", "meditation"],
        "subject": ["hands", "praying-hands", "gesture", "3d-render", "emoji"],
        "style": ["modern", "3d-render", "minimalist", "clean", "gradient", "emoji-style"]
    },
    {
        "title": "Justice Scales Blue",
        "description": "3D rendered balance scales with blue body and gold pans on a light to dark blue gradient background. The traditional justice symbol features two balanced golden bowls suspended from a blue central beam and stand.",
        "conceptual": ["justice", "law", "balance", "fairness", "legal", "equality"],
        "subject": ["scales", "balance", "justice-symbol", "3d-render", "legal"],
        "style": ["modern", "3d-render", "clean", "symbolic", "gradient", "minimalist"]
    },
    {
        "title": "Game Controller Blue",
        "description": "PlayStation-style game controller in blue with black touchpad and multicolored buttons on a light to dark blue gradient background. The realistic controller features dual analog sticks, d-pad, and action buttons.",
        "conceptual": ["gaming", "entertainment", "video-games", "play", "technology", "recreation"],
        "subject": ["game-controller", "gamepad", "playstation", "controller", "gaming-device"],
        "style": ["realistic", "modern", "clean", "gradient", "minimalist", "3d-render"]
    },
    {
        "title": "City Skyline Blue",
        "description": "3D rendered futuristic city skyline with tall skyscrapers and buildings in various shades of blue and white on a blue to cyan gradient background. The isometric view shows a dense urban landscape with architectural variety.",
        "conceptual": ["urban", "city", "architecture", "metropolitan", "modern", "development"],
        "subject": ["cityscape", "buildings", "skyscrapers", "3d-render", "urban"],
        "style": ["modern", "3d-render", "isometric", "clean", "gradient", "futuristic"]
    },
    {
        "title": "Starry Night Sky",
        "description": "Night sky filled with countless white stars of varying brightness scattered across a dark to light blue gradient background. The celestial scene creates a peaceful, cosmic atmosphere with natural star distribution.",
        "conceptual": ["space", "cosmos", "night", "astronomy", "celestial", "universe"],
        "subject": ["stars", "night-sky", "space", "cosmos", "celestial"],
        "style": ["realistic", "gradient", "atmospheric", "serene", "minimalist", "cosmic"]
    },
    {
        "title": "Petri Dish Bacteria",
        "description": "Overhead view of a petri dish with blue bacterial colonies growing in circular patterns on a light blue gradient background. The glass dish shows microscopic organisms forming spotted clusters across the culture medium.",
        "conceptual": ["science", "biology", "microbiology", "research", "laboratory", "medicine"],
        "subject": ["petri-dish", "bacteria", "colonies", "laboratory", "science"],
        "style": ["scientific", "realistic", "clean", "gradient", "medical", "microscopic"]
    },
    {
        "title": "Game Controller Black",
        "description": "Black PlayStation-style game controller with glossy finish and multicolored buttons on a vibrant pink to magenta gradient background. The controller shows realistic details including dual analog sticks, touchpad, and PlayStation logo.",
        "conceptual": ["gaming", "entertainment", "video-games", "play", "technology", "recreation"],
        "subject": ["game-controller", "gamepad", "playstation", "controller", "gaming-device"],
        "style": ["realistic", "modern", "clean", "gradient", "vibrant", "product-photography"]
    },
    {
        "title": "Office Workspace Blue",
        "description": "Minimalist office workspace with white desk, modern chair, and laptop on a light to dark blue gradient background. The clean setup shows a contemporary work environment with sleek furniture and simple design.",
        "conceptual": ["work", "office", "productivity", "business", "professional", "workspace"],
        "subject": ["desk", "chair", "office", "workspace", "furniture"],
        "style": ["minimalist", "modern", "clean", "gradient", "simple", "3d-render"]
    },
    {
        "title": "Teal Chain Links",
        "description": "Multiple interlocking teal chain links on a dark teal gradient background. The 3D rendered chains show metallic texture and realistic connecting links forming a network pattern in the corner.",
        "conceptual": ["connection", "link", "network", "strength", "unity", "blockchain"],
        "subject": ["chains", "links", "metal", "3d-render", "connection"],
        "style": ["modern", "3d-render", "technical", "gradient", "minimalist", "metallic"]
    },
    {
        "title": "Hurricane Spiral View",
        "description": "Satellite view of a hurricane with distinctive spiral cloud formations and visible eye at center on a pink to blue gradient background. The weather system shows the characteristic swirling pattern of a tropical cyclone.",
        "conceptual": ["weather", "storm", "nature", "climate", "disaster", "power"],
        "subject": ["hurricane", "storm", "clouds", "cyclone", "weather-system"],
        "style": ["realistic", "satellite-view", "dramatic", "gradient", "atmospheric", "natural"]
    },
    {
        "title": "Greenland Map White",
        "description": "3D relief map of Greenland showing topographical features with white landmass and blue ocean on a blue gradient background. The map displays the island's distinctive shape with detailed coastline and terrain elevation.",
        "conceptual": ["geography", "cartography", "arctic", "land", "territory", "location"],
        "subject": ["map", "greenland", "geography", "3d-render", "topography"],
        "style": ["clean", "3d-render", "cartographic", "gradient", "minimalist", "technical"]
    },
    {
        "title": "Dinosaur Skeleton Purple",
        "description": "3D rendered T-Rex dinosaur skeleton in complete anatomical detail on a pink to purple gradient background. The fossil display shows the predator's characteristic large skull, teeth, ribcage, and skeletal structure.",
        "conceptual": ["paleontology", "prehistoric", "history", "extinction", "science", "evolution"],
        "subject": ["dinosaur", "skeleton", "fossil", "t-rex", "bones"],
        "style": ["modern", "3d-render", "scientific", "gradient", "detailed", "educational"]
    },
    {
        "title": "Crowd Diversity Figures",
        "description": "Large group of simplified 3D human figures in various colors (red, orange, pink, purple, blue) arranged in rows on a red gradient background. The crowd represents diversity with different colored individuals standing together.",
        "conceptual": ["diversity", "crowd", "population", "community", "unity", "society"],
        "subject": ["people", "figures", "crowd", "3d-render", "humans"],
        "style": ["modern", "3d-render", "minimalist", "gradient", "abstract", "symbolic"]
    },
    {
        "title": "Gaming Setup Purple",
        "description": "Complete gaming workstation with RGB-lit gaming PC, curved monitor displaying game, mechanical keyboard, gaming mouse, headset, and racing-style chair on a purple gradient background. The setup features vibrant LED lighting creating a modern gaming atmosphere.",
        "conceptual": ["gaming", "technology", "entertainment", "esports", "setup", "streaming"],
        "subject": ["gaming-setup", "computer", "monitor", "desk", "gaming-chair"],
        "style": ["modern", "3d-render", "detailed", "gradient", "atmospheric", "rgb-lighting"]
    },
    {
        "title": "Protest March Illustration",
        "description": "Illustrated crowd of diverse protesters marching with signs and banners on a purple gradient background. The stylized artwork shows people of different ethnicities holding various protest signs in a peaceful demonstration.",
        "conceptual": ["protest", "activism", "social-justice", "demonstration", "rights", "movement"],
        "subject": ["protesters", "march", "crowd", "signs", "people"],
        "style": ["illustrated", "artistic", "gradient", "modern", "colorful", "editorial"]
    },
    {
        "title": "Olympic Rings Red",
        "description": "3D rendered Olympic rings in their traditional colors (blue, yellow, black, green, red) on a red to orange gradient background. The iconic interlocking circles are shown with depth and cast subtle shadows.",
        "conceptual": ["sports", "competition", "unity", "international", "excellence", "achievement"],
        "subject": ["olympic-rings", "circles", "interlocking", "3d-render", "symbol"],
        "style": ["modern", "clean", "3d-render", "minimalist", "vibrant", "gradient"]
    },
    {
        "title": "Circular Waves Orange",
        "description": "Concentric circular waves or ripples in varying shades of orange creating a layered geometric pattern on an orange gradient background. The design resembles sound waves or water ripples emanating from a central point.",
        "conceptual": ["waves", "sound", "rhythm", "pattern", "flow", "energy"],
        "subject": ["circles", "waves", "ripples", "pattern", "geometric"],
        "style": ["abstract", "modern", "gradient", "minimalist", "geometric", "layered"]
    },
    {
        "title": "Angry Emoji Orange",
        "description": "3D rendered angry face emoji with furrowed eyebrows, frowning mouth, and censored text symbol on a yellow to orange gradient background. The expressive emoji conveys frustration or anger with exaggerated facial features.",
        "conceptual": ["emotion", "anger", "frustration", "expression", "mood", "feeling"],
        "subject": ["emoji", "face", "angry", "emoticon", "3d-render"],
        "style": ["modern", "3d-render", "expressive", "gradient", "emoji-style", "playful"]
    },
    {
        "title": "Stressed Emoji Red",
        "description": "3D rendered anxious or stressed face emoji in red with worried expression and sweat drops on a red gradient background. The emoji shows downturned eyebrows and multiple perspiration droplets indicating stress or concern.",
        "conceptual": ["stress", "anxiety", "worry", "emotion", "pressure", "concern"],
        "subject": ["emoji", "face", "stressed", "emoticon", "3d-render"],
        "style": ["modern", "3d-render", "expressive", "gradient", "emoji-style", "emotional"]
    },
    {
        "title": "Curved Waves Red",
        "description": "Layered curved waves or bands in shades of orange and red creating a flowing geometric pattern on a red to orange gradient background. The design features smooth transitions between concentric arcs.",
        "conceptual": ["waves", "flow", "pattern", "rhythm", "movement", "energy"],
        "subject": ["waves", "curves", "layers", "pattern", "geometric"],
        "style": ["abstract", "modern", "gradient", "minimalist", "geometric", "flowing"]
    },
    {
        "title": "Wavy Lines Purple",
        "description": "Abstract wavy horizontal lines in varying shades of purple creating a flowing pattern on a purple gradient background. The undulating stripes suggest movement and fluidity with smooth color transitions.",
        "conceptual": ["waves", "flow", "pattern", "rhythm", "movement", "abstract"],
        "subject": ["waves", "lines", "stripes", "pattern", "abstract"],
        "style": ["abstract", "modern", "gradient", "minimalist", "flowing", "smooth"]
    },
    {
        "title": "Capsule Pills Orange",
        "description": "3D rendered pharmaceutical capsules in blue and orange colors scattered on an orange gradient background. The two-toned pill capsules show realistic texture and lighting, representing medication or supplements.",
        "conceptual": ["medicine", "health", "pharmaceutical", "treatment", "medication", "healthcare"],
        "subject": ["pills", "capsules", "medication", "pharmaceutical", "3d-render"],
        "style": ["realistic", "3d-render", "clean", "gradient", "modern", "medical"]
    },
    {
        "title": "Orange Gears Gradient",
        "description": "Multiple 3D rendered mechanical gears in various sizes in shades of orange on an orange to red gradient background. The interlocking cogwheels feature toothed edges and create a sense of mechanical complexity and movement.",
        "conceptual": ["mechanics", "engineering", "industry", "technology", "machinery", "system"],
        "subject": ["gears", "cogwheels", "mechanism", "3d-render", "machinery"],
        "style": ["modern", "3d-render", "technical", "gradient", "clean", "mechanical"]
    }
]

# Update the first 30 entries
for i in range(30):
    # Update title and description
    data[i]['title'] = updated_entries[i]['title']
    data[i]['description'] = updated_entries[i]['description']

    # Update tags
    data[i]['tags']['conceptual'] = updated_entries[i]['conceptual']
    data[i]['tags']['subject'] = updated_entries[i]['subject']
    data[i]['tags']['style'] = updated_entries[i]['style']

    # Keep existing: originalFilename, newFilename, colors, analyzed_colors

# Save the updated metadata
with open('images_metadata.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✓ Successfully updated the first 30 entries in images_metadata.json\n")
print("Updated entries:")
print("=" * 80)
for i in range(30):
    print(f"{i+1:2d}. {data[i]['newFilename']:50s} - {data[i]['title']}")
print("=" * 80)
print(f"\nTotal entries in file: {len(data)}")
print("First 30 entries have been updated with accurate descriptions based on actual image analysis.")
