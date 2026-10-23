
# Hooked with Love — complete PyScript website logic
from js import document, window, localStorage, FileReader, confirm, Date
from pyodide.ffi import create_proxy
import json, re, html, hashlib

PRODUCTS = [
    {"id":1,"code":"H1","name":"Dark Bat Hero Keychain","price":99,"category":"Crochet Keychains","image":"IMAGES/H1_warm_bg.png","art":"🦇","desc":"Black crochet bat-hero with glowing yellow eyes and a dangling keyring."},
    {"id":2,"code":"H2","name":"Cloud Cupcake Keychain","price":60,"category":"Crochet Keychains","image":"IMAGES/H2_warm_bg.png","art":"🧁","desc":"White crochet cupcake with a blue wrapper, blushing cheeks and a sweet face."},
    {"id":3,"code":"H3","name":"Crochet Bottle Holder","price":199,"category":"Personalized Gifts","image":"IMAGES/H3_warm_bg.png","art":"🧶","desc":"Black mesh sleeve with a carry handle for water bottles. Colors can be customized."},
    {"id":4,"code":"H4","name":"Fluffy Sheep Keychain","price":99,"category":"Crochet Keychains","image":"IMAGES/H4_warm_bg.png","art":"🐑","desc":"Round white lamb with a curly wool top, pink ears and a little yellow sling bag."},
    {"id":5,"code":"H5","name":"Green Power Girl Doll Keychain","price":180,"category":"Crochet Keychains","image":"IMAGES/H5_warm_bg.png","art":"👧","desc":"Doll with a black bob, big green felt eyes, and a green and black striped dress."},
    {"id":6,"code":"H6","name":"Custom Doll Keychain","price":250,"category":"Personalized Gifts","image":"IMAGES/H6_warm_bg.png","art":"🪆","desc":"Made-to-order doll with your choice of hair, outfit and glasses."},
    {"id":7,"code":"H7","name":"Hanging Web Hero Keychain","price":99,"category":"Crochet Keychains","image":"IMAGES/H7_warm_bg.png","art":"🕸️","desc":"Spider-themed hero hanging upside down from a white crochet cord, with a felt mask."},
    {"id":8,"code":"H8","name":"Mini Octopus Keychain","price":50,"category":"Crochet Keychains","image":"IMAGES/H8_warm_bg.png","art":"🐙","desc":"Pastel octopus with an embroidered sleepy face. Available in blue, purple, pink or yellow."},
    {"id":9,"code":"H9","name":"Rose Ruffle Charm","price":60,"category":"Crochet Flowers","image":"IMAGES/H9_warm_bg.png","art":"🌹","desc":"Soft bell-shaped charm with crochet roses, green leaves and ruffled white trim. Available in pink, blue and purple."},
    {"id":10,"code":"H10","name":"Square Sponge Buddy Keychain","price":180,"category":"Crochet Keychains","image":"IMAGES/H10_warm_bg.png","art":"🟨","desc":"Yellow square character with felt eyes, long legs, a red tie and brown shorts."},
    {"id":11,"code":"H11","name":"Candy Jellyfish Keychain","price":99,"category":"Crochet Keychains","image":"IMAGES/H11_warm_bg.png","art":"🪼","desc":"Red and white jellyfish with a ruffled bell and long twisting tentacles."},
    {"id":12,"code":"H12","name":"Little Chick Keychain","price":50,"category":"Crochet Keychains","image":"IMAGES/H12_warm_bg.png","art":"🐥","desc":"Blue and yellow chick with a black bead eye and optional pearl and crystal charm."},
    {"id":13,"code":"H13","name":"Bunny Pair Keychains","price":60,"category":"Crochet Keychains","image":"IMAGES/H13_warm_bg.png","art":"🐰","desc":"White bunnies with a blue headband or pink hood, bead eyes and blush."},
    {"id":14,"code":"H14","name":"Purple Ghost Monster Keychain","price":99,"category":"Crochet Keychains","image":"IMAGES/H14_warm_bg.png","art":"👻","desc":"Grinning purple monster with red felt eyes, a spiky head and arms, and a white felt smile."},
    {"id":15,"code":"H15","name":"Pink Tulip and Lily Bouquet","price":450,"category":"Fuzzy Crafts","image":"IMAGES/H15_warm_bg.png","art":"💐","desc":"Pipe-cleaner pink tulips and a large lily in cream wrapping with gold edges and a pink ribbon."},
    {"id":16,"code":"H16","name":"Sunflower Pot Arrangement","price":400,"category":"Fuzzy Crafts","image":"IMAGES/H16_warm_bg.png","art":"🌻","desc":"Fuzzy sunflowers, daisies and buds in a brown chenille pot."},
    {"id":17,"code":"H17","name":"Purple Lily Bouquet","price":550,"category":"Fuzzy Crafts","image":"IMAGES/H17_warm_bg.png","art":"💐","desc":"Violet pipe-cleaner lilies and small daisies in lavender wrap with an organza bow."},
    {"id":18,"code":"H18","name":"Pink Lily Bouquet","price":550,"category":"Fuzzy Crafts","image":"IMAGES/H18_warm_bg.png","art":"🌸","desc":"Pink lilies, daisies and green leaves in pink wrap with satin and organza ribbons."},
    {"id":19,"code":"H19","name":"Rainbow Crystal Bracelet","price":89,"category":"Personalized Gifts","image":"IMAGES/H19_warm_bg.png","art":"📿","desc":"Stretch bracelet of multicolor faceted crystals with rhinestone spacers."},
    {"id":20,"code":"H20","name":"Lavender Bow Pearl Bracelet","price":99,"category":"Personalized Gifts","image":"IMAGES/H20_warm_bg.png","art":"🎀","desc":"Lavender and pearl beads with rhinestone spacers and a bow charm."},
    {"id":21,"code":"H21","name":"Lavender Bow Pearl Bracelet","price":99,"category":"Personalized Gifts","image":"IMAGES/H21_warm_bg.png","art":"🎀","desc":"Lavender and pearl beads with rhinestone spacers and a bow charm."},
    {"id":22,"code":"H22","name":"Pink Heart Charm Bracelet","price":89,"category":"Personalized Gifts","image":"IMAGES/H22_warm_bg.png","art":"💗","desc":"Pink crackle glass, pearls and a flower bead with a silver heart charm."},
    {"id":23,"code":"H23","name":"Green Garden Bracelet","price":89,"category":"Personalized Gifts","image":"IMAGES/H23_warm_bg.png","art":"🍀","desc":"Mint crackle beads, pearls, a flower bead and a star bead."},
    {"id":24,"code":"H24","name":"Fuzzy Daisy Keychain","price":60,"category":"Fuzzy Crafts","image":"IMAGES/H24_warm_bg.png","art":"🌼","desc":"Round pipe-cleaner gerbera flower in assorted pastel colors, each with a gold keyring."},
    {"id":25,"code":"H25","name":"Class of 2026 Graduation Ribbon Pin","price":120,"category":"Personalized Gifts","image":"IMAGES/H25_warm_bg.png","art":"🎓","desc":"Fuzzy flower rosette with a Congratulations badge, satin ribbons and leaf accents."}
]

CATS = ["All Products","Crochet Keychains","Crochet Flowers","Fuzzy Crafts","Personalized Gifts"]
cart, reviews, user, order = [], [], None, None
category, product, quantity, stars, pending = "All Products", PRODUCTS[2], 1, 0, None
_proxies = []

def E(i):
    return document.getElementById(i)

def Q(s):
    return document.querySelector(s)

def QA(s):
    return document.querySelectorAll(s)

def V(i):
    el = E(i)
    return el.value if el else ""

def esc(s):
    return html.escape(str(s or ""), quote=True)

def money(n):
    return "₱" + format(int(n), ",")

def load(k, default=None):
    try:
        value = localStorage.getItem("hw_" + k)
        return json.loads(value) if value is not None else default
    except Exception:
        return default

def save(k, value):
    try:
        localStorage.setItem("hw_" + k, json.dumps(value))
    except Exception:
        pass

def notify(message):
    toast = E("toast")
    if not toast:
        return
    toast.textContent = message
    toast.classList.add("show")
    def hide():
        toast.classList.remove("show")
    proxy = create_proxy(hide)
    _proxies.append(proxy)
    window.setTimeout(proxy, 2800)

def logged():
    return bool(user)

def update_auth_header():
    """Show optional sign-in controls until authenticated, then greet the user."""
    control = E("authHeaderControl")
    if not control:
        return
    if logged():
        name = esc(user.get("name", "there"))
        control.innerHTML = (
            f'<button type="button" class="auth-greeting" '
            f'data-page="profile" aria-label="Open profile">Hi! {name}</button>'
        )
    else:
        control.innerHTML = (
            '<button type="button" class="auth-header-btn" data-page="login">Log In</button> '
            '<button type="button" class="auth-header-btn primary" data-page="signup">Sign Up</button>'
        )

def page(p):
    global pending
    if p in ("profile", "cart", "checkout", "customize") and not logged():
        pending = "page:" + p
        save("pending", pending)
        p = "login"
        notify("Please log in or sign up to continue.")

    # The five main sections now have their own HTML files. Other app sections
    # remain in index.html so the existing login/cart/checkout/profile flow works.
    if not E(p):
        main_pages = {
            "home": "home.html",
            "about": "about.html",
            "shop": "shop.html",
            "contact": "contact.html",
            "reviews": "reviews.html",
        }
        if p in main_pages:
            window.location.href = main_pages[p]
        else:
            window.location.href = "index.html#" + p
        return

    for section in QA(".page"):
        section.classList.toggle("active", section.id == p)

    # FIX: keep all main navigation buttons active and clickable.
    for nav_button in QA("nav [data-page]"):
        nav_button.classList.toggle(
            "active", nav_button.getAttribute("data-page") == p
        )
    main_links = {
        "home": "home.html",
        "about": "about.html",
        "shop": "shop.html",
        "contact": "contact.html",
        "reviews": "reviews.html",
    }
    for nav_link in QA("nav a"):
        nav_link.classList.toggle("active", main_links.get(p) == nav_link.getAttribute("href"))

    update_auth_header()
    for icon_button in QA(".header-actions > .icon-btn"):
        icon_button.style.display = "" if logged() else "none"

    if p == "shop":
        products()
    elif p == "cart":
        render_cart()
    elif p == "checkout":
        render_checkout()
    elif p == "profile":
        render_profile()
    elif p == "reviews":
        render_reviews()

    window.scrollTo(0, 0)

def after_auth():
    global pending
    destination = pending or load("pending")
    pending = None
    save("pending", None)

    if destination and destination.startswith("add:"):
        page("shop")
        notify("Please choose Add to Cart again after logging in.")
    elif destination and destination.startswith("page:"):
        page(destination.split(":", 1)[1])
    elif destination == "checkout":
        page("checkout")
    elif destination == "cart":
        page("cart")
    elif destination == "profile":
        page("profile")
    else:
        page("shop")

def image_markup(p, img_class="", placeholder_class="image-placeholder"):
    code = esc(p.get("code", "CUSTOM"))
    name = esc(p.get("name", "Product photo"))
    art = esc(p.get("art", "🎁"))
    image = p.get("image", "")
    cls = f' class="{esc(img_class)}"' if img_class else ""

    placeholder = (
        f'<div class="{esc(placeholder_class)}" style="display:grid">'
        f'<span class="placeholder-plus">{art}</span>'
        f'<span>Add Product Photo</span><small>{code}</small></div>'
    )
    if not image:
        return placeholder

    return (
        f'<img{cls} src="{esc(image)}" alt="{name}" '
        f'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'grid\'">'
        + placeholder.replace('style="display:grid"', 'style="display:none"')
    )

def card(p):
    return (
        f'<article class="product">'
        f'<div class="product-art">{image_markup(p)}</div>'
        f'<div class="product-body"><h3>{esc(p["name"])}</h3>'
        f'<p>{esc(p["category"])}</p><div class="product-foot">'
        f'<span class="price">{money(p["price"])}</span>'
        f'<button class="btn btn-primary btn-small" data-act="open:{p["id"]}">View Details</button>'
        f'</div></div></article>'
    )

def featured():
    if E("featuredGrid"):
        E("featuredGrid").innerHTML = "".join(card(p) for p in PRODUCTS[:4])
    if E("relatedGrid"):
        E("relatedGrid").innerHTML = "".join(
            card(p) for p in [x for x in PRODUCTS if x["id"] != product["id"]][:3]
        )

def filters():
    if not E("filters"):
        return
    E("filters").innerHTML = "".join(
        f'<button class="chip {"active" if category == c else ""}" data-act="cat:{esc(c)}">{esc(c)}</button>'
        for c in CATS
    )

def products():
    filters()
    q = V("searchInput").lower()
    found = [
        p for p in PRODUCTS
        if (category == "All Products" or p["category"] == category)
        and q in p["name"].lower()
    ]
    sort_by = V("sortSelect")
    if sort_by == "low":
        found.sort(key=lambda x: x["price"])
    elif sort_by == "high":
        found.sort(key=lambda x: x["price"], reverse=True)
    elif sort_by == "name":
        found.sort(key=lambda x: x["name"].lower())

    if E("shopGrid"):
        E("shopGrid").innerHTML = "".join(card(p) for p in found)
    if E("noResults"):
        E("noResults").classList.toggle("hidden", bool(found))

def setcat(c):
    global category
    category = c
    products()

def open_product(i):
    global product, quantity
    product = next((p for p in PRODUCTS if p["id"] == int(i)), PRODUCTS[0])
    quantity = 1
    save("current_product", product["id"])
    # Product details are one of the remaining app sections in index.html.
    if not E("detailName"):
        window.location.href = "index.html#product"
        return
    E("detailName").textContent = product["name"]
    E("detailPrice").textContent = money(product["price"])
    E("detailDesc").textContent = product["desc"]
    E("detailArt").innerHTML = image_markup(product)
    E("detailQty").textContent = "1"
    featured()
    page("product")

def count():
    if E("cartCount"):
        E("cartCount").textContent = str(sum(x["qty"] for x in cart))
    save("cart", cart)

def add_cart(auth=False):
    global pending
    if not auth and not logged():
        pending = None
        page("login")
        notify("Please log in or create an account first to add items to your cart.")
        return

    found = next(
        (x for x in cart if x.get("id") == product["id"] and not x.get("custom")),
        None
    )
    if found:
        found["qty"] += quantity
    else:
        cart.append({
            **product, "qty": quantity, "custom": False,
            "options": "", "selected": True
        })
    count()
    notify("Added to cart successfully!")
    page("cart")

def add_custom(auth=False):
    global pending
    if not auth and not logged():
        pending = None
        page("login")
        notify("Please log in or create an account first to add a customized gift.")
        return

    q = max(1, min(20, int(float(V("customQty") or 1))))
    opts = " · ".join(
        x for x in [V("customColor"), V("customDesign"), V("customName").strip()] if x
    )
    cart.append({
        "id": 99, "code": "CUSTOM", "name": "Customized Crochet Gift",
        "price": 169, "category": "Personalized Gifts", "image": "",
        "art": "🎁", "qty": q, "custom": True, "options": opts, "selected": True
    })
    count()
    notify("Customized item added to cart!")
    page("cart")

def total(items):
    return sum(x["price"] * x["qty"] for x in items)

def render_cart():
    chosen = [x for x in cart if x.get("selected", True)]
    if not cart:
        E("cartContent").innerHTML = (
            '<div class="empty"><div class="empty-icon">🧺</div>'
            '<h3>Your cart is waiting for something lovely.</h3>'
            '<p>Explore our handmade collection and find a little something special.</p>'
            '<button class="btn btn-primary" data-act="page:shop">Continue Shopping</button></div>'
        )
        return

    rows = ""
    for i, item in enumerate(cart):
        checked = "checked" if item.get("selected", True) else ""
        rows += (
            f'<div class="cart-row">'
            f'<label class="cart-select"><input type="checkbox" data-chg="select:{i}" {checked}>'
            f'<div class="mini-art">{image_markup(item, "mini-art-photo", "mini-art-fallback")}</div></label>'
            f'<div><strong>{esc(item["name"])}</strong>'
            f'<div class="subtle">{esc(item.get("options") or item["category"])}</div>'
            f'<div class="price">{money(item["price"])} each</div></div>'
            f'<div class="qty"><button data-act="qty:{i}:-1">−</button>'
            f'<span>{item["qty"]}</span><button data-act="qty:{i}:1">+</button></div>'
            f'<strong class="line-total">{money(item["price"] * item["qty"])}</strong>'
            f'<button class="text-link" data-act="remove:{i}">Remove</button></div>'
        )

    subtotal = total(chosen)
    E("cartContent").innerHTML = (
        f'<div class="cart-layout"><div class="panel">'
        f'<h3>Cart Items ({sum(x["qty"] for x in cart)})</h3>'
        f'<p class="subtle">Select the items you want to check out. Unselected items stay in your cart.</p>{rows}</div>'
        f'<div class="summary"><h3>Selected Order Summary</h3>'
        f'<div class="summary-line"><span>Selected items</span><strong>{sum(x["qty"] for x in chosen)}</strong></div>'
        f'<div class="summary-line"><span>Subtotal</span><strong>{money(subtotal)}</strong></div>'
        f'<div class="summary-line"><span>Estimated Delivery Fee</span><strong>{"₱50" if chosen else "₱0"}</strong></div>'
        f'<div class="summary-line total"><span>Estimated Total</span><strong>{money(subtotal + (50 if chosen else 0))}</strong></div>'
        f'<button class="btn btn-primary wide" data-act="checkout" {"disabled" if not chosen else ""}>Proceed to Checkout ({len(chosen)})</button>'
        f'<button class="btn btn-secondary wide mt" data-act="page:shop">Continue Shopping</button></div></div>'
    )

def render_checkout():
    chosen = [x for x in cart if x.get("selected", True)]
    subtotal = total(chosen)
    lines = []
    for item in chosen:
        lines.append(
            f'<div class="checkout-product-line">'
            f'<div class="checkout-product-photo">{image_markup(item, "checkout-photo", "checkout-photo-fallback")}</div>'
            f'<span>{esc(item["name"])} × {item["qty"]}</span>'
            f'<strong>{money(item["price"] * item["qty"])}</strong></div>'
        )
    E("checkoutItems").innerHTML = "".join(lines) or "<p>No items selected. Return to your cart and select items.</p>"
    E("checkoutSubtotal").textContent = money(subtotal)
    E("checkoutTotal").textContent = money(subtotal + (50 if chosen else 0))

def submit_order(ev):
    global order, cart
    ev.preventDefault()
    if not logged():
        page("login")
        return
    if not E("checkoutForm").checkValidity():
        E("checkoutForm").reportValidity()
        return

    chosen = [x.copy() for x in cart if x.get("selected", True)]
    if not chosen:
        notify("Select at least one cart item.")
        page("cart")
        return

    order = {
        "ref": "HL-" + str(int(Date.new().getTime()))[-6:],
        "items": chosen, "total": total(chosen) + 50,
        "name": V("fullName"), "email": V("email"),
        "date": str(Date.new().toLocaleDateString())
    }
    save("order", order)
    E("orderRef").textContent = order["ref"]
    E("confirmationItems").innerHTML = "".join(
        f'<div class="checkout-product-line"><div class="checkout-product-photo">{image_markup(item, "checkout-photo", "checkout-photo-fallback")}</div>'
        f'<span>{esc(item["name"])} × {item["qty"]}</span><strong>{money(item["price"] * item["qty"])}</strong></div>'
        for item in chosen
    ) + '<div class="summary-line"><span>Delivery fee (estimate)</span><strong>₱50</strong></div>'
    E("confirmationTotal").textContent = money(order["total"])
    E("confirmationCustomer").textContent = "Order for " + order["name"] + " · " + order["email"]
    cart = [x for x in cart if not x.get("selected", True)]
    count()
    E("checkoutForm").reset()
    page("confirmation")

def render_reviews():
    if not E("ratingSummary"):
        return
    if not reviews:
        E("ratingSummary").innerHTML = (
            '<div class="empty"><div class="empty-icon">♡</div>'
            '<h3>No reviews yet</h3><p>Be the first to share your feedback.</p></div>'
        )
        E("reviewList").innerHTML = ""
        return

    avg = sum(r["stars"] for r in reviews) / len(reviews)
    E("ratingSummary").innerHTML = (
        f'<div class="stars">{"★" * round(avg)}{"☆" * (5-round(avg))}</div>'
        f'<h2>{avg:.1f} / 5</h2><p>{len(reviews)} customer review(s)</p>'
    )
    E("reviewList").innerHTML = "".join(
        f'<article class="panel mb"><div class="stars">{"★"*r["stars"]}{"☆"*(5-r["stars"])}</div>'
        f'<h3>{esc(r["title"])}</h3><p>{esc(r["comment"])}</p>'
        f'<div class="subtle">{esc(r["name"])} · {esc(r["date"])}</div></article>'
        for r in reversed(reviews)
    )

def render_profile():
    if not user:
        return
    name = user.get("name", "")
    email = user.get("email", "")
    phone = user.get("phone", "")
    if E("profileName"):
        E("profileName").value = name
    if E("profileEmail"):
        E("profileEmail").value = email
    if E("profilePhone"):
        E("profilePhone").value = phone
    if E("profileDisplayName"):
        E("profileDisplayName").textContent = name or "Your Name"
    if E("profileDisplayEmail"):
        E("profileDisplayEmail").textContent = email or "your@email.com"
    avatar = load("avatar")
    if avatar and E("profileAvatar"):
        E("profileAvatar").src = avatar
    render_orders()

def render_orders():
    global order
    order = order or load("order")
    if not E("profileOrderTable"):
        return
    if not order:
        E("profileOrderTable").innerHTML = "<p>No orders yet. Place an order to see it here.</p>"
        return
    E("profileOrderTable").innerHTML = (
        f'<table><thead><tr><th>Order Reference</th><th>Date</th><th>Total</th><th>Status</th><th>Action</th></tr></thead>'
        f'<tbody><tr><td>{esc(order["ref"])}</td><td>{esc(order.get("date",""))}</td>'
        f'<td>{money(order["total"])}</td><td><span class="pill">Received</span></td>'
        f'<td><button class="btn btn-secondary btn-small" data-act="tracklast">View Details</button></td></tr></tbody></table>'
    )

def stars_set(n):
    global stars
    stars = int(n)
    for button in QA("#starPicker button"):
        button.textContent = "★" if int(button.getAttribute("data-star")) <= stars else "☆"

def change_photo(ev):
    file = ev.target.files.item(0)
    if not file:
        return
    reader = FileReader.new()
    def done(_):
        E("profileAvatar").src = reader.result
        save("avatar", str(reader.result))
        notify("Profile picture saved in this browser.")
    proxy = create_proxy(done)
    _proxies.append(proxy)
    reader.onload = proxy
    reader.readAsDataURL(file)

def click(ev):
    global user, pending, quantity, product
    node = ev.target.closest("[data-act], [data-click], [data-page], [data-onclick], [data-faq]")
    if not node:
        return

    # FIX: all four main navigation links now work.
    nav_page = node.getAttribute("data-page")
    if nav_page:
        page(nav_page)
        return

    action = node.getAttribute("data-act") or node.getAttribute("data-click") or ""

    if not action:
        raw = node.getAttribute("data-onclick") or ""
        match = re.search(r"showPage\('([^']+)'\)", raw)
        if match:
            action = "page:" + match.group(1)
        elif "demoLogout" in raw:
            action = "logout"
        elif "addToCart" in raw:
            action = "add"
        elif "addCustomToCart" in raw:
            action = "custom"
        elif "resetShop" in raw:
            action = "reset"
        elif "selectSwatch" in raw:
            action = "swatch"
        elif "Profile changes" in raw:
            action = "saveProfile"
        elif "Account settings" in raw:
            action = "saveSettings"
        else:
            patterns = [
                (r"filterCategory\('([^']+)'\)", "cat:"),
                (r"openProduct\((\d+)\)", "open:"),
                (r"changeDetailQty\((-?\d+)\)", "detailqty:"),
                (r"setStars\((\d+)\)", "stars:"),
                (r"profileTab\('([^']+)'", "tab:"),
                (r"togglePassword\('([^']+)'", "password:")
            ]
            for pattern, prefix in patterns:
                match = re.search(pattern, raw)
                if match:
                    action = prefix + match.group(1)
                    break

    faq_id = node.getAttribute("data-faq")
    if faq_id:
        item = node.closest(".faq-item")
        if item:
            expanded = item.getAttribute("aria-expanded") == "true"
            item.setAttribute("aria-expanded", "false" if expanded else "true")
            node.setAttribute("aria-expanded", "false" if expanded else "true")
            mark = node.querySelector(".faq-mark")
            if mark:
                mark.textContent = "+" if expanded else "−"
        return

    if action.startswith("page:"):
        page(action.split(":", 1)[1])
    elif action.startswith("cat:"):
        setcat(action.split(":", 1)[1])
    elif action.startswith("open:"):
        open_product(action.split(":")[1])
    elif action in ("add", "addToCart"):
        add_cart()
    elif action in ("custom", "addCustomToCart"):
        add_custom()
    elif action in ("reset", "resetShop"):
        E("searchInput").value = ""
        setcat("All Products")
    elif action == "saveProfile":
        if user:
            name = V("profileName").strip()
            email = V("profileEmail").strip().lower()
            phone = V("profilePhone").strip()
            if not name or not email:
                notify("Please enter your name and email address.")
                return
            old_email = user.get("email", "").strip().lower()
            user["name"] = name
            user["email"] = email
            user["phone"] = phone
            save("user", user)
            # Keep the saved account record in sync with the current profile.
            if old_email:
                account = load("account_" + old_email, {}) or {}
                account["name"] = name
                account["email"] = email
                account["phone"] = phone
                if email != old_email:
                    save("account_" + old_email, None)
                save("account_" + email, account)
            update_auth_header()
            render_profile()
            notify("Profile information updated successfully.")
    elif action == "saveSettings":
        notify("Preferences saved in this browser.")
    elif action in ("swatch", "selectSwatch"):
        for item in QA(".swatch"):
            item.classList.remove("selected")
        node.classList.add("selected")
    elif action.startswith("detailqty:"):
        quantity = max(1, min(20, quantity + int(action.split(":")[1])))
        E("detailQty").textContent = str(quantity)
    elif action.startswith("stars:"):
        stars_set(action.split(":")[1])
    elif action.startswith("qty:"):
        _, index, amount = action.split(":")
        cart[int(index)]["qty"] = max(1, min(20, cart[int(index)]["qty"] + int(amount)))
        count()
        render_cart()
    elif action.startswith("remove:"):
        if confirm("Remove this item from your cart?"):
            cart.pop(int(action.split(":")[1]))
            count()
            render_cart()
    elif action == "checkout":
        if logged():
            page("checkout")
        else:
            pending = "checkout"
            page("login")
    elif action == "logout":
        user = None
        save("user", None)
        notify("You have logged out.")
        page("home")
    elif action.startswith("tab:"):
        tab_id = action.split(":", 1)[1]
        for tab in QA(".profile-tab"):
            tab.classList.toggle("hidden", tab.id != tab_id)
        for button in QA(".side-menu button"):
            button.classList.remove("active")
        node.classList.add("active")
    elif action.startswith("password:"):
        inp = E(action.split(":", 1)[1])
        if inp:
            show = inp.type == "password"
            inp.type = "text" if show else "password"
            node.textContent = "Hide" if show else "Show"
    elif action == "tracklast" and order:
        E("trackRef").value = order["ref"]
        E("trackDisplay").textContent = order["ref"]
        page("tracking")

def submit(ev):
    global user, pending, stars, reviews, order, cart
    form = ev.target
    raw = form.getAttribute("data-onsubmit") or form.getAttribute("data-submit") or ""
    if not raw:
        return
    ev.preventDefault()

    if "demoLogin" in raw or raw == "login":
        email = V("loginEmail").strip().lower()
        account = load("account_" + email)
        if not account:
            notify("No account found for this email. Please sign up first.")
            return
        password_hash = hashlib.sha256(V("loginPassword").encode()).hexdigest()
        if account.get("password_hash") != password_hash:
            notify("Incorrect email or password.")
            return
        user = {"name": account["name"], "email": email, "phone": account.get("phone", "")}
        save("user", user)
        notify("Login successful.")
        after_auth()

    elif "demoSignup" in raw or raw == "signup":
        if V("registerPassword") != V("registerConfirm"):
            notify("Passwords do not match.")
            return
        email = V("registerEmail").strip().lower()
        if load("account_" + email):
            notify("Account already exists. Please log in.")
            return
        name = V("registerName").strip() or "Customer"
        password_hash = hashlib.sha256(V("registerPassword").encode()).hexdigest()
        save("account_" + email, {"name": name, "email": email, "phone": "", "password_hash": password_hash})
        user = {"name": name, "email": email, "phone": ""}
        save("user", user)
        notify("Account created.")
        after_auth()

    elif "submitOrder" in raw or raw == "checkout":
        submit_order(ev)

    elif "submitReview" in raw or raw == "review":
        if not stars:
            notify("Please choose a star rating first.")
            return
        reviews.append({
            "stars": stars, "title": V("reviewTitle"),
            "comment": V("reviewComment"), "name": V("reviewName"),
            "product": V("reviewProduct"),
            "date": str(Date.new().toLocaleDateString())
        })
        save("reviews", reviews)
        form.reset()
        stars_set(0)
        render_reviews()
        notify("Thank you for your feedback.")

    elif "trackOrder" in raw or raw == "track":
        ref = V("trackRef").strip()
        if order and ref.lower() == order["ref"].lower():
            E("trackDisplay").textContent = ref.upper()
            E("trackingResult").classList.remove("hidden")
            notify("Order found.")
        else:
            notify("Order not found. Check the reference.")

def input_(ev):
    raw = ev.target.getAttribute("data-oninput") or ev.target.getAttribute("data-input") or ""
    if "renderProducts" in raw:
        products()
    elif "updateCustomTotal" in raw:
        q = max(1, min(20, int(float(V("customQty") or 1))))
        E("customQtyLabel").textContent = str(q)
        E("customTotal").textContent = money(169 * q)

def change(ev):
    raw = ev.target.getAttribute("data-onchange") or ev.target.getAttribute("data-chg") or ""
    if "changeProfilePhoto" in raw:
        change_photo(ev)
    elif raw.startswith("select:"):
        cart[int(raw.split(":")[1])]["selected"] = bool(ev.target.checked)
        save("cart", cart)
        render_cart()

def init():
    global cart, user, reviews, order, product, pending

    cart = load("cart", []) or []
    user = load("user")
    reviews = load("reviews", []) or []
    order = load("order")
    pending = load("pending")
    saved_product_id = load("current_product")
    if saved_product_id is not None:
        product = next((p for p in PRODUCTS if p["id"] == int(saved_product_id)), product)

    # Keep saved cart items compatible with the current H1-H25 catalog.
    valid_codes = {p["code"] for p in PRODUCTS}
    updated_cart = []
    for item in cart:
        if item.get("custom"):
            updated_cart.append(item)
        elif item.get("code") in valid_codes:
            current = next((p for p in PRODUCTS if p["code"] == item.get("code")), None)
            if current:
                updated_cart.append({
                    **current,
                    "qty": item.get("qty", 1),
                    "custom": False,
                    "options": item.get("options", ""),
                    "selected": item.get("selected", True)
                })
    cart = updated_cart
    save("cart", cart)

    # Convert form handlers to Python/PyScript event actions.
    for node in QA("[data-onsubmit]"):
        raw = node.getAttribute("data-onsubmit") or ""
        if "demoLogin" in raw:
            node.setAttribute("data-submit", "login")
        elif "demoSignup" in raw:
            node.setAttribute("data-submit", "signup")
        elif "submitOrder" in raw:
            node.setAttribute("data-submit", "checkout")
        elif "submitReview" in raw:
            node.setAttribute("data-submit", "review")
        elif "trackOrder" in raw:
            node.setAttribute("data-submit", "track")

    for node in QA("[data-oninput]"):
        raw = node.getAttribute("data-oninput") or ""
        if "renderProducts" in raw:
            node.setAttribute("data-input", "renderProducts")
        elif "updateCustomTotal" in raw:
            node.setAttribute("data-input", "updateCustomTotal")

    for node in QA("[data-onchange]"):
        raw = node.getAttribute("data-onchange") or ""
        if "changeProfilePhoto" in raw:
            node.setAttribute("data-chg", "changeProfilePhoto")

    # Populate the review product dropdown.
    if E("reviewProduct"):
        for p in PRODUCTS:
            option = document.createElement("option")
            option.value = p["name"]
            option.textContent = p["name"]
            E("reviewProduct").appendChild(option)

    # Bind one delegated listener. It also handles dynamically created product buttons.
    for event_name, handler in [
        ("click", click),
        ("submit", submit),
        ("input", input_),
        ("change", change)
    ]:
        proxy = create_proxy(handler)
        _proxies.append(proxy)
        document.addEventListener(event_name, proxy)

    featured()
    products()
    render_reviews()
    count()
    update_auth_header()

    # Support direct links such as index.html#cart or index.html#login.
    requested_page = str(window.location.hash or "").lstrip("#")
    if requested_page == "product":
        open_product(product["id"])
    elif requested_page and E(requested_page):
        page(requested_page)

    if user:
        for button in QA(".header-actions > .icon-btn"):
            button.style.display = ""
        render_profile()
    else:
        for button in QA(".header-actions > .icon-btn"):
            button.style.display = "none"

    # Keep the promotional video section available on the Home Page.
    if E("promoVideo"):
        E("promoVideo").src = "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"

init()
