import json
import os
from typing import List
from pydantic import BaseModel, Field
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GhostPersona(BaseModel):
    persona_type: str = Field(description="The profile of the ghost persona.")
    queries: List[str] = Field(description="List of 10 high-context search queries.")
    entropy_score: float = Field(description="Calculated variance from real intent.")

class IntentInverter:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def generate_ghost_persona(self, real_intent: str) -> GhostPersona:
        prompt = f"""
        User Real Intent: "{real_intent}"
        Task: Create a 'Contrast Persona' that is the socio-economic opposite.
        Output: Return ONLY a JSON object with keys: persona_type, queries (list of 10), and entropy_score (0.8-1.0).
        """
        try:
            response = self.model.generate_content(prompt)
            clean_json = response.text.replace("```json", "").replace("```", "").strip()
            return GhostPersona(**json.loads(clean_json))
        except Exception as e:
            return GhostPersona(persona_type="Neutral", queries=["news", "weather"], entropy_score=0.5)
