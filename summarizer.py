import time
from model import get_summarizer

def summarize_text(text, length_option):
    """
    Summarize the given text based on the length option.
    
    Args:
        text (str): The input text to summarize.
        length_option (str): 'short', 'medium', or 'long'
    
    Returns:
        dict: {
            'summary': str,
            'processing_time': float,
            'original_length': int,
            'summary_length': int
        }
    """
  #mapping length
    length_map = {
        'short': 50,
        'medium': 100,
        'long': 150
    }
    max_length = length_map.get(length_option, 100)
    min_length = max(5, min(max_length - 10, 20))  # Ensure min_length is reasonable relative to max_length
    
    # Counting  original words
    original_length = len(text.split())
    
    # Get the summarizer
    summarizer = get_summarizer()
    tokenizer = summarizer["tokenizer"]
    model = summarizer["model"]
    
    # Time the summarization
    start_time = time.time()
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_length, 
        min_length=min_length,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=2,
        length_penalty=2.0,
        temperature=0.7
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    end_time = time.time()
    summary_length = len(summary.split())
    processing_time = end_time - start_time
    
    return {
        'summary': summary,
        'processing_time': processing_time,
        'original_length': original_length,
        'summary_length': summary_length
    }