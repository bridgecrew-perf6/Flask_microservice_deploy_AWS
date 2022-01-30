from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer
from flask import Flask, request, render_template

def translate(text):
    model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)
    translated_text = translation(text, max_length=40)[0]['translation_text']
    return translated_text
    
@app.route('/')
def do_translate():
    return
    
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)