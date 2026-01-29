import streamlit as st

st.set_page_config(page_title="Notenrechner", page_icon="📚")

st.title("📚 Schulnoten-Rechner")

st.write("Gib zwei Teilnoten ein und wähle die Gewichtung.")

# Eingabe der Teilnoten
note1 = st.number_input("Teilnote 1", min_value=1.0, max_value=6.0, step=0.1)
note2 = st.number_input("Teilnote 2", min_value=1.0, max_value=6.0, step=0.1)

# Auswahl der Gewichtung
gewichtung = st.radio(
    "Gewichtung auswählen:",
    ("70% / 30%", "40% / 60%")
)

# Berechnung
if st.button("Gesamtnote berechnen"):
    if gewichtung == "70% / 30%":
        gesamtnote = note1 * 0.7 + note2 * 0.3
    else:
        gesamtnote = note1 * 0.4 + note2 * 0.6

    st.success(f"✅ Die Gesamtnote beträgt: **{gesamtnote:.2f}**")
