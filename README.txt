HOOKED WITH LOVE — MULTI-PAGE SPLIT

Files included:
- index.html: original complete single-page app, retained for login, signup, product details, customize, cart, checkout, confirmation, tracking and profile.
- home.html: complete original Home section.
- about.html: complete original About Us section.
- shop.html: complete original Shop section.
- contact.html: complete original Contact Us & FAQ section.
- reviews.html: complete original Reviews section.
- styles.css: original inline CSS moved to a shared stylesheet, with navigation-link styles added.
- app.py: original PyScript interaction logic adapted so the five separated pages can navigate to each other and the remaining app sections.
- pyscript.toml: original PyScript config.
- gitignore.txt and README_original.md: supplied project files.

RUN IN VS CODE
1. Extract this ZIP into your website project folder.
2. Keep your original IMAGES folder in this same folder, with the same IMAGES/ filenames. The image paths in the HTML and app.py have not been renamed.
3. Open the extracted folder in VS Code.
4. In the VS Code terminal, run:
   python -m http.server 8000
5. Open http://localhost:8000 in your browser.

Do not open the HTML with file:// directly. PyScript needs the site served over HTTP and internet access to load its CDN files.

NOTES
- No separate JavaScript file existed in the uploaded website. The interactions are implemented in app.py using PyScript, so app.py stays in the same folder as the HTML files and pyscript.toml.
- The five separated sections' inner HTML was checked against the uploaded original; their content is unchanged.
- The original IMAGES folder was not included in the uploaded files, so it must be copied from your existing project into this folder.
