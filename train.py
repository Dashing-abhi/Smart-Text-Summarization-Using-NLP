# #fine tuning
# from transformers import Trainer, TrainingArguments
# from data_loader import load_data, tokenize_data
# from model import load_model
# import config

# def train():
#     dataset = load_data()
#     tokenized_dataset = tokenize_data(dataset)

#     model = load_model()

#     training_args = TrainingArguments(
#         output_dir=config.OUTPUT_DIR,
#         learning_rate=config.LEARNING_RATE,
#         per_device_train_batch_size=config.TRAIN_BATCH_SIZE,
#         per_device_eval_batch_size=config.EVAL_BATCH_SIZE,
#         num_train_epochs=config.EPOCHS,
#         weight_decay=0.01,
#         eval_strategy="epoch",
#         save_strategy="epoch",
#         logging_dir="./logs",
#         save_total_limit=2,
#         fp16=True
#     )

#     trainer = Trainer(
#         model=model,
#         args=training_args,
#         train_dataset=tokenized_dataset["train"],
#         eval_dataset=tokenized_dataset["validation"]
#     )

#     trainer.train()
#     trainer.save_model(config.OUTPUT_DIR)

# if __name__ == "__main__":
#     train()