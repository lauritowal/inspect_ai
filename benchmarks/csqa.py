"""
CommonSenseQA (CSQA): A Question Answering Challenge Targeting Commonsense Knowledge

Alon Talmor, Jonathan Herzig, Nicholas Lourie, Jonathan Berant
https://arxiv.org/pdf/1811.00937v2

# eval w/ 500 randomly selected samples
inspect eval csqa.py --limit 500
"""

from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.dataset._sources.hf import hf_dataset
from inspect_ai.scorer import choice
from inspect_ai.solver import multiple_choice


def record_to_sample(record):
    return Sample(
        input=record["question"],
        choices=[
            str(record["choices"]["text"][0]),
            str(record["choices"]["text"][1]),
            str(record["choices"]["text"][2]),
            str(record["choices"]["text"][3]),
            str(record["choices"]["text"][4]),
        ],
        target=record["answerKey"],
        metadata={"question_concept": record["question_concept"]},
    )

@task
def csqa():
    dataset = hf_dataset(
        path="tau/commonsense_qa",
        split="validation",
        sample_fields=record_to_sample,
        trust=True,
        shuffle=True,
    )
    
    return Task(
        dataset=dataset,
        plan=multiple_choice(),
        scorer=choice(),
    )
