# from transformers import BartTokenizer , BartForConditionalGeneration
# model_name = "facebook/bart-base"
# tokenizer = BartTokenizer.from_pretrained(model_name)

# model = BartForConditionalGeneration.from_pretrained(model_name)

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
# model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

from transformers import BartForConditionalGeneration,BartTokenizer
import config
tokenizer = BartTokenizer.from_pretrained(config.MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(config.MODEL_NAME)

def load_model():
    return model

def get_summarizer():
    return {"tokenizer": tokenizer, "model": model}