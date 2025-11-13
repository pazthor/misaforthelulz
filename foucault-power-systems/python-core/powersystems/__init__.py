"""
Foucault Power Systems Framework

A Python implementation for analyzing power systems through Foucauldian concepts:
- Power as productive (not just repressive)
- Power as relational and circulating
- Disciplinary mechanisms and surveillance
- Power/knowledge relationships
- Biopower and governmentality
"""

from .core import (
    PowerSystem,
    Privilege,
    PrivilegeScope,
    ReachEstimation,
    PowerRelation,
    PowerDirection,
    DisciplinaryMechanism
)

from .analyzer import PowerSystemAnalyzer, SystemAnalysis

__version__ = "1.0.0"
__all__ = [
    "PowerSystem",
    "Privilege",
    "PrivilegeScope",
    "ReachEstimation",
    "PowerRelation",
    "PowerDirection",
    "DisciplinaryMechanism",
    "PowerSystemAnalyzer",
    "SystemAnalysis"
]
