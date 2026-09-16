import os

directory = r"c:\Users\Maa\Deskmate services"

target = """<div class="container footer-bottom">
            <p>&copy; 2024 DeskMate VA. All Rights Reserved.</p>"""

replacement = """<div class="container footer-bottom">
            <p>&copy; 2024 DeskMate VA. All Rights Reserved.<br><span style="font-size: 0.85em; opacity: 0.8; margin-top: 5px; display: inline-block;">Designed and developed by: <a href="https://www.linkedin.com/in/mahek-darji-521651303/" target="_blank" style="text-decoration: underline; color: inherit;">Mahek Darji</a></span></p>"""

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
