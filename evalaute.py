# #fine tuning
# import evaluate
# from transformers import pipeline

# rouge = evaluate.load("rouge")

# def evaluate_model(model_path):
#     summarizer = pipeline("summarization", model=model_path)

#     text = "Artificial Intelligence is transforming industries rapidly..."

#     summary = summarizer(text, max_length=100, min_length=30)

#     print("Summary:", summary[0]['summary_text'])