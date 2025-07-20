import openai 
def chat_with_gpt(prompt):
    #client = openai.OpenAI(api_key = "Use your key here " )
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content":prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Bot: ", response)
    

