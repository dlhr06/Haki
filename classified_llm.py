from g4f.client import Client
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import pymupdf
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

def generate_dictionary(file_path: str, target_language: str = 'en', model: str = 'gpt-3') -> dict:
    
    language = languages.get(target_language)
    #pdf_text = read_pdf(file_path)
    
    pdf_text= ''

    doc = pymupdf.open(file_path)
    for page in doc: 
         pdf_text = page.get_text()
    
    prompt = f"""Generate a dictionary in Python format of the information in my Curriculum Vitae. The dictionary should have keys representing sections such as 'Personal Information', 'Education', 'Experience', 'Skills', etc. Please respond in {language}. Here is my Curriculum Vitae:
    
    {pdf_text}
    """
    response = client.chat.completions.create(
        model=models.get(model),
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    response_text = response.choices[0].message.content
    print(response_text)

    
    dictionary_start = response_text.find('dictionary: ') + len('dictionary: ')
    dictionary_text = response_text[dictionary_start:].strip()

    try:
        dictionary = eval(dictionary_text)
    except SyntaxError:
        dictionary = {}

    return dictionary 
    
#generate_dictionary(filecv)
#print(generate_dictionary)