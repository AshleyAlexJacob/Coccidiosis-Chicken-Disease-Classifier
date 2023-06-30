# Coccidiosis (Chicken Disease) Classifier
End to End Coccidiosis ML Based classifier.

### Worflows

1. Update config.yaml (For paths and global settings)
2. Update secrets.yaml/.env [Optional]
3. Update params.yaml (For Model Params and Hyperparameters)
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml

### For Tensorboard Logs

Type in the terminal:

```
    tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir 
```

### Run Entire Workflow

```
    dvc init
```

```
    dvc repro
```

### Prediction Pipeline
```
    python app.py
```