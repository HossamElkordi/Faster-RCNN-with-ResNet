import os

split = []
with os.scandir('DataImages/') as entries:
    for entry in entries:
        image_id = entry.name.split('_')[0]
        filepath = os.path.join('DataImages/', entry.name)
        split.append((filepath, image_id))

print(split)