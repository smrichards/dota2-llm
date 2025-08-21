#!/usr/bin/env python3
"""
Script to train Mistral Nemo 7B on Dota 2 data
Usage: python scripts/train_model.py [--data PATH] [--output PATH]
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from model_training import DotaModelTrainer
import config

def main():
    parser = argparse.ArgumentParser(description="Train Dota 2 LLM")
    parser.add_argument("--data", type=str, default=str(config.TRAINING_DATA_FILE),
                       help="Path to training data file")
    parser.add_argument("--output", type=str, default=str(config.MODELS_DIR / "mistral-nemo-dota2"),
                       help="Output directory for trained model")
    parser.add_argument("--model", type=str, default=config.MODEL_NAME,
                       help="Base model to fine-tune")
    parser.add_argument("--epochs", type=int, default=config.NUM_EPOCHS,
                       help="Number of training epochs")
    
    args = parser.parse_args()
    
    # Check if training data exists
    if not Path(args.data).exists():
        print(f"Error: Training data not found at {args.data}")
        print("Run data collection first: python scripts/collect_data.py")
        return 1
    
    print("=== Dota 2 Model Training ===")
    print(f"Training data: {args.data}")
    print(f"Base model: {args.model}")
    print(f"Output directory: {args.output}")
    print(f"Epochs: {args.epochs}")
    
    # Update config if needed
    if args.epochs != config.NUM_EPOCHS:
        config.NUM_EPOCHS = args.epochs
    
    # Initialize trainer
    trainer = DotaModelTrainer(model_name=args.model)
    
    # Setup model and tokenizer
    print("\nSetting up model and tokenizer...")
    trainer.setup_model_and_tokenizer()
    trainer.setup_lora()
    
    # Load and prepare data
    print("\nLoading training data...")
    training_examples = trainer.load_training_data(args.data)
    dataset = trainer.prepare_dataset(training_examples)
    
    # Train the model
    print("\nStarting training...")
    trained_model = trainer.train_model(dataset, args.output)
    
    # Test the model
    print("\nTesting trained model...")
    trainer.test_model()
    
    print(f"\n=== Training Complete ===")
    print(f"Model saved to {args.output}")
    return 0

if __name__ == "__main__":
    sys.exit(main())