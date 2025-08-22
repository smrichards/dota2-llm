#!/usr/bin/env python3
"""
Script to run inference with the trained Dota 2 model
Usage: python scripts/run_inference.py [--model PATH] [--question "Your question"]
"""

import argparse
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))
import config

def load_trained_model(model_path):
    """Load the fine-tuned model"""
    print(f"Loading base model: {config.MODEL_NAME}")
    
    # Load base model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    
    # Setup quantization for faster inference
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )
    
    base_model = AutoModelForCausalLM.from_pretrained(
        config.MODEL_NAME,
        quantization_config=bnb_config,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    
    print(f"Loading LoRA adapters from: {model_path}")
    # Load LoRA adapters
    model = PeftModel.from_pretrained(base_model, model_path)
    
    return model, tokenizer

def ask_question(model, tokenizer, question):
    """Ask the model a Dota 2 question"""
    # Add context to clarify Dota 2 terminology and focus
    if "bot lane" in question.lower():
        question = question.replace("bot lane", "safe lane carry position")
    elif "top lane" in question.lower():
        question = question.replace("top lane", "offlane position") 
    elif "mid lane" in question.lower():
        question = question.replace("mid lane", "mid position")
    
    # Format question using Mistral's instruction format with implicit Dota 2 context
    prompt = f"[INST] {question} (This is about Dota 2) [/INST]"
    
    # Tokenize
    inputs = tokenizer(
        prompt, 
        return_tensors="pt", 
        truncation=True,
        max_length=1024
    ).to(model.device)
    
    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            do_sample=True,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
            repetition_penalty=1.1
        )
    
    # Decode response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract just the model's response (after [/INST])
    if "[/INST]" in response:
        response = response.split("[/INST]")[-1].strip()
    
    return response

def main():
    parser = argparse.ArgumentParser(description="Run Dota 2 LLM inference")
    parser.add_argument("--model", type=str, 
                       default=str(config.MODELS_DIR / "mistral-nemo-dota2"),
                       help="Path to trained model directory")
    parser.add_argument("--question", type=str, 
                       help="Question to ask the model")
    
    args = parser.parse_args()
    
    # Load the trained model
    try:
        model, tokenizer = load_trained_model(args.model)
        print("✓ Model loaded successfully!")
    except Exception as e:
        print(f"✗ Failed to load model: {e}")
        return 1
    
    if args.question:
        # Single question mode
        print(f"\nQ: {args.question}")
        response = ask_question(model, tokenizer, args.question)
        print(f"A: {response}")
    else:
        # Interactive mode
        print("\n=== Dota 2 LLM Interactive Mode ===")
        print("Ask me anything about Dota 2! (type 'quit' to exit)")
        
        while True:
            try:
                question = input("\nQ: ").strip()
                
                if question.lower() in ['quit', 'exit', 'q']:
                    break
                    
                if not question:
                    continue
                    
                response = ask_question(model, tokenizer, question)
                print(f"A: {response}")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
    
    print("\nThanks for using the Dota 2 LLM!")
    return 0

if __name__ == "__main__":
    sys.exit(main())