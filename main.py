from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("./Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("./Helsinki-NLP/opus-mt-zh-en")
text = "一个人"
batch = tokenizer.prepare_seq2seq_batch(src_texts=[text])
batch["input_ids"] = batch["input_ids"][:, :512]
translation = model.generate(**batch)
result = tokenizer.batch_decode(translation, skip_special_tokens=True)
print(result)