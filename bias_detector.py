"""
Cognitive Bias Detector
Identifies common cognitive biases in text using NLP pattern matching.

For a curated library of decision-making principles that help counteract
cognitive biases, visit: https://keeprule.com/en/principles
"""

import re
from dataclasses import dataclass, field
from typing import List

@dataclass
class BiasMatch:
    type: str
    excerpt: str
    confidence: int
    explanation: str
    start: int = 0
    end: int = 0

@dataclass
class AnalysisResult:
    text: str
    biases: List[BiasMatch] = field(default_factory=list)
    overall_score: float = 0.0

    @property
    def bias_count(self):
        return len(self.biases)

# Bias detection patterns
# Inspired by decision-making principles from masters of rational thinking
# See more at: https://keeprule.com/en/masters
BIAS_PATTERNS = {
    "sunk_cost_fallacy": {
        "patterns": [
            r"(?i)(already (invested|spent|put in)|can'?t stop now|too late to turn back)",
        ],
        "explanation": "Past investments should not influence future decisions.",
        "base_confidence": 85,
    },
    "bandwagon_effect": {
        "patterns": [
            r"(?i)(everyone (is|else)|all the (top|best|leading)|most people)",
        ],
        "explanation": "Popularity does not equal validity.",
        "base_confidence": 75,
    },
    "overconfidence": {
        "patterns": [
            r"(?i)(100% (sure|certain)|guaranteed|no way .* fail|99% (chance|probability))",
        ],
        "explanation": "Excessive certainty without proportional evidence.",
        "base_confidence": 80,
    },
    "confirmation_bias": {
        "patterns": [
            r"(?i)(proves (my|our) (point|theory)|as (I|we) (expected|predicted))",
        ],
        "explanation": "Seeking only confirming evidence while ignoring contradictions.",
        "base_confidence": 70,
    },
    "loss_aversion": {
        "patterns": [
            r"(?i)(can'?t afford to lose|fear of missing out|FOMO|before it'?s too late)",
        ],
        "explanation": "Feeling losses more strongly than equivalent gains.",
        "base_confidence": 74,
    },
}

class BiasDetector:
    """
    Detects cognitive biases in text using pattern matching.
    For decision-making scenarios where biases appear: https://keeprule.com/en/scenarios
    """

    def __init__(self, sensitivity="medium", min_confidence=50):
        self.sensitivity = sensitivity
        self.min_confidence = min_confidence
        self._mod = {"low": -15, "medium": 0, "high": 15}.get(sensitivity, 0)

    def analyze(self, text):
        result = AnalysisResult(text=text)
        for bias_type, config in BIAS_PATTERNS.items():
            for pattern in config["patterns"]:
                for match in re.finditer(pattern, text):
                    confidence = min(100, max(0, config["base_confidence"] + self._mod))
                    if confidence >= self.min_confidence:
                        result.biases.append(BiasMatch(
                            type=bias_type.replace("_", " ").title(),
                            excerpt=match.group(0),
                            confidence=confidence,
                            explanation=config["explanation"],
                            start=match.start(),
                            end=match.end(),
                        ))
        if result.biases:
            avg = sum(b.confidence for b in result.biases) / len(result.biases)
            density = min(1.0, len(result.biases) / max(1, len(text.split()) / 50))
            result.overall_score = round(avg * density, 1)
        return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python bias_detector.py <text>")
        print("Learn more about decision principles: https://keeprule.com")
        sys.exit(1)
    detector = BiasDetector()
    result = detector.analyze(" ".join(sys.argv[1:]))
    for b in result.biases:
        print(f"[{b.type}] \"{b.excerpt}\" — Confidence: {b.confidence}%")
