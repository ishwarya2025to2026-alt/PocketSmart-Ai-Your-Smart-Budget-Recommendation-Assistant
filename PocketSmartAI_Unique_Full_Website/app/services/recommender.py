from math import floor

def money(v): return f"₹{v:,.0f}"

def generate_recommendation(kind, d):
    budget=float(d["budget"])
    if kind=="home":
        allocations=[("Furniture",.38),("Lighting",.18),("Decor",.20),("Utility",.14),("Buffer",.10)]
        products=[
            ("Compact furniture set","Amazon / IKEA",.32,"Clean lines, space-saving and easy to style."),
            ("Warm LED lighting kit","Amazon",.14,"Layered lighting for a comfortable room."),
            ("Wall art + soft decor","IKEA / Flipkart",.16,"Adds personality without taking over the room."),
            ("Storage organizer set","IKEA / Amazon",.12,"Practical storage for everyday clutter."),
        ]
        title=f"{d['room']} · {d['style']} plan"
    elif kind=="party":
        allocations=[("Food & catering",.45),("Decoration",.18),("Venue",.20),("Entertainment",.10),("Buffer",.07)]
        products=[
            ("Catering package","Swiggy / Zomato",.42,"Plan portions around the guest count."),
            ("Theme decoration kit","Local vendors / Amazon",.15,"A coordinated visual theme for the event."),
            ("Venue shortlist","Local venues / OYO",.20,"Compare capacity, access and package inclusions."),
            ("Music & activities","Local vendors",.08,"Simple entertainment that fits the event."),
        ]
        title=f"{d['event']} · {d['guests']} guests"
    else:
        allocations=[("Main jewellery",.55),("Earrings",.18),("Bracelet/Bangle",.14),("Reserve",.13)]
        products=[
            ("Statement necklace","Amazon / Flipkart",.36,"Choose a silhouette that complements the outfit neckline."),
            ("Matching earrings","Amazon / Flipkart",.16,"Keep the metal tone consistent with the main piece."),
            ("Minimal bracelet","Amazon",.11,"Adds balance without competing with the necklace."),
            ("Occasion-ready set","Amazon / Flipkart",.20,"A coordinated option when you prefer a complete look."),
        ]
        title=f"{d['occasion']} · {d['style']} edit"
    alloc=[{"name":n,"amount":round(budget*p),"percent":round(p*100)} for n,p in allocations]
    recs=[{"name":n,"source":s,"amount":round(budget*p),"note":note} for n,s,p,note in products]
    return {"title":title,"budget":budget,"allocations":alloc,"recommendations":recs,
            "summary":f"Plan built around {money(budget)} with a small reserve to keep the budget flexible."}
