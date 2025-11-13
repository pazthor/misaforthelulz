"""
Example Power Systems

Collection of Foucauldian power system implementations.
"""

from .surveillance_system import (
    SocialMediaSurveillanceSystem,
    WorkplaceSurveillanceSystem
)

from .knowledge_system import (
    EducationalSystem,
    AcademicPublishingSystem
)

from .biopower_system import (
    PublicHealthSystem,
    FitnessTrackingSystem
)

__all__ = [
    "SocialMediaSurveillanceSystem",
    "WorkplaceSurveillanceSystem",
    "EducationalSystem",
    "AcademicPublishingSystem",
    "PublicHealthSystem",
    "FitnessTrackingSystem"
]
