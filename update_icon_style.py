import os

directory = r"c:\Users\Maa\Deskmate services"

target = """<span style="font-size: 0.85em; opacity: 0.8;">Designed and developed by: <a href="https://www.linkedin.com/in/mahek-darji-521651303/" target="_blank" style="text-decoration: none; color: inherit;"><i class="fa-brands fa-linkedin" style="color: #0A66C2; font-size: 1.1em; margin-right: 2px;"></i> <span style="text-decoration: underline;">Mahek Darji</span></a></span>"""

replacement = """<span style="font-size: 0.9em; opacity: 0.9; font-weight: 600;">Designed & Developed by: <a href="https://www.linkedin.com/in/mahek-darji-521651303/" target="_blank" style="text-decoration: none; color: inherit;">Mahek Darji <i class="fa-brands fa-linkedin" style="font-size: 1.1em; margin-left: 4px;"></i></a></span>"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if target in content:
            new_content = content.replace(target, replacement)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Target not found in {filename}")

print("Done")
