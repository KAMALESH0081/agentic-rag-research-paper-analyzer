from pydantic import BaseModel
from typing import List, Optional

class ExtractionResult(BaseModel):
    datasets_used: Optional[List[str]]
    benchmark_dataset: Optional[List[str]]
    evaluation_metric: Optional[List[str]]
    method: Optional[List[str]]