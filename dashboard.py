import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import json
import os

# Interaktives Dashboard konfigurieren
st.set_page_config(
    page_title="Scrabble 2-Letter Words",
    page_icon="🅰️",
    layout="wide"
)

# Verzeichnis mit JSON-Dateien
json_directory = "."  # Hier können Sie das Verzeichnis anpassen, in dem sich die JSON-Dateien befinden

# Alle JSON-Dateien im Verzeichnis auflisten
def list_json_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.json')]


# Lade Sprachdaten
def load_language_data(language_file):
    with open(language_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# JSON-Dateien auflisten
json_files = list_json_files(json_directory)

# Verfügbare Sprachen basierend auf Dateinamen (ohne .json)
languages = [os.path.splitext(file)[0] for file in json_files]

# Standardmäßig Englisch auswählen
default_language_index = languages.index('english') if 'english' in languages else 0

# Sprache auswählen
selected_language = st.selectbox("Select Language", languages, index=default_language_index)

# Pfad zur ausgewählten Sprachdatei
language_file = f"{selected_language}.json"

# Sprachdaten laden
data = load_language_data(language_file)
two_letter_words = data["two_letter_words"]
word_descriptions = data["word_descriptions"]

# Buchstaben des Alphabets (nur A-Z)
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Kreuztabelle initialisieren
crosstab = pd.DataFrame('', index=alphabet, columns=alphabet)

# Wörter in die Kreuztabelle eintragen
for word in two_letter_words:
    word = word.strip().lower()  # Entferne Leerzeichen und konvertiere in Kleinbuchstaben
    # Sicherstellen, dass es ein 2-Buchstaben-Wort mit erlaubten Zeichen ist
    if len(word) == 2 and all(c in alphabet for c in word):
        first, second = word
        crosstab.loc[first, second] = word.upper()  # Zeige Wörter in Großbuchstaben

# Erstelle eine Matrix für die Farbdarstellung (1 für Wörter, 0 für leere Felder)
color_matrix = np.where(crosstab != '', 1, 0)

# Initialisiere customdata mit Beschreibungen
hover_data = np.empty((len(alphabet), len(alphabet)), dtype=object)
for i, row in enumerate(alphabet):
    for j, col in enumerate(alphabet):
        word = crosstab.loc[row, col]
        hover_data[i][j] = word_descriptions.get(word.lower(), "")

# Erstelle die Plotly-Heatmap mit Annotationen
fig = px.imshow(
    color_matrix,  # Verwende die Maskenmatrix für die Farbdarstellung
    labels=dict(x="Second Letter", y="First Letter"),
    x=alphabet,
    y=alphabet,  # Verwende alphabet für die y-Achse
    color_continuous_scale=[(0.0, "papayawhip"), (1.0, "lightgreen")],
    aspect="auto",  # Automatische Anpassung des Aspekts
    text_auto=True
)

# Text und Hover-Informationen aktualisieren
fig.update_traces(
    text=crosstab.values,
    texttemplate="<b>%{text}</b>",
    textfont_size=16,  # Größere Schriftgröße für Text
    customdata=hover_data,
    hovertemplate="<span style='font-size:16px'>%{customdata}</span><extra></extra>",
    hoverinfo="skip"  # Standardmäßig Hoverinformationen überspringen
)

# Entferne Skala und setze Gitterlinien
fig.update_layout(
    xaxis=dict(tickvals=list(range(len(alphabet))), ticktext=alphabet, side="top", showgrid=False),
    yaxis=dict(tickvals=list(range(len(alphabet))), ticktext=alphabet, autorange="reversed", showgrid=False),
    coloraxis_showscale=False,
    margin=dict(l=50, r=50, b=50, t=50),
    width=1000,
    height=1000,
)

# Setze Lücken zwischen den Zellen
fig.update_traces(xgap=2, ygap=2)

# Titel der App
st.title("Interactive 2-Letter Scrabble Words Crosstab")

# Zeige das Diagramm an
st.plotly_chart(fig, use_container_width=True)
