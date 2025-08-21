"""
Mistral Nemo 7B fine-tuning for Dota 2 gameplay advice
"""

import json
import torch
from pathlib import Path
from datasets import Dataset
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM, 
    TrainingArguments,
    BitsAndBytesConfig
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
import config

class DotaModelTrainer:
    def __init__(self, model_name=config.MODEL_NAME):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        
    def setup_model_and_tokenizer(self):
        """Initialize tokenizer and model with quantization"""
        print(f"Loading tokenizer and model: {self.model_name}")
        
        # Setup tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"
        
        # Setup quantization config for memory efficiency
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )
        
        # Load model with quantization
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=bnb_config,
            device_map="auto",
            torch_dtype=torch.float16,
            # attn_implementation="flash_attention_2" if torch.cuda.is_available() else None
        )
        
        # Prepare model for k-bit training
        self.model = prepare_model_for_kbit_training(self.model)
        
    def setup_lora(self):
        """Setup LoRA configuration"""
        lora_config = LoraConfig(
            r=config.LORA_R,
            lora_alpha=config.LORA_ALPHA,
            target_modules=config.LORA_TARGET_MODULES,
            lora_dropout=config.LORA_DROPOUT,
            bias="none",
            task_type="CAUSAL_LM",
        )
        
        self.model = get_peft_model(self.model, lora_config)
        
    def load_training_data(self, data_path=config.TRAINING_DATA_FILE):
        """Load and prepare training data"""
        print(f"Loading training data from {data_path}")
        
        training_examples = []
        with open(data_path, 'r', encoding='utf-8') as f:
            for line in f:
                example = json.loads(line.strip())
                training_examples.append(example)
        
        print(f"Loaded {len(training_examples)} training examples")
        return training_examples
    
    def format_training_example(self, example):
        """Format training example for instruction following"""
        instruction = example['instruction']
        output = example['output']
        
        # Use Mistral's instruction format
        formatted_text = f"[INST] {instruction} [/INST] {output}"
        return {"text": formatted_text}
    
    def prepare_dataset(self, training_examples):
        """Convert training examples to HuggingFace dataset"""
        formatted_examples = [self.format_training_example(ex) for ex in training_examples]
        dataset = Dataset.from_list(formatted_examples)
        
        print(f"Created dataset with {len(dataset)} examples")
        return dataset
    
    def train_model(self, dataset, output_dir=None):
        """Train the model using SFTTrainer"""
        if output_dir is None:
            output_dir = config.MODELS_DIR / "mistral-nemo-dota2"
        
        # Training arguments
        training_args = TrainingArguments(
            output_dir=str(output_dir),
            num_train_epochs=config.NUM_EPOCHS,
            per_device_train_batch_size=config.BATCH_SIZE,
            gradient_accumulation_steps=config.GRADIENT_ACCUMULATION_STEPS,
            learning_rate=config.LEARNING_RATE,
            warmup_steps=config.WARMUP_STEPS,
            logging_steps=10,
            save_steps=100,
            save_total_limit=2,
            prediction_loss_only=True,
            remove_unused_columns=False,
            push_to_hub=False,
            report_to=["wandb"] if "wandb" in locals() else [],
            optim="paged_adamw_8bit",
            lr_scheduler_type="cosine",
            gradient_checkpointing=True,
        )
        
        # Initialize trainer
        trainer = SFTTrainer(
            model=self.model,
            train_dataset=dataset,
            tokenizer=self.tokenizer,
            args=training_args,
            max_seq_length=config.MAX_LENGTH,
            dataset_text_field="text",
            packing=False,
        )
        
        print("Starting training...")
        trainer.train()
        
        # Save the final model
        print(f"Saving model to {output_dir}")
        trainer.save_model()
        self.tokenizer.save_pretrained(output_dir)
        
        return trainer
    
    def test_model(self, test_prompts=None):
        """Test the trained model with sample prompts"""
        if test_prompts is None:
            test_prompts = [
                "What items should I build on Invoker against Pudge, Anti-Mage, Crystal Maiden?",
                "How do I play Pudge effectively?",
                "What's the best strategy for playing support in Dota 2?"
            ]
        
        print("\n=== Testing Model ===")
        for prompt in test_prompts:
            formatted_prompt = f"[INST] {prompt} [/INST]"
            
            inputs = self.tokenizer(
                formatted_prompt, 
                return_tensors="pt", 
                truncation=True,
                max_length=config.MAX_LENGTH
            ).to(self.model.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=256,
                    temperature=0.7,
                    do_sample=True,
                    top_p=0.9,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Extract just the response part
            response = response.split("[/INST]")[-1].strip()
            
            print(f"\nQ: {prompt}")
            print(f"A: {response}")

def main():
    """Main training pipeline"""
    print("=== Dota 2 Model Training ===")
    
    # Initialize trainer
    trainer = DotaModelTrainer()
    
    # Setup model and tokenizer
    trainer.setup_model_and_tokenizer()
    trainer.setup_lora()
    
    # Load and prepare data
    training_examples = trainer.load_training_data()
    dataset = trainer.prepare_dataset(training_examples)
    
    # Train the model
    trained_model = trainer.train_model(dataset)
    
    # Test the model
    trainer.test_model()
    
    print("\n=== Training Complete ===")
    print("Model saved to models/mistral-nemo-dota2/")

if __name__ == "__main__":
    main()