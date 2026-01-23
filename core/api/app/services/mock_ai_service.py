"""
Mock AI Translation Service for testing purposes.
Provides sample translations when OpenAI API is not available.
"""

from typing import Dict
import random


class MockAITranslationService:
    """Mock service that provides sample translations."""
    
    def __init__(self):
        # Sample translations for common words
        self.sample_translations = {
            "happiness": {
                "translation": "ayọ̀",
                "part_of_speech": "noun",
                "example": "Happiness is important → Ayọ̀ ṣe pàtàkì"
            },
            "wisdom": {
                "translation": "ọgbọ́n",
                "part_of_speech": "noun",
                "example": "Wisdom comes with age → Ọgbọ́n ńbọ̀ pẹ̀lú ọjọ́"
            },
            "courage": {
                "translation": "ìyà",
                "part_of_speech": "noun",
                "example": "He showed courage → Ó fi ìyà hàn"
            },
            "friendship": {
                "translation": "ìfẹ́ràn",
                "part_of_speech": "noun",
                "example": "Friendship is valuable → Ìfẹ́ràn ṣe pàtàkì"
            },
            "knowledge": {
                "translation": "ìmọ̀",
                "part_of_speech": "noun",
                "example": "Knowledge is power → Ìmọ̀ jẹ́ agbára"
            },
            "love": {
                "translation": "ifẹ́",
                "part_of_speech": "noun",
                "example": "I love you → Mo nífẹ́ rẹ"
            },
            "peace": {
                "translation": "àlàáfíà",
                "part_of_speech": "noun",
                "example": "Peace be with you → Àlàáfíà kí ó bà wá"
            },
            "hope": {
                "translation": "ìrètí",
                "part_of_speech": "noun",
                "example": "Never lose hope → Má ṣe padanu ìrètí"
            }
        }
    
    def translate_to_yoruba(self, english_text: str) -> Dict[str, any]:
        """Translate English text to Yoruba using mock data."""
        word = english_text.lower()
        
        if word in self.sample_translations:
            sample = self.sample_translations[word]
            return {
                "word": english_text,
                "translation": sample["translation"],
                "part_of_speech": sample["part_of_speech"],
                "example": sample["example"],
                "source": "mock_ai",
                "model": "mock-gpt-4o"
            }
        else:
            # Generate a mock translation for unknown words
            return self._generate_mock_translation(english_text)
    
    def _generate_mock_translation(self, english_text: str) -> Dict[str, any]:
        """Generate a mock translation for unknown words."""
        # Simple mock translation logic
        mock_translations = [
            f"ọmọ {english_text.lower()}",
            f"bàbá {english_text.lower()}",
            f"màmá {english_text.lower()}",
            f"ọ̀rẹ́ {english_text.lower()}"
        ]
        
        mock_parts = ["noun", "verb", "adjective", "adverb"]
        mock_examples = [
            f"I need {english_text} → Mo nílò {english_text}",
            f"This is {english_text} → Èyí jẹ́ {english_text}",
            f"Give me {english_text} → Fún mi ní {english_text}"
        ]
        
        return {
            "word": english_text,
            "translation": random.choice(mock_translations),
            "part_of_speech": random.choice(mock_parts),
            "example": random.choice(mock_examples),
            "source": "mock_ai",
            "model": "mock-gpt-4o"
        }
    
    def is_available(self) -> bool:
        """Mock service is always available."""
        return True


# Global instance
mock_ai_service = MockAITranslationService()


def translate_to_yoruba_mock(english_text: str) -> Dict[str, any]:
    """Convenience function for mock AI translation."""
    return mock_ai_service.translate_to_yoruba(english_text)


def is_mock_ai_available() -> bool:
    """Check if mock AI service is available."""
    return mock_ai_service.is_available()
