import streamlit as st
import pandas as pd
import plotly.express as px

# Liste der gültigen 2-Buchstaben-Wörter im englischen Scrabble
two_letter_words = [
    "aa", "ab", "ad", "ae", "ag", "ah", "ai", "al", "am", "an", "ar", "as", "at", "aw", "ax", "ay",
    "ba", "be", "bi", "bo", "by",
    "da", "de", "do",
    "ed", "ef", "eh", "el", "em", "en", "er", "es", "et", "ex",
    "fa", "fe",
    "go",
    "ha", "he", "hi", "ho",
    "id", "if", "in", "is", "it",
    "jo",
    "ka", "ki",
    "la", "li", "lo",
    "ma", "me", "mi", "mm", "mo", "mu", "my",
    "na", "ne", "no", "nu",
    "od", "oe", "of", "oh", "oi", "om", "on", "op", "or", "os", "ow", "ox", "oy",
    "pa", "pe", "pi",
    "qi",
    "re",
    "sh", "si", "so",
    "ta", "te", "ti", "to",
    "uh", "um", "un", "up", "us", "ut",
    "we",
    "wo",
    "xi", "xu",
    "ya", "ye", "yo",
    "za"
]

# Beschreibungen der 2-Buchstaben-Wörter
word_descriptions = {
    "aa": "Rough, cindery lava.",
    "ab": "An abdominal muscle.",
    "ad": "An advertisement.",
    "ae": "One (Scots Gaelic).",
    "ag": "Agricultural (informal).",
    "ah": "Expression of surprise.",
    "ai": "A three-toed sloth.",
    "al": "An East Indian tree.",
    "am": "1st person singular present of be.",
    "an": "A form of the indefinite article.",
    "ar": "The letter 'r'.",
    "as": "To the same degree.",
    "at": "In the position of.",
    "aw": "Expression of disappointment.",
    "ax": "A tool for chopping.",
    "ay": "Variant of 'aye', yes.",
    "ba": "An eternal soul (Egyptian mythology).",
    "be": "To exist.",
    "bi": "A bisexual person.",
    "bo": "A friend or pal.",
    "by": "Near or next to.",
    "da": "Dad.",
    "de": "Of (French).",
    "do": "Perform an action.",
    "ed": "Education.",
    "ef": "The letter 'f'.",
    "eh": "Expression of inquiry.",
    "el": "An elevated railway.",
    "em": "A printer's measure.",
    "en": "Another printer's measure.",
    "er": "Expression of hesitation.",
    "es": "The letter 's'.",
    "et": "Past tense of eat.",
    "ex": "A former partner.",
    "fa": "A musical note.",
    "fe": "A Hebrew letter.",
    "go": "To move from one place to another.",
    "ha": "Expression of triumph.",
    "he": "A male person.",
    "hi": "Informal greeting.",
    "ho": "Expression of surprise.",
    "id": "Part of the psyche.",
    "if": "A condition.",
    "in": "Contained by.",
    "is": "3rd person singular present of be.",
    "it": "A neuter pronoun.",
    "jo": "A sweetheart (Scots).",
    "ka": "The spiritual self (ancient Egypt).",
    "ki": "The vital force (Japanese).",
    "la": "A musical note.",
    "li": "A Chinese unit of distance.",
    "lo": "Expression of surprise.",
    "ma": "Mother.",
    "me": "1st person singular pronoun.",
    "mi": "A musical note.",
    "mm": "Expression of satisfaction.",
    "mo": "A moment.",
    "mu": "A Greek letter.",
    "my": "Possessive pronoun.",
    "na": "No.",
    "ne": "Born with the name of.",
    "no": "A negative reply.",
    "nu": "A Greek letter.",
    "od": "A hypothetical force.",
    "oe": "A whirlwind off the Faeroe Islands.",
    "of": "Belonging to.",
    "oh": "Expression of surprise.",
    "oi": "Expression of dismay.",
    "om": "A mantra used in meditation.",
    "on": "Position above.",
    "op": "A style of abstract art.",
    "or": "A conjunction.",
    "os": "A bone.",
    "ow": "Expression of pain.",
    "ox": "A domesticated bovine animal.",
    "oy": "Expression of dismay.",
    "pa": "A father.",
    "pe": "A Hebrew letter.",
    "pi": "A mathematical constant.",
    "qi": "The vital force (Chinese).",
    "re": "A musical note.",
    "sh": "Used to urge silence.",
    "si": "A musical note.",
    "so": "A musical note.",
    "ta": "Expression of gratitude.",
    "te": "A musical note.",
    "ti": "A musical note.",
    "to": "In the direction of.",
    "uh": "Expression of hesitation.",
    "um": "Expression of hesitation.",
    "un": "One.",
    "up": "Position above.",
    "us": "1st person plural pronoun.",
    "ut": "A musical note (archaic).",
    "we": "1st person plural pronoun.",
    "wo": "Woe (archaic).",
    "xi": "A Greek letter.",
    "xu": "A currency of Vietnam.",
    "ya": "You.",
    "ye": "You (archaic).",
    "yo": "Expression of greeting.",
    "za": "Pizza."
}

# Buchstaben des Alphabets
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Kreuztabelle initialisieren
crosstab = pd.DataFrame('', index=alphabet, columns=alphabet)

# Wörter in die Kreuztabelle eintragen
for word in two_letter_words:
    first, second = word
    crosstab.loc[first, second] = word

# Interaktives Dashboard
st.set_page_config(page_title="Scrabble 2-Letter Words", layout="wide")
st.title("Interactive 2-Letter Scrabble Words Crosstab")

# Erstelle eine Plotly-Heatmap
fig = px.imshow(
    crosstab.applymap(lambda x: len(x)),  # Erstelle eine Heatmap basierend auf der Länge des Inhalts
    labels=dict(x="Second Letter", y="First Letter", color="Word Present"),
    x=alphabet,
    y=alphabet,
    color_continuous_scale="Viridis",
    text_auto=True
)

# Füge Beschreibungen als Hover-Information hinzu
for i, row in enumerate(alphabet):
    for j, col in enumerate(alphabet):
        word = crosstab.loc[row, col]
        if word in word_descriptions:
            fig.data[0].text[i][j] = word.upper()  # Zeige das Wort in Großbuchstaben
            fig.data[0].customdata[i][j] = word_descriptions[word]

fig.update_traces(
    hovertemplate="<b>%{text}</b><br>Description: %{customdata}<extra></extra>",
    textposition="middle center"
)

# Zeige das Diagramm an
st.plotly_chart(fig, use_container_width=True)
