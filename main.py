from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer

def translate(text):
    model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
    translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)
    translated_text = translation(text, max_length=40)[0]['translation_text']
    return translated_text