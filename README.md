# BERTopic Reusable Pipeline

**Project:** [Project AWeSoMe](https://project-awesome.nl/)

**Authors:** Inga Vondenhof 

**Last updated:** May 2026

A modular BERTopic pipeline for large-scale social media text corpora. The pipeline is split across four notebooks that run in sequence, with a shared `config.py` for all file paths.

## Quickstart

```powershell
git clone https://github.com/ikv-awesome/BERTopicReusablePipeline.git
cd BERTopicReusablePipeline
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

Then place your CSV in `input/data/` and run the notebooks in order (see [Usage](#usage)).

## Requirements

### Environment setup
The pipeline requires Python 3.11.

**1. Create the virtual environment**

Open PowerShell in the BERTopic directory:
- Right click with your mouse
- Select "Open in Terminal"

Run:
```powershell
py -3.11 -m venv .venv
```

**2. Activate the environment**

```powershell
.venv\Scripts\activate
```

If you get a script execution error in PowerShell, run this first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**3. Upgrade pip**

```powershell
python -m pip install --upgrade pip
```

**4. Install PyTorch (GPU)**

```powershell
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121
```

> PyTorch must be installed separately before `requirements.txt` to ensure the correct CUDA 12.1 build is used. Installing it from PyPI will result in a CPU-only version.

**5. Install remaining dependencies**

```powershell
pip install -r requirements.txt
```

**6. Download required NLTK data**

```powershell
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"
```

**7. Register the environment as a Jupyter kernel**

```powershell
pip install ipykernel
python -m ipykernel install --user --name tiktok_env --display-name "Tiktok environment"
```

Then select **.venv** as the kernel in JupyterLab.

## Project structure

```
project/
│
├── config.py                        ← All file paths
├── requirements.txt                 ← Required Python packages
│
├── 1_data_preparation.ipynb         ← Creating documents for BERTopic
├── 2_embeddings_gridsearch.ipynb    ← Transformer model selection & hyperparameter grid search
├── 3_topic_modelling.ipynb          ← Topic modelling
├── 4_output_exploration.ipynb       ← Topic output evaluations
│
├── input/
│   ├── data/                        ← Place your input CSV here
│   └── documents/                   ← docs.pkl (created in notebook 1)
│
└── output/
    ├── embeddings/                  ← Files related to embeddings
    ├── checkpoint files/            ← Checkpoint files for stopping/reloading time-intensive steps
    ├── figures/                     ← Saved plots
    ├── topic info files/            ← Topic info tables (used for manual coding)
    └── topic model/                 ← Saved BERTopic model, topic assignments
```

## Usage

Run the notebooks in order:

1. **`1_data_preparation.ipynb`** — load your CSV and preprocess it into documents
2. **`2_embeddings_gridsearch.ipynb`** — generate embeddings and run hyperparameter grid search
3. **`3_topic_modelling.ipynb`** — fit the BERTopic model
4. **`4_output_exploration.ipynb`** — explore and evaluate the topic output

All file paths are managed centrally in `config.py` — you should not need to change paths inside the notebooks themselves.

## Adapting to your own data

**Minimum changes required to run on a new dataset:**

1. **Notebook 1**: change the text column name: `docs = input_df['your_column'].tolist()`
2. **Notebook 3**: adjust `DESIRED_TRAINING_SIZE` if your corpus is small (< 50 k documents, the pipeline handles this automatically but you may want to lower the value to speed things up)
3. **Notebook 3**: review the custom stopword list in `fit_bertopic`

**For small corpora (< 50 k documents):**  
All sample sizes and training sizes are capped automatically with `min(DESIRED_SIZE, len(docs))`, so no manual adjustments are needed. The full corpus will be used for both the grid search and model training.

**For non-English corpora:**  
The vectoriser in notebook 3 already includes Dutch, Spanish, French, and German stopwords alongside English. Add additional languages by extending the `languages` list in `fit_bertopic`.

---

## AI disclosure

AI tools were used to assist with developing, labelling, and debugging code, and with formatting Markdown cells.

Tools used: [CursorAI](https://cursor.com/agents), [Claude AI](https://claude.ai/), [ChatGPT](https://chatgpt.com/)

All outputs were verified by the authors. The authors accept full accountability for the accuracy and validity of this pipeline.
