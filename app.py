
import pandas as pd
import streamlit as st
from io import BytesIO
# ----------------- Master Maps -----------------
ideal3d_map =  {
    # ---------------- GK Series ----------------
    "GKTwo": [
        "GKTWO RAPID PROTOTYPING MACHINE-50 PCS",
    ],
    "GK3 Ultra": [
        "GK3 ULTRA RAPID PROTOTYPING MACHINE GK3 ULTRA RAPID PROTOTYPING MACHINE",
    ],
    "GK3 Pro": [
        "GK3 PRO RAPID PROTOTYPING MACHINE GK3 PRO RAPID PROTOTYPING MACHINE",
    ],

    # ---------------- Bambu Lab ----------------
    "Bambu Lab A1": [
        "A1-EURAPID PROTOTYPING MACHINE",
        "RAPID PROTOTYPING MACHINE - A1-EU RAPID PROTOTYPING MACHIN",
        "RAPID PROTOTYPING MACHINE - AI RAPID PROTOTYPING MACHIN",  # typo AI → A1
    ],
    "Bambu Lab A1 Mini": [
        "RAPID PROTOTYPING MACHINE - AI MINI RAPID PROTOTYPING MACHIN",
        "A1 MINI-EU RAPID PROTOTYPING MACHINE A1 MINI-EU RAPID PROTOTYPING MACHIN",
        "RAPID PROTOTYPING MACHINE - A1-MINI-EU RAPID PROTOTYPING MACHIN",
        "3D PRINTER - MODEL NO - A1 MINI  EU 3D PRINTER - MODEL NO - A1 MINI  EU",
    ],
    "Bambu Lab A1 Combo": [
        "RAPID PROTOTYPING MACHINE - A1-COMBO1-EU RAPID PROTOTYPING MACHIN",
        "RAPID PROTOTYPING MACHINE - A1-COMBO-EU RAPID PROTOTYPING MACHIN",
        "A1-COMBO-EURAPID PROTOTYPING MACHINE",
    ],
    "Bambu Lab A1 Mini Combo EU": [
        "",
    ],
    "Bambu Lab P1S": [
        "P1SRAPID PROTOTYPING MACHINE",
        "P1S RAPID PROTOTYPING MACHINE P1S RAPID PROTOTYPING MACHIN",
        "RAPID PROTOTYPING MACHINE - P I S RAPID PROTOTYPING MACHIN",
    ],
    "Bambu Lab P1S Combo": [
        "P1S COMBO RAPID PROTOTYPING MACHINE P1S COMBO RAPID PROTOTYPING MACHIN",
        "P1S COMBORAPID PROTOTYPING MACHINE",
        "RAPID PROTOTYPING MACHINE - P1S-COMBO1 RAPID PROTOTYPING MACHIN",
        "RAPID PROTOTYPING MACHINE - P I S COMBO RAPID PROTOTYPING MACHIN",
    ],
    "Bambu Lab X1 Carbon": [
        "X1-CRAPID PROTOTYPING MACHINE",
        "X1-CARBON RAPID PROTOTYPING MACHINE X1-CARBON RAPID PROTOTYPING MACHIN",
    ],
    "Bambu Lab X1 Carbon Combo": [
        "X1-CARBON COMBORAPID PROTOTYPING MACHINE",
        "X1-CARBON COMBO RAPID PROTOTYPING MACHINE X1-CARBON COMBO RAPID PROTOTYPING MACHIN",
        "RAPID PROTOTYPING MACHINE - XI-CARBON COMBO RAPID PROTOTYPING MACHIN",  # XI → X1 typo
    ],
"Bambu Lab H2D Combo": [
        "RAPID PROTOTYPING MACHINE - H2D-COMBO1-EU RAPID PROTOTYPING MACHIN","	RAPID PROTOTYPING MACHINE - H2D-COMBO2-EU RAPID PROTOTYPING MACHIN"
    ],



    # ---------------- Elegoo ----------------
    "Elegoo Saturn 4 Ultra": [
        "ELEGOO SATURN 4 ULTRA RAPID PROTOTYPING MACHINE ELEGOO SATURN 4 ULTRARAPID PROTOTYPING M",
        "ELEGOO SATURN 4 ULTRA RAPID PROTOTYPING MACHINE ELEGOO SATURN 4 ULTRA RAPID PROTOTYPING",
        "ELEGOO SATURN 4 RAPID PROTOTYPING MACHINE ELEGOO SATURN 4 RAPID PROTOTYPING MACHIN",
    ],
    "Elegoo Saturn 4": [
        "ELEGOO SATURN 4 3D PRINTER ELEGOO SATURN 4 3D PRINTER",
    ],
    "Elegoo Saturn 2 8K": [
        "ELEGOO SATURN 2 8K LCD SCREEN ELEGOO SATURN 2 8K LCD SCREEN",
    ],
    "Elegoo Orange Storm Giga": [
        "ELEGOO ORANGESTORM GIGA RAPIDPROTOTYPING MACHINE-15 PCS",
    ],
    "Elegoo Centauri Carbon": [
        "ELEGOO CENTAURI CARBON 3D PRINTER ELEGOO CENTAURI CARBON 3D PRINTER",
    ],
    "Elegoo Neptune 4 Max": [
        "ELEGOO NEPTUNE 4 MAX RAPID PROTOTYPING MACHINE ELEGOO NEPTUNE 4 MAX RAPID PROTOTYPING M",
    ],
    "Elegoo Washing Station": [
        "ELEGOO WASHING STATION ELEGOO WASHING STATION",
    ],
    "Elegoo (Unclassified)": [
        "ELEGOO RAPIDPROTOTYPING MACHINE-80 PCS",  # looks like an Elegoo shipment but generic
    ],

    # ---------------- JAMGHE / Phrozen / Accufab ----------------
    "Jamghe": [
        "JAMGHE RAPID PROTOTYPING MACHINE - 5 NOS JAMGHE RAPID PROTOTYPING MACHINE",
    ],
    "Phrozen": [
        "RAPID PROTOTYPING MACHINE PHROZEN",
    ],
    "Accufab AB-CEL": [
        "ACCUFAB AB-CEL",
    ],

    # ---------------- Generic / Non-model entries ----------------
    "Rapid Prototyping Machine (Generic)": [
        "RAPID PROTOTYPING MACHINE",
        "RAPID PROTOTYPING MACHINE-308 PCS RAPID PROTOTYPING MACHINE-308 PCS",
    ],
    "Accessories (Generic)": [
        "ACCESSORIES FOR RAPID PROTOTYPING MACHINE ACCESSORIES FOR RAPID PROTOTYPING MACHIN",
        " SPARE PARTS / ACCESSORIES / COMPONENT  FOR RAPID PROTOTYPING MACHINE  SPARE PARTS / ACCESSORIES / COMPONENT  FOR RAPID PROTOTYPING MACHI",
    ],
    "Filament (Generic)": [
        "FILAMENTS WHITERAW MATERIAL FOR RAPID PROTOTYPING MACHINE",
        "FILAMENTSRAPID PROTOTYPING MACHINE",
        "FILAMENT RAW MATERIAL FOR RAPID PROTOTYPING MACHINE-83 pc FILAMENT RAW MATERIAL FOR RAPID PROTOTYPING MACHINE-83 pc",
    ],
}

wol3d_map = {
    "ELEGOO SATURN 4": [
        "MODEL-ELEGOO SATURN 4 3D PRINTER"
    ],
    "ELEGOO SATURN 4 ULTRA": [
        "3D PRINTER - MODEL : ELEGOO SATURN 4 ULTRA MODEL-ELEGOO SATURN 4 ULTRA 3D PRINTER",
        "3D PRINTER - MODEL : ELEGOO SATURN 4 ULTRA 3D PRINTER - MODEL : ELEGOO SATURN 4 ULTRA",
        "3D PRINTER - MODEL NO: ELEGOO SATURN 4 ULTRA",
        "MODEL-ELEGOO SATURN 4 ULTRA 3D PRINTER",
        "3D PRINTER -ELEGOO SATURN 4 ULTRA 3D PRINTER -ELEGOO SATURN 4 ULTRA"
    ],
    "ELEGOO SATURN 4 ULTRA 16K": [
        "3D PRINTER - EELEGOO SATURN 4 ULTRA 16K 3D PRINTER - EELEGOO SATURN 4 ULTRA 16K",
        "3D PRINTER - MODEL : ELEGOO SATURN 4 ULTRA 16K 3D PRINTER - MODEL : ELEGOO SATURN 4 ULTRA 16K",
        "3D PRINTER - ELEGOO SATURN 4 ULTRA 16K 3D PRINTER - ELEGOO SATURN 4 ULTRA 16K"
    ],
    "ELEGOO MARS 5 ULTRA": [
        "3D PRINTER -ELEGOO MARS 5 ULTRA 3D PRINTER -ELEGOO MARS 5 ULTRA",
        "MODEL-ELEGOO MARS 5 ULTRA 3D PRINTER"
    ],
    "ELEGOO NEPTUNE 4 PLUS": [
        "3D PRINTER - MODEL NO:ELEGOO NEPTUNE 4 PLUS",
        "3D PRINTER - ELEGOO NEPTUNE 4 PLUS 3D PRINTER - ELEGOO NEPTUNE 4 PLUS"
    ],
    "ELEGOO NEPTUNE 4 MAX": [
        "3D PRINTER - MODEL NO:ELEGOO NEPTUNE 4 MAX 3D PRINTER - MODEL NO:ELEGOO NEPTUNE 4 MAX",
        "3D PRINTER - ELEGOO NEPTUNE 4 MAX - EU PLUG 3D PRINTER - ELEGOO NEPTUNE 4 MAX - EU PLUG",
        "3D PRINTER - MODEL NO:ELEGOO NEPTUNE 4 MAX"
    ],
    "ELEGOO CENTAURI CARBON": [
        "3D PRINTER - ELEGOO CENTAURI CARBON EU PLUG 3D PRINTER - ELEGOO CENTAURI CARBON - EU PLUG",
        "3D PRINTER - ELEGOO CENTAURI CARBON EU PLUG 3D PRINTER - ELEGOO CENTAURI CARBON EU PLUG"
    ],
    "ELEGOO ORANGE STORM GIGA": [
        "MODEL-ELEGOO ORANGE STORM GIGA 3D PRINTER",
        "3D PRINTER - MODEL : ELEGOO ORANGE STORM GIGA 3D PRINTER - MODEL : ELEGOO ORANGE STORM GIGA"
    ],
    "BAMBU LAB P1S": [
        "3D PRINTER - MODEL NO - P1S",
        "3D PRINTER - MODEL NO - P1S 3D PRINTER - MODEL NO - P1S"
    ],
    "BAMBU LAB P1S COMBO": [
        "3D PRINTER - MODEL NO- P1S COMBO",
        "3D PRINTER - MODEL NO - P1S COMBO 3D PRINTER - MODEL NO - P1S COMBO",
        "3D PRINTER - MODEL NO- P1S COMBO 3D PRINTER - MODEL NO- P1S COMBO"
    ],
    "BAMBU LAB P1P": [
        "3D PRINTER - MODEL NO - P1P 3D PRINTER - MODEL NO - P1P"
    ],
    "BAMBU LAB X1 CARBON": [
        "3D PRINTER - MODEL NO- X1 CARBON COMBO",
        "3D PRINTER - MODEL NO - X1-CARBON 3D PRINTER - MODEL NO - X1-CARBON",
        "3D PRINTER - MODEL NO - X1 CARBON COMBO 3D PRINTER - MODEL NO - X1 CARBON COMBO",
        "3D PRINTER - MODEL NO - X1 CARBON 3D PRINTER - MODEL NO - X1 CARBON",
        "3D PRINTER - MODEL NO - X1-CARBON COMBO 3D PRINTER - MODEL NO - X1-CARBON COMBO"
    ],
    "BAMBU LAB X1E COMBO": [
        "3D PRINTER - MODEL NO -X1E COMBO-EU 3D PRINTER - MODEL NO -X1E COMBO-EU",
        "3D PRINTER - MODEL NO - X1E COMBO EU"
    ],
    "BAMBU LAB A1": [
        "3D PRINTER - MODEL NO - A1-EU 3D PRINTER - MODEL NO - A1-EU",
        "3D PRINTER - MODEL NO - A1 EU 3D PRINTER - MODEL NO - A1 EU",
        "3D PRINTER - MODEL NO - A1 EU"
    ],
    "BAMBU LAB A1 COMBO": [
        "3D PRINTER - MODEL NO - A1-COMBO-EU 3D PRINTER - MODEL NO - A1 EU",
        "3D PRINTER - MODEL NO - A1 COMBO EU 3D PRINTER - MODEL NO - A1 COMBO EU",
        "3D PRINTER - MODEL NO - A1 COMBO EU 3D PRINTER - MODEL NO - A1 COMBO AU",
        "3D PRINTER - MODEL NO - A1 -COMBO-EU 3D PRINTER - MODEL NO - A1 -COMBO-EU",
        "3D PRINTER - MODEL NO - A1 COMBO EU",
        "3D PRINTER - MODEL NO - A1-COMBO-EU 3D PRINTER - MODEL NO - A1-COMBO-EU",
        "3D PRINTER - MODEL NO - A1 COMBO AU 3D PRINTER - MODEL NO - A1 COMBO AU"
    ],
    "BAMBU LAB A1 MINI": [
        "3D PRINTER - MODEL NO- A1 MINI-EU 3D PRINTER - MODEL NO- A1 MINI-EU",
        "3D PRINTER - MODEL NO - A1 MINI-EU 3D PRINTER - MODEL NO - A1 MINI-EU",
        "3D PRINTER - MODEL NO - A1 MINI EU 3D PRINTER - MODEL NO - A1 MINI EU",
        "3D PRINTER - MODEL NO - A1 MINI EU 3D PRINTER - MODEL NO - A1 MINI EU",
        "3D PRINTER - MODEL NO - A1 MINI EU 3D PRINTER - MODEL NO - A1 MINI EU"
    ],
    "BAMBU LAB A1 MINI COMBO": [
        "3D PRINTER - MODEL NO - A1 MINI-COMBO-EU 3D PRINTER - MODEL NO - A1 MINI-COMBO-EU",
        "3D PRINTER - MODEL NO - A1 MINI  COMBO EU 3D PRINTER - MODEL NO - A1 MINI  COMBO EU"
    ],
    "CREALITY ENDER 3": [
        "3D PRINTER - MODEL NO - CREALITY ENDER 3 3D PRINTER - MODEL NO - CREALITY ENDER 3",
        "3D PRINTER - MODEL NO - ENDER 3 3D PRINTER - MODEL NO - CREALITY ENDER 3"
    ],
    "CREALITY ENDER 3 V3 KE": [
        "3D PRINTER - MODEL NO - CREALITY ENDER 3 V3 KE 3D PRINTER - MODEL NO - CREALITY ENDER 3 V3 KE"
    ],
    "CREALITY ENDER 3 V3 SE": [
        "3D PRINTER - MODEL NO - CREALITY ENDER 3 V3 SE 3D PRINTER - MODEL NO - CREALITY ENDER 3 V3 SE",
        "3D PRINTER - MODEL NO -CREALITY ENDER 3 V3 SE 3D PRINTER - MODEL NO -CREALITY ENDER 3 V3 SE"
    ],
    "CREALITY ENDER 5 PRO": [
        "3D PRINTER - MODEL NO - CREALITY ENDER 5 PRO 3D PRINTER - MODEL NO - CREALITY ENDER 5 PRO",
        "3D PRINTER - MODEL NO - ENDER 5 PRO 3D PRINTER - MODEL NO - ENDER 5 PRO"
    ],
    "CREALITY K1 MAX": [
        "3D PRINTER - MODEL NO - K1 MAX",
        "3D PRINTER - MODEL NO - CREALITY K1 MAX 3D PRINTER - MODEL NO - CREALITY K1 MAX"
    ],
    "CREALITY K1C": [
        "3D PRINTER - MODEL NO - K1 C"
    ],
    "CREALITY K2 PLUS COMBO": [
        "3D PRINTER - MODEL NO - CREALITY K2 PLUS COMBO 3D PRINTER - MODEL NO - CREALITY K2 PLUS COMBO",
        "3D PRINTER - MODEL NO - K2 PLUS COMBO 3D PRINTER - MODEL NO - K2 PLUS COMBO"
    ],
    "CREALITY HI": [
        "3D PRINTER - MODEL NO - CREALITY HI 3D PRINTER - MODEL NO - CREALITY HI","3D PRINTER - MODEL NO - CREALITY CREALITY HI 3D PRINTER - MODEL NO - CREALITY CREALITY HI"
    ],
    "CREALITY HI COMBO": [
        "3D PRINTER - MODEL NO - CREALITY HI COMBO 3D PRINTER - MODEL NO - CREALITY HI COMBO"
    ],
    "FLASHFORGE ADVENTURER 5M": [
        "3D PRINTER - MODEL : ADVENTURER 5M 3D PRINTER - MODEL : ADVENTURER 5M",
        "3D PRINTER - ADVENTURER 5M 3D PRINTER - ADVENTURER 5M"
    ],
    "FLASHFORGE ADVENTURER 5M PRO": [
        "3D PRINTER - MODEL : ADVENTURER 5M PRO 3D PRINTER - MODEL : ADVENTURER 5M",
        "3D PRINTER - ADVENTURER 5M PRO 3D PRINTER - ADVENTURER 5M PRO"
    ],
    "FLASHFORGE GUIDER 3 ULTRA": [
        "3D PRINTER - GUIDER 3 ULTRA 3D PRINTER - GUIDER 3 ULTRA"
    ],
    "H2D COMBO1 EU": [
        "3D PRINTER - MODEL NO - H2D-COMBO1-EU 3D PRINTER - MODEL NO - H2D-COMBO1-EU"
    ],
    "H2D COMBO2 EU": [
        "3D PRINTER - MODEL NO - H2D-COMBO2-EU 3D PRINTER - MODEL NO - H2D-COMBO2-EU"
    ],
    "BAMBU LAB P2": [
        "3D PRINTER - MODEL : P2 3D PRINTER - MODEL : P2"
    ],
    "RC MINI": [
        "3D PRINTER - MODEL : RC MINI 3D PRINTER - MODEL : RC MINI"
    ]
}

#----------------- Helper: Reverse map -----------------
def build_reverse_map(product_map):
    reverse_map = {}
    for canonical, variants in product_map.items():
        for v in variants:
            reverse_map[v.strip().upper()] = canonical
    return reverse_map

# ----------------- Exact mapping function -----------------
def map_to_master_exact(raw_name, reverse_map):
    if not isinstance(raw_name, str):
        return None
    return reverse_map.get(raw_name.strip().upper(), raw_name)

# ----------------- Streamlit App -----------------
st.set_page_config(page_title="3D Printer Import Dashboard", layout="wide")
st.title("📊 3D Printer Import Dashboard")

# Select company
company = st.radio("Select Company", ["Ideal3D", "WOL3D"], horizontal=True)

# Load corresponding product map
if company == "Ideal3D":
    product_map = ideal3d_map   # <-- you need to define this dict
else:
    product_map = wol3d_map     # <-- you need to define this dict

reverse_map = build_reverse_map(product_map)

# File upload
uploaded_file = st.file_uploader("📂 Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df.columns = df.columns.str.strip()

    if "HS Code" not in df.columns or "Product Description" not in df.columns:
        st.error("❌ Excel must contain 'HS Code' and 'Product Description' columns")
    else:
        # === Filter by HS Code ===
        df = df[df["HS Code"] == 84775900]

        # === Apply mapping ===
        df["Product Master"] = df["Product Description"].apply(
            lambda x: map_to_master_exact(x, reverse_map)
        )

        # Ensure Date column is datetime (for unique counts)
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.date

        # === Grouped summary report ===
        report = (
            df.groupby("Product Master")
            .agg(
                Quantity=("Quantity", "sum"),
                Shipment_Dates=("Date", lambda x: ", ".join(sorted(x.dropna().astype(str).unique()))),
                Shippers=("Shipper", lambda x: ", ".join(sorted(x.dropna().astype(str).unique()))),
                Number_of_Shipments=("Date", "nunique"),
                Number_of_Shippers=("Shipper", "nunique"),
            )
            .reset_index()
        )

        # --- KPIs ---
        total_rows = len(df)
        total_qty = report["Quantity"].sum()
        total_models = report["Product Master"].nunique()
        total_shippers = df["Shipper"].nunique()

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("📦 Total Imports", total_rows)
        col2.metric("🔢 Total Quantity", total_qty)
        col3.metric("🖨️ Unique Models", total_models)
        col4.metric("🚢 Unique Shippers", total_shippers)

        # --- Show grouped report ---
        st.subheader("📑 Grouped Import Report")
        st.dataframe(report, use_container_width=True)

        # --- Bar chart ---
        st.subheader("📊 Quantity by Product Model")
        st.bar_chart(report.set_index("Product Master")["Quantity"])

        # --- Show raw mapped data ---
        st.subheader("📋 Raw Import Data (Order-level)")
        st.dataframe(df, use_container_width=True)

        # --- Download buttons ---
        def to_excel_bytes(df):
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                df.to_excel(writer, index=False)
            return buffer.getvalue()

        st.download_button(
            label="📥 Download Grouped Report (Excel)",
            data=to_excel_bytes(report),
            file_name=f"{company}_grouped_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        st.download_button(
            label="📥 Download Raw Data (Excel)",
            data=to_excel_bytes(df),
            file_name=f"{company}_raw_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
