import os
import re

css_code = """
/* Dropdown Menu */
.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown .dropbtn {
    display: flex;
    align-items: center;
}

.dropdown-content {
    display: none;
    position: absolute;
    background-color: var(--bg-white);
    min-width: 250px;
    box-shadow: var(--shadow-lg);
    z-index: 1050;
    border-radius: 8px;
    overflow: hidden;
    top: 100%;
    left: 0;
    border: 1px solid var(--border-color);
}

.dropdown-content a {
    color: var(--text-color) !important;
    padding: 12px 16px !important;
    text-decoration: none;
    display: block;
    font-size: 0.9rem !important;
    transition: var(--transition);
    font-weight: 500 !important;
}

.dropdown-content a:hover {
    background-color: var(--bg-light) !important;
    color: var(--primary-color) !important;
    padding-left: 20px !important;
}

.dropdown:hover .dropdown-content {
    display: block;
}
"""

directory = r"c:\Users\Maa\Deskmate services"

# 1. Append CSS
css_path = os.path.join(directory, "styles", "main.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if "/* Dropdown Menu */" not in css_content:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(css_code)

# 2. Update HTML files
dropdown_html_normal = """<div class="dropdown">
                    <a href="services.html" class="dropbtn">Services <i class="fa-solid fa-chevron-down" style="font-size: 0.8em; margin-left: 4px;"></i></a>
                    <div class="dropdown-content">
                        <a href="admin-support.html">Admin Support</a>
                        <a href="accounting-support.html">Accounting Support</a>
                        <a href="ecommerce-support.html">E-commerce Support</a>
                        <a href="digital-marketing.html">Digital Marketing</a>
                        <a href="web-design.html">Web Design & Maintenance</a>
                        <a href="it-services.html">IT / Web Services</a>
                        <a href="export-support.html">Export Support <span style="background-color: var(--green-color); color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.65rem; margin-left: 5px; font-weight: bold;">NEW</span></a>
                    </div>
                </div>"""

dropdown_html_active = dropdown_html_normal.replace('class="dropbtn"', 'class="dropbtn active"')

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We also have to handle footer links, wait!
        # The footer also has <a href="services.html">Services</a>
        # We ONLY want to replace the one in <nav class="nav-links">!
        
        # Find the nav block
        nav_pattern = re.compile(r'(<nav class="nav-links">.*?)(<a href="services\.html"(?: class="active")?>Services</a>)(.*?</nav>)', re.DOTALL)
        
        def nav_replacer(match):
            prefix = match.group(1)
            target = match.group(2)
            suffix = match.group(3)
            
            if 'class="active"' in target:
                replacement = dropdown_html_active
            else:
                replacement = dropdown_html_normal
                
            return prefix + replacement + suffix
            
        new_content = nav_pattern.sub(nav_replacer, content)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")

print("Done")
