"""Model configurations in json format"""


# "./" = root folder of the project
CFGLog = {
    "data": {
        "path": "./data/yelp.csv",
        "x": "text",
        "y": "stars",
        "test_size": 0.2,
        "random_state": 2022,
        "ngram_range": (1, 2),
        "min_df": 10

    },
    "train": {
            "solver": "liblinear",
            "max_iter": 1000,
            "random_state": 2022,
            "C": 0.01,
            "penalty": "l2",
    },
    "output": {
        "output_path": "../data/exported_models/",
        "model_name": "20230217_152148_LogReg.pickle",
    }
}