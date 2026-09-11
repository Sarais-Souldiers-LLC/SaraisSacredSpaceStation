from enum import Enum
from typing import Dict, Any, List


class StairStage(str, Enum):
    STRUCTURE = "structure"
    ASCENSION = "ascension"
    ROTATIONREFLECTION = "rotation/reflection"
    ALIGNMENT = "alignment"
    INTEGRATION = "integration"


class SaraiStaircaseEngine:
    """
    S.A.R.A.I. Staircase™
    Layered AI-driven decision-making and routine management system.
    """

    def __init__(self) -> None:
        self.current_stage: StairStage = StairStage.STRUCTURE
        self.history: List[Dict[str, Any]] = []

    def evaluate_input(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prototype decision layer.
        Later: plug in real cosmology logic + lineage rules.
        """
        score = payload.get("alignment_score", 0)
        lineage_weight = payload.get("lineage_weight", 1)

        composite = score * lineage_weight

        if composite < 20:
            self.current_stage = StairStage.STRUTURE
        elif composite < 40:
            self.current_stage = StairStage.ASCENSION
        elif composite < 60:
            self.current_stage = StairStage.ROTATIONREFLECTION
        elif composite < 80:
            self.current_stage = StairStage.ALIGNMENT
        else:
            self.current_stage = StairStage.INTEGRATION

        snapshot = {
            "input": payload,
            "composite_score": composite,
            "stage": self.current_stage.value,
        }
        self.history.append(snapshot)
        return snapshot

    def get_path(self) -> List[str]:
        """
        Returns symbolic staircase path.
        """
        return [
            "S¹: Structure",
            "A²: Ascension",
            "R³: Rotation/Reflection",
            "A⁴: Alignment",
            "I⁵: Integration",
        ]
