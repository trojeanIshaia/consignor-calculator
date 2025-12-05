import streamlit as st
import os

def main():
    # --- PAGE CONFIGURATION ---
    st.set_page_config(page_title="Consignor Income Calculator", page_icon="🏷️")

    # --- BRAND DATA ---
    luxury_brands = [
        "Alexander McQueen", "AllSaints", "Balenciaga", "Balmain", "Bottega Veneta", 
        "Burberry", "Chanel", "Christian Louboutin", "Coach (Designer line)", "Dior", 
        "Fear of God", "Fendi", "Givenchy", "Giuseppe Zanotti", "Gucci", "Hermès", 
        "Jacquemus", "Jimmy Choo", "Kate Spade New York", "Louis Vuitton", "Manolo Blahnik", 
        "Max Mara", "Michael Kors Collection", "Off-White", "Palm Angels", "Prada", 
        "Ralph Lauren Collection", "Reiss", "Saint Laurent (YSL)", "Stuart Weitzman", 
        "Ted Baker", "Tory Burch", "Valentino", "Versace", "Zimmermann"
    ]

    standard_brands = [
        "Abercrombie & Fitch", "Aldo", "Ann Taylor", "Banana Republic", "Calvin Klein", 
        "Cole Haan", "DKNY", "Express", "Fossil", "French Connection (FCUK)", "Gap", 
        "Guess", "Hollister", "Karen Millen", "Kenneth Cole", "Levi’s", "Loft", 
        "Mango", "Marc Jacobs (Diffusion line)", "Massimo Dutti", "Michael Kors (Main line)", 
        "Nautica", "Next", "Nine West", "Oasis", "Phase Eight", "Polo Ralph Lauren", 
        "River Island", "Steve Madden", "Tommy Hilfiger", "Topshop", "Vince Camuto", 
        "Wallis", "Zara"
    ]

    fast_fashion_brands = [
        "ASOS", "Adidas", "Aeropostale", "American Eagle", "Boohoo", "Champion", 
        "Charlotte Russe", "Cider", "Converse", "Cotton On", "Fashion Nova", 
        "Forever 21", "H&M", "Hollister (Casual line)", "Justice", "Nike", 
        "Old Navy", "PrettyLittleThing", "Primark", "Puma", "Rainbow", "Reebok", 
        "Romwe", "Rue21", "SHEIN", "Sketchers", "Target (Wild Fable, A New Day)", 
        "Uniqlo", "Walmart (No Boundaries, Time & Tru)"
    ]

    all_brands = sorted(luxury_brands + standard_brands + fast_fashion_brands)
    all_brands.append("Other")

    # --- LOGO & HEADER ---
    # This checks if you uploaded a file named 'logo.png' or 'logo.jpg'
    # Make sure the file name in GitHub matches one of these exactly!
    if os.path.exists("logo.png"):
        st.image("logo.png", width=200) 
    elif os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=200)
    
    st.title("Consignor Income Calculator")
    
    # Updated Full Header Description
    st.write("""
    Curious how much you could earn from your pre-loved pieces? 
    Use this quick calculator to estimate your potential payout before bringing in your items. 
    This tool is designed to help you understand how consignment works and what to expect before your items are reviewed. 
    Actual listing prices and payout amounts will be confirmed once your pieces are inspected and accepted for sale.
    """)

    st.markdown("---")

    # --- INPUT FORM ---
    item_types = ["Dress", "Top", "Bottom", "Jacket/Outerwear", "Shoes", "Handbag", "Accessory", "Menswear", "Kidswear", "Other"]
    st.selectbox("Item Type", item_types)

    selected_brand = st.selectbox("Brand", all_brands)
    
    if selected_brand == "Other":
        custom_brand = st.text_input("Please enter the Brand name:")

    category = "Standard" 
    
    if selected_brand in luxury_brands:
        category = "Designer/Luxury"
    elif selected_brand in standard_brands:
        category = "Standard"
    elif selected_brand in fast_fashion_brands:
        category = "Clearance/Fast Fashion"
    elif selected_brand == "Other":
        category = "Standard"

    st.info(f"**Category:** {category}")

    price = st.number_input("Suggested Listing Price ($)", min_value=0.00, step=1.00, format="%.2f")

    # --- CALCULATION LOGIC ---
    if st.button("Calculate Payout"):
        consignor_share = 0.0
        boutique_share = 0.0

        if category == "Designer/Luxury":
            consignor_share = 0.60
            boutique_share = 0.40
        elif category == "Standard":
            consignor_share = 0.50
            boutique_share = 0.50
        elif category == "Clearance/Fast Fashion":
            consignor_share = 0.40
            boutique_share = 0.60
        
        your_earnings = price * consignor_share
        boutique_earnings = price * boutique_share

        st.success(f"### You make: ${your_earnings:,.2f}")
        st.write(f"We make: ${boutique_earnings:,.2f}")
        st.caption(f"Based on a {int(consignor_share*100)}% / {int(boutique_share*100)}% split for {category} items.")

    # --- DISCLAIMER (Cleaned) ---
    st.markdown("---")
    st.caption("### Disclaimer")
    st.caption("""
    The figures shown in this calculator are estimates only. The suggested listing price, 
    consignment rate, and potential payout are subject to change after in-person inspection 
    and review by ReTagged Boutique.
    
    Final pricing and payment amounts may vary based on factors outlined in the Consignment Guide, 
    including item condition, authenticity, brand demand, and cleaning requirements.
    
    Use of this calculator does not constitute a contract or guarantee of sale. 
    The actual amount paid to the consignor will be confirmed in the official Consignment Agreement.
    """)

if __name__ == "__main__":
    main()
