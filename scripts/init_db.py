#!/usr/bin/env python3
"""
Database initialization script for Yoruba Language API.
Populates the database with sample translations and proverbs.
"""

import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import engine, Base, SessionLocal
from app.database import Translation, Proverb


def init_database():
    """Initialize the database with tables and sample data."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    print("Populating database with sample data...")
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(Translation).count() > 0:
            print("Database already contains data. Skipping population.")
            return
        
        # Sample translations
        translations = [
            {
                "english_word": "love",
                "yoruba_word": "ifẹ́",
                "part_of_speech": "noun",
                "example_sentence": "I love you → Mo nífẹ́ rẹ"
            },
            {
                "english_word": "hello",
                "yoruba_word": "Ẹ káàbọ̀",
                "part_of_speech": "interjection",
                "example_sentence": "Hello, how are you? → Ẹ káàbọ̀, báwo ni?"
            },
            {
                "english_word": "thank you",
                "yoruba_word": "Ẹ ṣeun",
                "part_of_speech": "interjection",
                "example_sentence": "Thank you very much → Ẹ ṣeun púpọ̀"
            },
            {
                "english_word": "water",
                "yoruba_word": "omi",
                "part_of_speech": "noun",
                "example_sentence": "I need water → Mo nílò omi"
            },
            {
                "english_word": "food",
                "yoruba_word": "oúnjẹ",
                "part_of_speech": "noun",
                "example_sentence": "The food is delicious → Oúnjẹ yẹn dùn"
            },
            {
                "english_word": "family",
                "yoruba_word": "ìdílé",
                "part_of_speech": "noun",
                "example_sentence": "My family is large → Ìdílé mi tóbi"
            },
            {
                "english_word": "friend",
                "yoruba_word": "ọ̀rẹ́",
                "part_of_speech": "noun",
                "example_sentence": "He is my friend → Ó jẹ́ ọ̀rẹ́ mi"
            },
            {
                "english_word": "beautiful",
                "yoruba_word": "lẹ́wà",
                "part_of_speech": "adjective",
                "example_sentence": "She is beautiful → Ó lẹ́wà"
            },
            {
                "english_word": "good",
                "yoruba_word": "dára",
                "part_of_speech": "adjective",
                "example_sentence": "This is good → Èyí dára"
            },
            {
                "english_word": "bad",
                "yoruba_word": "búburú",
                "part_of_speech": "adjective",
                "example_sentence": "That is bad → Ìyẹn búburú"
            }
        ]
        
        # Sample proverbs
        proverbs = [
            {
                "yoruba_text": "Ìwà l'ẹ̀wà",
                "english_translation": "Character is beauty",
                "meaning": "A good character is more important than physical appearance.",
                "category": "character"
            },
            {
                "yoruba_text": "Ọmọdé kì í mọ ìgbà",
                "english_translation": "A child does not know time",
                "meaning": "Children are impatient and don't understand the concept of waiting.",
                "category": "patience"
            },
            {
                "yoruba_text": "Ìbà l'ọba",
                "english_translation": "Respect is king",
                "meaning": "Respect is the most important virtue and should be shown to all.",
                "category": "respect"
            },
            {
                "yoruba_text": "Ọ̀rọ̀ púpọ̀ ò ní ìdúró",
                "english_translation": "Many words cannot stand",
                "meaning": "Excessive talking often leads to problems or reveals secrets.",
                "category": "wisdom"
            },
            {
                "yoruba_text": "Ẹni tí kò bá gbọ́n, kò lè gbọ́n",
                "english_translation": "He who is not wise cannot be wise",
                "meaning": "Some people are naturally foolish and cannot be taught wisdom.",
                "category": "wisdom"
            }
        ]
        
        # Insert translations
        for trans_data in translations:
            translation = Translation(**trans_data)
            db.add(translation)
        
        # Insert proverbs
        for prov_data in proverbs:
            proverb = Proverb(**prov_data)
            db.add(proverb)
        
        db.commit()
        print(
            f"Successfully added {len(translations)} translations and "
            f"{len(proverbs)} proverbs."
        )
        
    except Exception as e:
        print(f"Error populating database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("Initializing Yoruba Language API Database...")
    init_database()
    print("Database initialization complete!")
