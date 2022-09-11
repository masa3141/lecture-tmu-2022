from abc import ABC, abstractmethod
import json
from typing import Any

from app.models.predict import RecommendedItem


class BaseMLModel(ABC):
    @abstractmethod
    def predict(self, req: Any) -> Any:
        raise NotImplementedError


class MLModel(BaseMLModel):
    """Sample ML model"""

    def __init__(self, model_path: str) -> None:
        self.model_path = model_path
        with open(model_path, "r") as f:
            self.model = json.load(f)

    def predict(self, item_id: str, topn=3) -> list[RecommendedItem]:
        results = []
        if item_id in self.model:
            results = [
                RecommendedItem(
                    item_id=item["item_id"], item_name=item["item_name"], score=item["score"], rank=item["rank"]
                )
                for item in self.model[item_id][0:topn]
            ]
        return results
