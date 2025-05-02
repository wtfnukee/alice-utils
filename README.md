# Alice WandB Metrics Skill

Voice assistant skill that fetches metrics from your latest Weights & Biases run.


## Setup

1. Clone this repository:
```bash
git clone github.com/wtfnukee/alice-util
cd alice-util
```
2. Set `WANDB_API_KEY` in .env.example
3. Update in `skill/skill.py`:
```python
entity = "your_username"
project = "your_project"
```


## Deployment

[Follow tutorial here](https://yandex.cloud/ru/docs/tutorials/serverless/alice-skill)


## Usage

1. "Алиса, запусти навык"
2. "метрики"

Example:
```
Метрики из последнего запуска:
батч аккураси: 0.95
трейн лосс: 0.12
```