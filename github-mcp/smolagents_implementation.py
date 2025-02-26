"""
Implementation of SmoLAgents from Hugging Face
https://huggingface.co/docs/transformers/main/en/sft_peft#small-language-agent-smolagent
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

class SmoLAgent:
    def __init__(self, model_name="HuggingFaceH4/zephyr-7b-beta"):
        """Initialize the SmoLAgent with a specified model."""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            torch_dtype=torch.float16, 
            device_map="auto"
        )
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=512
        )
        
    def generate_response(self, prompt, system_prompt=None):
        """Generate a response based on the prompt."""
        if system_prompt:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        else:
            messages = [{"role": "user", "content": prompt}]
            
        # Format messages for the model
        formatted_prompt = self.tokenizer.apply_chat_template(
            messages, 
            tokenize=False, 
            add_generation_prompt=True
        )
        
        # Generate response
        outputs = self.pipe(formatted_prompt)
        response = outputs[0]["generated_text"]
        
        # Extract just the assistant's response
        return response.split("assistant")[-1].strip()
    
    def run_tool(self, tool_name, **kwargs):
        """Execute a specific tool with the given parameters."""
        # This is where you would implement tool-specific logic
        if tool_name == "search":
            return f"Searching for: {kwargs.get('query', '')}"
        elif tool_name == "calculate":
            return f"Calculating: {kwargs.get('expression', '')}"
        else:
            return f"Unknown tool: {tool_name}"
    
    def plan_and_execute(self, user_request):
        """Plan a sequence of actions and execute them to fulfill a request."""
        # First, generate a plan
        planning_prompt = f"""
        User request: {user_request}
        
        Create a step-by-step plan to fulfill this request. 
        For each step, specify what tool to use (if any).
        """
        
        plan = self.generate_response(
            planning_prompt,
            system_prompt="You are a helpful assistant that creates detailed plans."
        )
        
        # Parse the plan and execute each step
        # This is a simplified implementation
        steps = plan.split("\n")
        results = []
        
        for step in steps:
            if "search" in step.lower():
                results.append(self.run_tool("search", query=user_request))
            elif "calculate" in step.lower():
                results.append(self.run_tool("calculate", expression="2+2"))
                
        # Generate final response based on results
        final_prompt = f"""
        User request: {user_request}
        
        Plan: {plan}
        
        Results: {results}
        
        Based on the above, provide a comprehensive response to the user.
        """
        
        return self.generate_response(
            final_prompt,
            system_prompt="You are a helpful assistant that provides thorough responses."
        )

# Example usage
if __name__ == "__main__":
    agent = SmoLAgent()
    response = agent.plan_and_execute("What is the capital of France and what's its population?")
    print(response)
