# Smart Text Summarization

A web-based text summarization application using Python, Flask, and Hugging Face Transformers.

## Features

- Input long text through a web interface
- Choose summary length: Short, Medium, or Long
- Generate summaries using a pretrained Transformer model (BART)
- Display processing time and text length metrics

## Setup

1. Ensure Python 3.7+ is installed.
2. Clone or download the project.
3. Navigate to the project directory.
4. Create a virtual environment: `python -m venv .venv`
5. Activate the virtual environment: 
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
6. Install dependencies: `pip install -r requirements.txt`

## Running the Application

1. Activate the virtual environment if not already.
2. Run the Flask app: `python app.py`
3. Open your browser and go to `http://127.0.0.1:5000/`

Note: The first summarization request may take longer as the model downloads.

## Project Structure

- `app.py`: Flask backend application
- `model.py`: Model loading function
- `summarizer.py`: Summarization logic
- `templates/index.html`: Frontend HTML
- `static/css/style.css`: Styles
- `static/js/script.js`: JavaScript
- `requirements.txt`: Python dependencies