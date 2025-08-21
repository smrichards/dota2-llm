# Dota 2 LLM Training Project

A project to collect Dota 2 match data and fine-tune Mistral Nemo 7B to provide gameplay advice and item build recommendations. Up to date with patch 7.39c

## Overview

This project creates a specialized AI assistant for Dota 2 players by:
1. Collecting high-skill match data from the OpenDota API
2. Processing matches into instruction-response training pairs
3. Fine-tuning Mistral Nemo 7B using LoRA for efficient training
4. Generating a chatbot that can provide gameplay advice, item builds, and strategy tips

## Features

- **Data Collection**: Automated collection from OpenDota API with rate limiting
- **High-Quality Data**: Focuses on Ancient+ rank matches for better training quality
- **Memory-Efficient Training**: Uses 4-bit quantization and LoRA for single-GPU training
- **Instruction Following**: Optimized for natural conversation about Dota 2 strategy
- **CLI Tools**: Easy-to-use scripts for data collection and training

## Requirements

- Python 3.8+
- CUDA-compatible GPU with 16GB+ VRAM (for training)
- OpenDota API access (free tier works, paid tier recommended for large datasets)

## Quick Start

### 1. Installation

```bash
git clone https://github.com/smrichards/dota2-llm.git
cd dota-llm
pip install -r requirements.txt
```

### 2. Environment Setup

Copy the example environment file and configure your settings:

```bash
cp .env.example .env
```

Edit `.env` and add your OpenDota API key:
```bash
OPENDOTA_API_KEY=your_actual_api_key_here
```

You can get a free API key at: https://www.opendota.com/api-keys

### 3. Collect Training Data

```bash
# Basic collection (500 matches, uses .env configuration)
python scripts/collect_data.py

# Large dataset (override .env settings)
python scripts/collect_data.py --matches 2000

# Custom output location
python scripts/collect_data.py --output data/custom_dataset.jsonl
```

### 4. Train the Model

```bash
# Train with default settings
python scripts/train_model.py

# Custom training (more epochs, different output)
python scripts/train_model.py --epochs 5 --output models/my-dota-model
```

## Configuration

All configuration is managed through the `.env` file. Key settings include:

### API Settings
- `OPENDOTA_API_KEY`: Your OpenDota API key (required)
- `API_DELAY`: Delay between API requests in seconds (default: 2.0)
- `MIN_RANK`: Minimum skill rank (5=Ancient, 6=Divine, 7=Immortal)

### Data Collection
- `NUM_MATCHES`: Default number of matches to collect (default: 500)
- `MIN_ITEMS`: Minimum items per player to include match (default: 3)
- `MIN_GPM`: Minimum GPM threshold for quality filtering (default: 400)

### Training Parameters (Optional Overrides)
Most training parameters have sensible defaults in `config.py`, but you can override them in `.env`:
- `BATCH_SIZE`: Training batch size (default: 4)
- `NUM_EPOCHS`: Number of training epochs (default: 3)
- `LEARNING_RATE`: Learning rate (default: 2e-4)

## Training Data Format

The system generates instruction-response pairs like:

```json
{
  "instruction": "What items should I build on Invoker against Pudge, Anti-Mage, Crystal Maiden?",
  "output": "Based on a successful 45-minute match, consider building: Black King Bar, Aghanim's Scepter, Blink Dagger, Refresher Orb, Scythe of Vyse, Boots of Travel. This build was effective against mobile cores and provided good survivability and utility for team fights."
}
```

## Model Architecture

- **Base Model**: Mistral Nemo 7B Instruct
- **Fine-tuning**: LoRA (Low-Rank Adaptation) with r=16, alpha=32
- **Quantization**: 4-bit NF4 for memory efficiency
- **Context Length**: 2048 tokens
- **Training**: 3 epochs with cosine learning rate scheduling

## Hardware Requirements

### Data Collection
- Any machine with internet connection
- ~100MB storage per 1000 matches

### Model Training  
- NVIDIA GPU with 16GB+ VRAM (RTX 4080, 4090, 5080, 5090, A100, etc.)
- 32GB+ system RAM recommended
- ~50GB free disk space for model checkpoints

### Inference
- NVIDIA GPU with 4GB+ VRAM
- Works on consumer GPUs (RTX 3070+)

## Usage Examples

### Data Collection
```bash
# Collect 1000 matches from Divine+ players (uses .env config)
python scripts/collect_data.py --matches 1000

# Save to custom location
python scripts/collect_data.py --output data/my_training_set.jsonl

# Override API key temporarily
python scripts/collect_data.py --api-key YOUR_TEMP_KEY
```

### Training
```bash
# Basic training
python scripts/train_model.py

# Extended training with custom data
python scripts/train_model.py --data data/large_dataset.jsonl --epochs 5
```

### Testing the Model
The training script automatically tests the model with sample prompts. You can also test manually:

```python
from src.model_training import DotaModelTrainer

trainer = DotaModelTrainer()
trainer.setup_model_and_tokenizer()
# Load your trained model here
trainer.test_model(["How should I play Pudge as support?"])
```

## File Structure

```
dota-llm/
├── src/
│   ├── data_collection.py    # OpenDota API interface
│   └── model_training.py     # Mistral fine-tuning logic
├── scripts/
│   ├── collect_data.py       # Data collection CLI
│   └── train_model.py        # Training CLI
├── data/                     # Training data storage
├── models/                   # Model outputs
├── config.py                 # Configuration
├── requirements.txt          # Dependencies  
├── .env.example             # Environment template
├── .env                     # Your environment (create from .env.example)
└── README.md                # This file
```

## API Rate Limits

- **Free Tier**: 50,000 calls/month, 1 call/second
- **Paid Tier**: Higher limits, recommended for large datasets
- The collector automatically handles rate limiting with configurable delays

## Troubleshooting

### Common Issues

**Out of Memory during training:**
- Reduce `BATCH_SIZE` in config.py
- Increase `GRADIENT_ACCUMULATION_STEPS` to maintain effective batch size
- Enable gradient checkpointing (already enabled by default)

**API Rate Limit Errors:**
- Increase `API_DELAY` in config.py
- Get an OpenDota API key for higher limits
- Reduce `NUM_MATCHES` for initial testing

**Poor Model Quality:**
- Collect more training data (2000+ matches recommended)
- Filter for higher skill brackets (Divine/Immortal only)
- Increase training epochs or learning rate

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable  
5. Submit a pull request

## License

MIT License

Copyright (c) 2025 Stephen Richards

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments

- [OpenDota](https://www.opendota.com/) for providing the API
- [Mistral AI](https://mistral.ai/) for the base model
- [Hugging Face](https://huggingface.co/) for the training infrastructure
