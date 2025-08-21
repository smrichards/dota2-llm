"""Configuration settings for Dota 2 LLM training project"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
SRC_DIR = PROJECT_ROOT / "src"

# OpenDota API configuration
OPENDOTA_API_KEY = os.environ.get('OPENDOTA_API_KEY', None)
API_DELAY = float(os.environ.get('API_DELAY', '2.0'))  # Rate limiting delay
MIN_RANK = int(os.environ.get('MIN_RANK', '5'))  # 5=Ancient, 6=Divine, 7=Immortal

# Data collection settings
DEFAULT_NUM_MATCHES = int(os.environ.get('NUM_MATCHES', '500'))
MIN_ITEMS_PER_PLAYER = int(os.environ.get('MIN_ITEMS', '3'))
MIN_GPM_THRESHOLD = int(os.environ.get('MIN_GPM', '400'))

# Model training configuration
MODEL_NAME = os.environ.get('MODEL_NAME', "mistralai/Mistral-Nemo-Instruct-2407")
MAX_LENGTH = int(os.environ.get('MAX_LENGTH', '2048'))
LEARNING_RATE = float(os.environ.get('LEARNING_RATE', '2e-4'))
BATCH_SIZE = int(os.environ.get('BATCH_SIZE', '4'))
GRADIENT_ACCUMULATION_STEPS = int(os.environ.get('GRADIENT_ACCUMULATION_STEPS', '4'))
NUM_EPOCHS = int(os.environ.get('NUM_EPOCHS', '3'))
WARMUP_STEPS = int(os.environ.get('WARMUP_STEPS', '100'))

# LoRA configuration for efficient fine-tuning
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.1
LORA_TARGET_MODULES = ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

# Training data files
TRAINING_DATA_FILE = DATA_DIR / "dota2_training_data.jsonl"
HEROES_DATA_FILE = DATA_DIR / "heroes.json"
ITEMS_DATA_FILE = DATA_DIR / "items.json"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)