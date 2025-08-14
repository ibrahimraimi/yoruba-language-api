#!/usr/bin/env python3
"""
Test script for AI Translation Feature.
"""

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.ai_translation_service import (
    translate_to_yoruba, 
    is_ai_available
)


def test_ai_translation():
    """Test the AI translation service."""
    print("🤖 Testing AI Translation Service")
    print("=" * 50)
    
    # Check if AI service is available
    if not is_ai_available():
        print("❌ AI translation service is not available.")
        print("Make sure you have set OPENAI_API_KEY in your .env file.")
        return
    
    print("✅ AI translation service is available!")
    print("Model: gpt-4o")
    print()
    
    # Test words
    test_words = [
        "happiness",
        "wisdom", 
        "courage",
        "friendship",
        "knowledge"
    ]
    
    print("Testing AI translations:")
    print("-" * 30)
    
    for word in test_words:
        try:
            print(f"Translating: {word}")
            result = translate_to_yoruba(word)
            
            print(f"  Yoruba: {result['translation']}")
            print(f"  Part of speech: {result['part_of_speech']}")
            print(f"  Example: {result['example']}")
            print(f"  Source: {result['source']}")
            print()
            
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            print()


if __name__ == "__main__":
    test_ai_translation()
