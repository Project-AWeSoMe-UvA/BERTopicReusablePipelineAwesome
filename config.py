"""Configuration file for BERTopic project"""
from pathlib import Path

# Project root (always the directory this file lives in)
PROJECT_ROOT = Path(__file__).resolve().parent

# =============================================================================
# DIRECTORIES
# =============================================================================
INPUT_DIR             = PROJECT_ROOT / "input"
DATA_PREP_DIR         = INPUT_DIR / "data"
DOCUMENTS_DIR         = INPUT_DIR / "documents"                

OUTPUT_DIR            = PROJECT_ROOT / "output"
EMBEDDINGS_DIR        = OUTPUT_DIR / "embeddings"
CHECKPOINT_DIR        = OUTPUT_DIR / "checkpoint files"
FIGURES_DIR           = OUTPUT_DIR / "figures"
TOPIC_INFO_DIR        = OUTPUT_DIR / "topic info files"
TOPIC_MODEL_DIR       = OUTPUT_DIR / "topic model"


# ============================================================================
# DOCUMENTS, EMBEDDINGS & GRIDSEARCH
# =============================================================================
PREPROCESSED_DOCS_PATH     = DOCUMENTS_DIR / "docs.pkl"

EMBEDDINGS_PATH            = EMBEDDINGS_DIR / "final_embeddings.npy"
EMBED_TEST_PATH            = EMBEDDINGS_DIR / "embed_test_results.pkl"

SAMPLE_SENSITIVITY_PATH    = CHECKPOINT_DIR / "sample_sensitivity_results.csv"
CHECKPOINT_PATH_GRIDSEARCH = CHECKPOINT_DIR / "bertopic_gridsearch_checkpoint.pkl"
FINAL_CSV_PATH_GRIDSEARCH  = CHECKPOINT_DIR / "bertopic_gridsearch_results.csv"
BEST_PARAMS_PATH           = CHECKPOINT_DIR / "best_params.json" 

# =============================================================================
# TOPIC MODEL
# =============================================================================
TOPIC_MODEL_PATH            = TOPIC_MODEL_DIR / "topic_model_final"
TOPICS_ASSIGNED_PATH        = TOPIC_MODEL_DIR / "topics_final.npy"
TOPIC_MODEL_RESULTS_PATH    = TOPIC_MODEL_DIR / "bertopic_results_final.csv.gz"

TOPIC_INFO_PATH             = TOPIC_INFO_DIR  / "topic_info.csv"
LABELLED_INFO_PATH          = TOPIC_INFO_DIR  / "topic_info_labelled.xlsx"