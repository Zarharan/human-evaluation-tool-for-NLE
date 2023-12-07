from .models import *
from .forms import *
from .utils import *
import pandas as pd
import numpy as np
import os
from django.conf import settings


def import_data():

    args= {"target_path": "data/explanation/llj.csv", "seed": 14, "target_instance_no": 50}

    target_file_df= pd.read_csv( os.path.join(settings.BASE_DIR, "evaluation/"+args["target_path"]))
    target_file_df= target_file_df.dropna()
    np.random.seed(args["seed"])
    target_file_df= target_file_df.sample(n=args["target_instance_no"], random_state= args["seed"], weights = target_file_df.groupby('label')['label'].transform('count'))    

    explanation_col_title= ""
    for name in ["gpt3", "chat_gpt", "gpt4", "vicuna", "mistral", "falcon", "llama"]:
        if name in args["target_path"]:
            if "explanation" in args["target_path"]:
                explanation_col_title= name
                if name in ["vicuna", "mistral", "falcon", "llama"]:
                    explanation_col_title+= "_cleaned"
            elif "joint" in args["target_path"]:
                explanation_col_title= name+ "_explanation"
            break

    for idx, row in target_file_df.iterrows():
        target_instance= Instance.objects.create(claim_id = row["claim_id"], claim = row["claim"], context = row["summarized_main_text"]
        ,explanation = row[explanation_col_title], tag = args["target_path"])
        target_instance.save()