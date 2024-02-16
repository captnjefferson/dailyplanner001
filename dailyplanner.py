import openai

client = OpenAI(api_key="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")  # Replace 'YOUR_API_KEY' with your actual key

prompts = [
    "Ask the user to paste what tasks didn't get completed yesterday. Gently interrogate why those tasks weren't able to be completed.",
    "Ask the user to paste their five most important tasks for the day. Ask the user if they have one or two that are absolutely critical to complete.",
    "Please analyze the user's previous responses to provide a prioritized list of tasks. Consider tasks from yesterday that weren't completed and weigh the importance of today's tasks."  
]

def send_prompt_to_gpt4(prompt, temperature=0.7):
    global conversation_history
    conversation_history.append({"role": "system", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview", 
        messages=conversation_history,
        temperature=temperature,
    )
    response_text = response.choices[0].message.content.strip()
    conversation_history.append({"role": "user", "content": response_text})  
    return response_text

if __name__ == "__main__":
    start_review = input("Would you like to do a daily review? (yes/no): ")
    if start_review.lower() == "yes":
        current_step = 0
        conversation_history = []
        while current_step < len(prompts):
            prompt = prompts[current_step]
            gpt4_response = send_prompt_to_gpt4(prompt)
            print("Bot Response:", gpt4_response)
            user_input = input("User Input: ")  
            conversation_history.append({"role": "user", "content": user_input})
            current_step += 1
    else:
        print("Have a good day!")
