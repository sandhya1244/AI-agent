import os
import re

html_file = "index_local.html"
asset_dir = "downloaded_assets"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

srcs = re.findall(r'src=["\'](downloaded_assets/[^"\']+)["\']', html)
missing = []

for path in srcs:
    full_path = os.path.join(".", path)
    if not os.path.exists(full_path):
        missing.append(path)

if missing:
    print("❌ Missing files referenced in HTML:")
    for m in missing:
        print(f" - {m}")
else:
    print("✅ All image paths in HTML exist in downloaded_assets/")
