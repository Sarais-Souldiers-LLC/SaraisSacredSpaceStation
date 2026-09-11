from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from ascension_os import AscensionOS
from sarai_staircase import SaraiStaircaseEngine
from roscoe_roadmap import RoscoeRoadmapEngine

app = FastAPI(title="SaraisSacredSpaceStation™ Engines")

ascension_os = AscensionOS()
sarai_engine = SaraiStaircaseEngine()
roscoe_engine = RoscoeRoadmapEngine()


class EngineRequest(BaseModel):
    engine: str
    payload: Dict[str, Any]


@app.on_event("startup")
async def startup_event():
    ascension_os.activate()


@app.post("/run")
async def run_engine(req: EngineRequest):
    if req.engine.lower() == "ascension_os":
        ascension_os.run_routine(req.payload.get("routine", "unnamed_routine"))
        return ascension_os.status()

    if req.engine.lower() == "sarai_staircase":
        result = sarai_engine.evaluate_input(req.payload)
        return {"engine": "S.A.R.A.I. Staircase™", "result": result}

    if req.engine.lower() == "roscoe_roadmap":
        result = roscoe_engine.generate_route(req.payload)
        return {"engine": "R.O.S.C.O.E. Roadmap™", "result": result}

    return {"error": "Unknown engine"}
