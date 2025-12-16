## This file handles the logic behind the interactions with Jira API.
## ----------------------------------------------------------------
## IMPORTS
## ----------------------------------------------------------------
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline 
from transformers import BitsAndBytesConfig

## ----------------------------------------------------------------
## CLASS DEFINITIONS
## ----------------------------------------------------------------
class BugReport:
        def __init__(self, summary, description, error_logs):
            self.summary = summary
            self.description = description
            self.error_logs = error_logs

## ----------------------------------------------------------------
## COMPARISON - Sentence Similarity Logic
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## COMPARISON - Polarity Logic
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## COMPARISON - LLM Error logs Logic
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## COMPARISON - FINAL Decision Logic
## ----------------------------------------------------------------
def main():
    # Using Phi-3-mini model for bug report comparison
    model_name = "microsoft/Phi-3-mini-4k-instruct"

    input_prompt = "How many donuts in a baker's dozen?"

    # Initialize the model inputs
    prompt = [ 
        {"role": "user", "content": f"Task: {input_prompt}" },
        #{"role": "user", "content": f"FirstBug: {input_bug.summary}, {input_bug.description}, {input_bug.error_logs}"},
        #{"role": "user", "content": f"SecondBug: {compare_bug.summary}, {compare_bug.description}, {compare_bug.error_logs}"}
    ]

    generation_args = { 
        "max_new_tokens": 30, 
        "return_full_text": False, 
        "temperature": 0.5, 
        "do_sample": False, 
    } 

    # Running the model
    output_text = run_model(generation_args, model_name, prompt)
    print(output_text) 

# ------------ Helpers ------------
# Runs the model with input prompt and params.
def run_model(generation_args: dict[str, any], model_name: str, prompt: list[dict[str, str]]):
    # Initialize model and tokenizer with 4-bit quantization
    
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    
    model = initialize_model(model_name, bnb_config)
    tokenizer = AutoTokenizer.from_pretrained(model_name) 

    # Create text generation pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    # Generate output
    output = pipe(prompt, **generation_args)
    return output[0]['generated_text']

# Initializes and returns LLM
def initialize_model(model_name: str, bnb_config: BitsAndBytesConfig):
    # Set random seed for reproducibility
    torch.random.manual_seed(0)

    # Load the model using 4-bit quantization
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",  # Use "auto" to allow for better device management
        quantization_config=bnb_config,  # Pass the BitsAndBytesConfig for quantization
        trust_remote_code=True,
    )
    return model


if __name__ == "__main__":
    main()