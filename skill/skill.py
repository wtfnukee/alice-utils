import os
import wandb


def transliterate(text):
    """Convert English text to Cyrillic using basic transliteration rules."""
    mapping = {
        "a": "а",
        "b": "б",
        "c": "с",
        "d": "д",
        "e": "е",
        "f": "ф",
        "g": "г",
        "h": "х",
        "i": "и",
        "j": "дж",
        "k": "к",
        "l": "л",
        "m": "м",
        "n": "н",
        "o": "о",
        "p": "п",
        "r": "р",
        "s": "с",
        "t": "т",
        "u": "у",
        "v": "в",
        "w": "в",
        "x": "кс",
        "y": "й",
        "z": "з",
    }

    text = text.replace("_", " ")
    text = text.replace("accuracy", "аккураси")
    text = text.replace("loss", "лосс")
    text = text.replace("batch", "батч")
    text = text.replace("epoch", "эпох")
    text = text.replace("train", "трейн")
    text = text.replace("test", "тест")
    text = text.replace("val", "вал")

    text = text.lower()
    for eng, cyr in mapping.items():
        text = text.replace(eng, cyr)

    return text


def get_metrics():
    """Get metrics from the latest wandb run."""
    try:
        api = wandb.Api()
        entity = "kwargs"  # Replace with your own
        project = "model-inference-simulation"  # Replace with your own

        runs = api.runs(f"{entity}/{project}")
        if not runs:
            return "Не удалось найти запуски в Weights & Biases."

        latest_run = next(runs)
        metrics = latest_run.summary

        if not metrics:
            return "Не удалось найти метрики в последнем запуске."

        metric_texts = []
        for key, value in metrics.items():
            if isinstance(value, (int, float)) and not key.startswith("_"):
                cyrillic_key = transliterate(key)
                metric_texts.append(f"{cyrillic_key}: {str(round(value, 2))}")

        if not metric_texts:
            return "В последнем запуске нет числовых метрик."

        return "Метрики из последнего запуска:\n" + "\n".join(metric_texts)

    except Exception as e:
        return f"Произошла ошибка при получении метрик: {str(e)}"


def handler(event, context):
    """
    Entry-point for Serverless Function.
    :param event: request payload.
    :param context: information about current execution context.
    :return: response to be serialized as JSON.
    """
    text = "Привет! Я могу показать метрики из последнего запуска Weights & Biases. Просто скажите 'метрики'."

    if (
        "request" in event
        and "original_utterance" in event["request"]
        and event["request"]["original_utterance"].lower().strip() == "метрики"
    ):
        text = get_metrics()

    return {
        "version": event["version"],
        "session": event["session"],
        "response": {"text": text, "end_session": "false"},
    }
