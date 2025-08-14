"""
Tone marking service for Yoruba language.
Adds diacritics (tone marks) to Yoruba text.
"""

import re


def add_tone_marks(text: str) -> str:
    """
    Add tone marks to Yoruba text based on common patterns.
    
    Args:
        text (str): Input Yoruba text without tone marks
        
    Returns:
        str: Text with tone marks added
    """
    if not text:
        return text
    
    result = text
    
    # Common tone patterns
    patterns = {
        "omo": "ọmọ",
        "baba": "bàbá",
        "mama": "màmá",
        "mi": "mi",
        "re": "rẹ",
        "wa": "wa",
        "won": "wọn",
        "ti": "tí",
        "ni": "ní",
        "si": "sí",
        "ko": "kò",
        "se": "ṣe",
        "je": "jẹ",
    }
    
    # Apply patterns
    for pattern, replacement in patterns.items():
        result = re.sub(
            r'\b' + re.escape(pattern) + r'\b', 
            replacement, 
            result, 
            flags=re.IGNORECASE
        )
    
    return result
