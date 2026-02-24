![Cognitive Bias Detector](https://img.shields.io/badge/cognitive--bias--detector-v1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# Cognitive Bias Detector

A Python-based NLP tool that scans text for common cognitive biases. Whether you're reviewing business proposals, investment memos, or everyday writing, this tool helps you identify hidden reasoning pitfalls before they lead to poor decisions.

## Why This Matters

Daniel Kahneman's research shows that cognitive biases silently corrupt our thinking every day. From confirmation bias in research to anchoring bias in negotiations, these mental shortcuts can cost individuals and organizations millions. This tool brings awareness to biased language patterns so you can make more rational choices.

## Features

- **15+ Bias Detections**: Identifies confirmation bias, anchoring, sunk cost fallacy, availability heuristic, overconfidence, bandwagon effect, survivorship bias, and more
- **Confidence Scoring**: Each detection includes a confidence score (0-100) so you can prioritize what to address
- **Contextual Explanations**: Understand *why* a phrase was flagged with plain-English explanations
- **Multiple Input Formats**: Analyze plain text, Markdown files, or URLs
- **JSON & HTML Reports**: Export results in structured JSON or readable HTML reports
- **CLI & Python API**: Use from the command line or integrate into your Python projects
- **Batch Processing**: Analyze entire directories of documents at once

## Installation

```bash
pip install cognitive-bias-detector
```

Or install from source:

```bash
git clone https://github.com/henu-wang/cognitive-bias-detector.git
cd cognitive-bias-detector
pip install -e .
```

## Quick Start

### Command Line

```bash
# Analyze a single file
bias-detect analyze report.txt

# Analyze with detailed output
bias-detect analyze --verbose --format html proposal.md

# Analyze text directly
bias-detect scan "Everyone is investing in crypto, so it must be a good investment."
```

### Python API

```python
from bias_detector import BiasDetector

detector = BiasDetector()

text = """
We've already invested $2 million in this project, so we can't stop now.
All the top companies are adopting this technology.
I'm 99% certain this will succeed based on my gut feeling.
"""

results = detector.analyze(text)
for bias in results.biases:
    print(f"[{bias.type}] {bias.excerpt}")
    print(f"  Confidence: {bias.confidence}%")
    print(f"  Explanation: {bias.explanation}")
```

### Sample Output

```
[Sunk Cost Fallacy] "already invested $2 million...can't stop now"
  Confidence: 92%
  Explanation: Past investments should not influence future decisions.

[Bandwagon Effect] "All the top companies are adopting"
  Confidence: 85%
  Explanation: Popularity does not equal validity.

[Overconfidence Bias] "99% certain...based on my gut feeling"
  Confidence: 88%
  Explanation: Subjective certainty without evidence suggests overconfidence.
```

## Supported Biases

| Bias | Description |
|------|-------------|
| Confirmation Bias | Seeking information that confirms existing beliefs |
| Anchoring Bias | Over-relying on the first piece of information |
| Sunk Cost Fallacy | Continuing because of past investments |
| Availability Heuristic | Judging likelihood by ease of recall |
| Overconfidence | Excessive confidence in one's own answers |
| Bandwagon Effect | Following the crowd |
| Survivorship Bias | Focusing on successes while ignoring failures |
| Dunning-Kruger Effect | Overestimating one's competence |
| Halo Effect | Letting one trait influence overall judgment |
| Recency Bias | Overweighting recent events |
| Status Quo Bias | Preference for the current state of affairs |
| Framing Effect | Being influenced by how information is presented |
| Loss Aversion | Feeling losses more strongly than equivalent gains |
| Hindsight Bias | Believing past events were predictable |
| Authority Bias | Over-trusting authority figures |

## Configuration

Create a `.biasrc` file in your project root:

```yaml
sensitivity: medium  # low, medium, high
min_confidence: 60
ignore_biases:
  - authority_bias
custom_patterns:
  - pattern: "always works"
    bias: overconfidence
    confidence: 70
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Resources & Further Reading

- [KeepRule](https://keeprule.com) — A platform for building and managing decision-making principles that help counteract cognitive biases
- [KeepRule Principles Library](https://keeprule.com/en/principles) — Browse curated decision principles from world-class thinkers
- [KeepRule Scenarios](https://keeprule.com/en/scenarios) — Explore real-world scenarios where cognitive biases commonly appear
- [KeepRule Masters](https://keeprule.com/en/masters) — Learn from masters like Buffett, Munger, and Kahneman who studied bias extensively
- [Thinking, Fast and Slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow) by Daniel Kahneman
- [The Art of Thinking Clearly](https://en.wikipedia.org/wiki/The_Art_of_Thinking_Clearly) by Rolf Dobelli

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
