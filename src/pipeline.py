from src.compression import compress_text
from src.summarizer_api import summarize_text

def citizen_dashboard_pipeline(text):
    compressed = compress_text(text)

    # Try summary (if it fails, return compressed)
    try:
        summary = summarize_text(compressed)
        return summary
    except:
        return compressed