import requests
from urllib.parse import urljoin

# Base URL of the site
base_url = "https://layla.ai"

# List of CSS paths to download
css_paths = [
    "/_next/static/css/fef4deb4c8cf4f8e.css",
    "/_next/static/css/d8f9dc2416b9151d.css",
    "/_next/static/css/764dae88cab959a9.css",
    "/_next/static/css/1f05a9040d02c810.css"
]

# This will store the final combined CSS
combined_css = ""

for css_path in css_paths:
    full_url = urljoin(base_url, css_path)
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        css_content = response.text

        # Fix all relative URLs like /_next/static/media/... to absolute URLs
        css_content = css_content.replace('url(/', f'url({base_url}/')

        combined_css += f"/* ---- Source: {full_url} ---- */\n{css_content}\n\n"
        print(f"✅ Downloaded: {full_url}")
    except requests.RequestException as e:
        print(f"❌ Failed to download {full_url}: {e}")

# Write the combined CSS to a file
output_file = "layla_combined.css"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(combined_css)

print(f"\n🎉 Combined CSS saved to: {output_file}")
