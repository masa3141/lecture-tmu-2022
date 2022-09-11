from pydantic import BaseModel, Field


class RecommendedItem(BaseModel):
    item_id: str
    item_name: str
    score: float
    rank: int


class PredictRequest(BaseModel):
    item_id: str = Field(..., title="input_item_id", description="Input item_id", example="item1")


class PredictResponse(BaseModel):
    results: list[RecommendedItem] = Field(
        ...,
        title="result",
        description="Predict value",
        example=[RecommendedItem(item_id="item1", item_name="item1 name", score=0.9, rank=1)],
    )
