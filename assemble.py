import build_css
import build_html
import build_js

css_content = build_css.get_css()
html_content = build_html.get_html()
js_content = build_js.get_js()

full_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="EasyRail — Simple Indian Railway ticket booking prototype for hackathon. No confusion, no jargon, just simple booking.">
  <title>EasyRail — Simple Indian Railway Ticket Booking</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
{css_content}
  </style>
</head>
<body>
{html_content}
  <script>
{js_content}
  </script>
</body>
</html>
"""

output_path = "/home/alumina/train/easyrail.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_document)

print(f"Successfully assembled {output_path}!")
