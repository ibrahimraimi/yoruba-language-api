#!/usr/bin/env python3
"""
Test script for Mock AI Translation Service.
"""

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.services.mock_ai_service import translate_to_yoruba_mock


def test_mock_ai_translation():
    """Test the mock AI translation service."""
    print("🤖 Testing Mock AI Translation Service")
    print("=" * 50)
    
    # Test words
    test_words = [
        "happiness",
        "wisdom", 
        "courage",
        "friendship",
        "knowledge",
        "love",
        "peace",
        "hope",
        "computer",  # Unknown word to test mock generation
        "technology"  # Another unknown word
    ]
    
    print("Testing mock AI translations:")
    print("-" * 40)
    
    for word in test_words:
        try:
            print(f"Translating: {word}")
            result = translate_to_yoruba_mock(word)
            
            print(f"  Yoruba: {result['translation']}")
            print(f"  Part of speech: {result['part_of_speech']}")
            print(f"  Example: {result['example']}")
            print(f"  Source: {result['source']}")
            print()
            
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            print()


if __name__ == "__main__":
    test_mock_ai_translation()
