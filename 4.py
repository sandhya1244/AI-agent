import os
import re
from urllib.parse import urlparse, unquote

# Load CSS
with open("layla_combined.css", "r", encoding="utf-8") as f:
    css = f.read()

# Folder where assets were downloaded
asset_dir = "downloaded_assets"

# Find URLs in CSS
pattern = re.compile(r'url\((["\']?)(https?://[^)\'"]+\.(?:png|jpg|jpeg|gif|webp|ico|svg)[^)"\']*)\1\)')
matches = pattern.findall(css)

for _, url in matches:
    filename = os.path.basename(urlparse(unquote(url)).path)
    local_path = f"{asset_dir}/{filename}"
    css = css.replace(url, local_path)

# Save new CSS
with open("layla_combined_local.css", "w", encoding="utf-8") as f:
    f.write(css)

print("✅ Updated layla_combined_local.css with local asset paths")
