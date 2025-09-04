import re
import streamlit as st
import pandas as pd

st.title("💊 AI Medical Prescription Extraction")

# Input complete prescription text
prescription_text = st.text_area("Paste complete prescription text here:", height=300)

def extract_prescription_details(text):
    details = {
        "Patient": {"Name": "", "Age": "", "Gender": "", "Contact": ""},
        "Doctor": {"Name": "", "Specialization": "", "Hospital": "", "Contact": ""},
        "Medicines": [],
        "General Instructions": {"Dietary": "", "Lifestyle": "", "Follow-up": ""},
        "Notes": {"Date": ""}
    }

    lines = text.split("\n")  # process line by line

    # --- Patient Info ---
    for line in lines:
        if line.lower().startswith("patient name"):
            details["Patient"]["Name"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("age"):
            details["Patient"]["Age"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("gender"):
            details["Patient"]["Gender"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("patient contact"):
            details["Patient"]["Contact"] = line.split(":", 1)[-1].strip()

        # --- Doctor Info ---
        elif line.lower().startswith("doctor name"):
            details["Doctor"]["Name"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("specialization"):
            details["Doctor"]["Specialization"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("hospital") or line.lower().startswith("clinic"):
            details["Doctor"]["Hospital"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("doctor contact"):
            details["Doctor"]["Contact"] = line.split(":", 1)[-1].strip()

        # --- Date ---
        elif line.lower().startswith("date") or line.lower().startswith("prescription date"):
            details["Notes"]["Date"] = line.split(":", 1)[-1].strip()

        # --- General Instructions ---
        elif line.lower().startswith("diet"):
            details["General Instructions"]["Dietary"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("rest") or line.lower().startswith("lifestyle"):
            details["General Instructions"]["Lifestyle"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("follow"):
            details["General Instructions"]["Follow-up"] = line.split(":", 1)[-1].strip()

        # --- Medicines ---
        elif any(keyword in line.lower() for keyword in ["mg", "tablet", "capsule", "syrup"]):
            # Try to capture format: Medicine Dosage – Frequency – Duration – Instructions
            parts = re.split(r"–|-", line)  # split by dash
            med_data = {
                "Medicine Name": parts[0].strip() if len(parts) > 0 else "",
                "Dosage": re.search(r"\d+mg", line, re.I).group() if re.search(r"\d+mg", line, re.I) else "",
                "Frequency": [p.strip() for p in parts if "time" in p or "daily" in p.lower()][0] if any("time" in p or "daily" in p.lower() for p in parts) else "",
                "Duration": [p.strip() for p in parts if "day" in p.lower()][0] if any("day" in p.lower() for p in parts) else "",
                "Instructions": parts[-1].strip() if len(parts) > 1 else ""
            }
            details["Medicines"].append(med_data)

    return details


if st.button("Extract Details"):
    if prescription_text.strip() == "":
        st.warning("Please paste the prescription text!")
    else:
        extracted = extract_prescription_details(prescription_text)

        st.header("📋 Extracted Prescription Details")

        st.subheader("👤 Patient Information")
        st.json(extracted["Patient"])

        st.subheader("👨‍⚕️ Doctor Information")
        st.json(extracted["Doctor"])

        st.subheader("💊 Medicines")
        if extracted["Medicines"]:
            df = pd.DataFrame(extracted["Medicines"])
            st.table(df)
        else:
            st.write("No medicines detected.")

        st.subheader("📌 General Instructions")
        st.json(extracted["General Instructions"])

        st.subheader("📝 Notes")
        st.json(extracted["Notes"])
