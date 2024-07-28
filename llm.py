from g4f.client import Client
# import asyncio
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

client = Client()
        
models = {
    'gpt-3': 'gpt-3.5-turbo',
    'gpt-4': 'gpt-4o'
}
languages = {
    'es': 'Spanish',
    'en': 'English',
    'fr': 'French'
}

def generate_summary(yaml_file:str, target_language:str='es', model:str = 'gpt-3') -> None:    
    language = languages.get(target_language)
    
    # Leer el archivo yaml
    with open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_data = f.read()
    
    # Ignorar la información personal
    yaml_data = "education:" + yaml_data.split('education:')[1]
        
    prompt = f"""Generate a professional summary based on the following information extracted from my Curriculum Vitae. Please respond in {language}. Please enter your response after the text 'summary:'. Here is the information from my Curriculum Vitae:
    {yaml_data}
    """    
    response = client.chat.completions.create(
        model=models.get(model),
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    
    print(response.choices[0].message.content)

# generate_summary('ejemplo_yaml.yaml',)

