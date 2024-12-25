import re

def process_text(text):
    # Collapse multiple spaces into a single space
    cleaned_text = re.sub(r"\s+", " ", text)
    
    # Remove punctuation but keep spaces and alphanumeric characters (consider keeping periods, commas)
    cleaned_text = re.sub(r"[^\w\s,.]", "", cleaned_text)
    
    # Remove leading/trailing whitespace
    cleaned_text = cleaned_text.strip()
    
    # Optionally convert to lowercase for uniformity
    cleaned_text = cleaned_text.lower()
    
    return cleaned_text
