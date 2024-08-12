
# Scrabble 2-Letter Words Dashboard

This repository contains a Streamlit application that visualizes valid two-letter Scrabble words for multiple languages. The dashboard displays a heatmap that allows users to explore and learn about these words interactively.

## Demo

Demo here: https://scrabble-words.streamlit.app/


## Features

- **Interactive Heatmap**: Displays two-letter words with their meanings for the selected language.
- **Multiple Language Support**: Easily switch between languages to view words and descriptions.
- **Hover Information**: Provides detailed descriptions of each word when hovered over.
- **Customizable**: Easily extendable to include more languages by adding new JSON files.

## Installation

To run this application, you'll need to have Python installed on your system. Follow these steps to get started:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/lucameier/scrabble.git
   cd scrabble-dashboard
   ```

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   streamlit run dashboard.py
   ```

   This will launch the application in your default web browser.

## Usage

- Select the desired language from the dropdown menu.
- Hover over the squares in the heatmap to view detailed descriptions of the words.
- Use the application to enhance your Scrabble gameplay or expand your vocabulary in different languages.

## File Structure

- `dashboard.py`: The main Streamlit application script.
- `requirements.txt`: Lists the Python dependencies needed to run the application.
- `*.json`: JSON files containing two-letter words and their descriptions for different languages.

## Adding New Languages

To add a new language:

1. Create a new JSON file in the same format as the existing ones.
2. Place it in the same directory as the other JSON files.
3. The application will automatically detect and list the new language in the dropdown menu.

### Example JSON Format

Here is a simplified example of what a JSON file should look like:

```json
{
  "two_letter_words": ["aa", "ab", "ad"],
  "word_descriptions": {
    "aa": "A type of lava.",
    "ab": "An abdominal muscle.",
    "ad": "An advertisement."
  }
}
```

## Contributing

Contributions are welcome! If you would like to add new features or improve the application, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. 

## Contact

For questions or suggestions, please contact me.
