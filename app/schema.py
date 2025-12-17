from pydantic import BaseModel
from typing import Optional

class LaptopFeatures(BaseModel):
    company: str
    product: Optional[str] = "Unknown"
    typename: str
    inches: float
    screenresolution: str
    cpu_company: str
    cpu_type: str
    cpu_frequency_ghz: float
    ram_gb: int
    memory: str
    gpu_company: str
    gpu_type: str
    opsys: str
    weight_kg: float
