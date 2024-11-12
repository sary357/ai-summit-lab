# ai-summit-lab
- For AI summit held at 2024-12-11

# Prerequisite
## Poetry

```
$ curl -sSL https://install.python-poetry.org | python3 -
```

## install necessary python libraries
```
$ poetry add langchain openai langchain_community langchain-openai python-dotenv notebook fastapi  uvicorn
```

# Folder structure
```
├── README.md: Introduction
├── LLM: sample codes that generates AWS Lambda codes
└── serverless_framework_api: API codes that can receive request from sample codes and execute them

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

## serverless framework
### with root privileges
- install npm
```
$ yum install -y npm
```
- install serverless framework
```
$ npm i serverless -g
```
- update serverless framework
```
$ serverless update
```
