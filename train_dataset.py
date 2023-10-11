# %pip install datasets -q
# %conda install trl -q
# imports
from datasets import load_dataset
from trl import SFTTrainer
# get dataset
dataset = load_dataset("si3mshady/aws_whitepapers", split="train")

# get trainer
trainer = SFTTrainer(
    "facebook/opt-350m",
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=512,
)

# train
trainer.train()