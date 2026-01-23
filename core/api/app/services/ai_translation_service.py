"""
AI Translation Service for Yoruba Language API.
Uses OpenAI GPT models to provide context-aware translations.
"""

import json
import logging
from typing import Dict
from openai import OpenAI
from app.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AITranslationService:
    """Service for AI-powered translations using OpenAI."""
    
    def __init__(self):
        self.client = None
        self.model = settings.ai_model
        
        if settings.openai_api_key:
            self.client = OpenAI(api_key=settings.openai_api_key)
            logger.info(
                f"AI Translation Service initialized with model: {self.model}"
            )
        else:
            logger.warning(
                "OpenAI API key not found. AI translations will not work."
            )
    
    def translate_to_yoruba(self, english_text: str) -> Dict[str, any]:
        """Translate English text to Yoruba using AI."""
        if not self.client:
            raise ValueError("OpenAI client not initialized. Check API key.")
        
        try:
            prompt = self._create_translation_prompt(english_text)
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Yoruba language expert and translator."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            ai_response = response.choices[0].message.content
            return self._parse_ai_response(ai_response, english_text)
            
        except Exception as e:
            logger.error(f"AI translation failed: {str(e)}")
            raise Exception(f"AI translation failed: {str(e)}")
    
    def _create_translation_prompt(self, english_text: str) -> str:
        """Create a structured prompt for the AI translation."""
        return f"""Translate "{english_text}" from English to Yoruba.
Respond in this JSON format:
{{
  "word": "{english_text}",
  "translation": "yoruba_translation_with_tones",
  "part_of_speech": "noun/verb/adjective",
  "example": "English example → Yoruba example"
}}"""
    
    def _parse_ai_response(
        self, ai_response: str, original_text: str
    ) -> Dict[str, any]:
        """Parse the AI response and extract translation data."""
        try:
            json_start = ai_response.find('{')
            json_end = ai_response.rfind('}') + 1
            
            if json_start != -1 and json_end != 0:
                json_str = ai_response[json_start:json_end]
                data = json.loads(json_str)
                data['source'] = 'ai'
                data['model'] = self.model
                return data
            else:
                return self._create_fallback_response(original_text)
                
        except json.JSONDecodeError:
            return self._create_fallback_response(original_text)
    
    def _create_fallback_response(self, original_text: str) -> Dict[str, any]:
        """Create a fallback response when AI parsing fails."""
        return {
            'word': original_text,
            'translation': original_text,
            'part_of_speech': 'noun',
            'example': f"I need {original_text}",
            'source': 'ai_fallback',
            'model': self.model
        }
    
    def is_available(self) -> bool:
        """Check if AI translation service is available."""
        return self.client is not None


# Global instance
ai_translation_service = AITranslationService()


def translate_to_yoruba(english_text: str) -> Dict[str, any]:
    """Convenience function to translate English to Yoruba."""
    return ai_translation_service.translate_to_yoruba(english_text)


def is_ai_available() -> bool:
    """Check if AI translation is available."""
    return ai_translation_service.is_available()
