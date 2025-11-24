import datetime

PRODUCT_CATALOG = {
    'WST01': {'name': 'Basic Cotton T-Shirt', 'price': 899.00},
    'WST02': {'name': 'Casual Denim Shirt', 'price': 1500.00},
    'WST03': {'name': 'Business Formal Blouse', 'price': 1850.00},
    'WST04': {'name': 'Solid Color Sweater', 'price': 2500.00},
    'WST05': {'name': 'Graphic Print Hoodie', 'price': 3200.00},
    'WST06': {'name': 'V-Neck Knit Top', 'price': 1100.00},
    'WST07': {'name': 'Sleeveless Summer Vest', 'price': 750.00},
     # Ethnic stuff 
    'IND08': {'name': 'Embroidered Kurta (Women)', 'price': 1999.00},
    'IND09': {'name': 'Pathani Kurta (Men)', 'price': 1750.00},
    'IND10': {'name': 'Cotton Tunic Top', 'price': 1200.00},
    'IND11': {'name': 'Silk Blend Fusion Kurti', 'price': 2800.00},
    'IND12': {'name': 'Handloom Tunic', 'price': 2100.00},
    'IND13': {'name': 'Jaipuri Printed Kaftan', 'price': 1450.00},
    'IND14': {'name': 'Chikankari Kurta', 'price': 3500.00},
    # Bottom wear
    'WSP15': {'name': 'Classic Blue Jeans', 'price': 3800.00},
    'WSP16': {'name': 'Formal Chino Trousers', 'price': 2999.00},
    'WSP17': {'name': 'Athleisure Joggers', 'price': 1900.00},
    'WSP18': {'name': 'Denim Mini Skirt', 'price': 1400.00},
    'WSP19': {'name': 'Tailored Pencil Skirt', 'price': 2200.00},
    'WSP20': {'name': 'Linen Summer Shorts', 'price': 999.00},
    'WSP21': {'name': 'Stretchable Leggings', 'price': 700.00},

    'INB22': {'name': 'Palazzo Pants (Printed)', 'price': 1100.00},
    'INB23': {'name': 'Churidar Leggings', 'price': 650.00},
    'INB24': {'name': 'Patiala Salwar', 'price': 1300.00},
    'INB25': {'name': "Men's Dhoti", 'price': 900.00},
    'INB26': {'name': 'Plain Sharara', 'price': 1700.00},
    'INB27': {'name': 'Cotton Petticoat', 'price': 400.00},
    'INB28': {'name': 'Flowy Maxi Skirt (Ethnic)', 'price': 2300.00},
    # Coats / Outerwear
    'OUT29': {'name': 'Trench Coat (Western)', 'price': 7500.00},
    'OUT30': {'name': 'Quilted Puffer Jacket', 'price': 5200.00},
    'OUT31': {'name': 'Denim Trucker Jacket', 'price': 4100.00},
    'OUT32': {'name': 'Nehru Jacket (Wool Blend)', 'price': 4500.00},
    'OUT33': {'name': 'Formal Suit Blazer', 'price': 6800.00},
    'OUT34': {'name': 'Ethnic Embroidered Vest', 'price': 2900.00},
    'OUT35': {'name': 'Tussar Silk Stole', 'price': 3300.00},

    # Dresses (so many!)
    'DRS36': {'name': 'Little Black Dress (LBD)', 'price': 3999.00},
    'DRS37': {'name': 'Floral Sundress', 'price': 2100.00},
    'DRS38': {'name': 'Georgette Anarkali Suit', 'price': 6500.00},
    'DRS39': {'name': 'Heavy Work Lehenga Set', 'price': 18000.00},
    'DRS40': {'name': 'Simple Wrap Dress', 'price': 3100.00},
    'DRS41': {'name': 'Casual Salwar Kameez', 'price': 2400.00},
    'DRS42': {'name': 'Cocktail Maxi Dress', 'price': 4800.00},
    'DRS43': {'name': 'Silk Saree (Printed)', 'price': 5500.00},

    # Accessories
    'ACC44': {'name': 'Leather Belt (Western)', 'price': 1800.00},
    'ACC45': {'name': 'Woolen Winter Cap', 'price': 700.00},
    'ACC46': {'name': 'Designer Dupatta', 'price': 1600.00},
    'ACC47': {'name': 'Handbag (Clutch)', 'price': 2200.00},
    'ACC48': {'name': 'Tie and Pocket Square Set', 'price': 1300.00},
    'ACC49': {'name': 'Kolhapuri Sandals', 'price': 1900.00},
    'ACC50': {'name': 'Embroidered Potli Bag', 'price': 950.00},
}

#showing the catalog function
def show_catalog(cat_data):    
    print("## 🛒Available Product🛒  ##")
    print("Code | Price     | Item")
    print("-" * 55)

    for cd, details in cat_data.items():
        label = details['name']
        cost_print = f"₹{details['price']:,.2f}"
        print(f"{cd: <5}| {cost_print: <11}| {label}")

    print("-" * 55)
    print(f"Total items floating around here: {len(cat_data)}\n")
#total function
def compute_total(my_cart):
   
    running = 0
    for entry in my_cart:
        line = entry['price'] * entry['qty']
        running += line
    return running

#quantity function
def req_qty():
    while True:
        ask = input("Enter quantity (just a number): ").strip()

        try:
            qty_val = int(ask)
            if qty_val < 1:
                print("Uh… quantity must be more than zero.")
                continue
            return qty_val

        except Exception as oops:
           
            print("Not a valid integer. Try again.")

#add to cart function
def add_to_cart(cat, user_cart):
   
    prev_total = compute_total(user_cart)
    print(f"\nYour total so far: ₹{prev_total:,.2f}")

    prod_inp = input("Product code (or type BILL to finish): ").strip().upper()

    if prod_inp == "BILL":
        return False 

    if prod_inp in cat:
        thing = cat[prod_inp]

        print(f"Selected → {thing['name']} @ ₹{thing['price']:.2f}")

        q = req_qty()

        new_item = {
            'code': prod_inp,
            'name': thing['name'],  
            'price': thing['price'],
            'qty': q
        }
        user_cart.append(new_item)

        print(f"Added {q} x '{thing['name']}' to your basket!")

    else:
       
        print("Hmm… code not recognised. Maybe a typo?")

    return True

# Print final bill 
def make_receipt(cart_items, grand_total):
    print("\n" + "=" * 36)
    print("      🧾FINAL RECEIPT 🧾")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 36)

    print("QTY | Code | Item Name             | Unit Price | Total")
    print("-" * 36)

    for it in cart_items:
        line_total = it['price'] * it['qty']  
        print(f"{it['qty']: <3} | {it['code']: <4} | {it['name']: <21} | ₹{it['price']: <9.2f} | ₹{line_total:,.2f}")

    print("-" * 36)
    print(f"Amount Payable: ₹{grand_total:,.2f}")
    print("=" * 36)
    print()  

# Main routine

my_catalog_copy = PRODUCT_CATALOG  
show_catalog(my_catalog_copy)

live_cart = []
print("Starting checkout... (type BILL anytime)\n")

while True:
    keep_going = add_to_cart(my_catalog_copy, live_cart)
    if not keep_going:
        break


if not live_cart:
    print("Your cart is empty.")
else:
    total_cash = compute_total(live_cart)
    make_receipt(live_cart, total_cash)

print("\nThank you for shopping with us!❤️ Have a great day.")