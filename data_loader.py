# #fine tuning
# from datasets import load_dataset
# from transformers import BartTokenizer
# import config

# tokenizer = BartTokenizer.from_pretrained(config.MODEL_NAME)

# def load_data():
#     dataset = load_dataset(config.DATASET_NAME, config.DATASET_VERSION)
#     return dataset

# def preprocess_function(examples):
#     inputs = examples["article"]
#     targets = examples["highlights"]

#     model_inputs = tokenizer(
#         inputs,
#         max_length=config.MAX_INPUT_LENGTH,
#         truncation=True,
#         padding="max_length"
#     )

#     labels = tokenizer(
#         targets,
#         max_length=config.MAX_TARGET_LENGTH,
#         truncation=True,
#         padding="max_length"
#     )

#     model_inputs["labels"] = labels["input_ids"]
#     return model_inputs

# def tokenize_data(dataset):
#     tokenized_dataset = dataset.map(preprocess_function, batched=True)
#     return tokenized_dataset