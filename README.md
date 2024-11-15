# ai-summit-lab (Part I)
- For AI summit held in 2025-02
- The codes are only about langchain to access OpenAI API and get codes back.

# Prerequisite
## Poetry

```
$ curl -sSL https://install.python-poetry.org | python3 -
```

## install necessary python libraries
```
$ poetry add langchain openai langchain_community langchain-openai python-dotenv notebook
```

## prepare open AI key
- Please be sure to have a file `.env` in this folder. Its content looks like
```
$ cat .env
OPENAI_API_KEY="sk-proj-m************************************i"
```

# Folder structure
```
├── README.md: Introduction
├── easy_sample.ipynb: sample codes that I tried to get codes from LLM.
├── IGNORE_ME.ipynb: please ignore this file
├── poetry.lock: for poetry 
└── pyproject.toml: for poetry
```


# References
## Use poetry shell
```
$ poetry shell
```

## Launch Jupyter
```
$ jupyter notebook --ip 0.0.0.0
```

