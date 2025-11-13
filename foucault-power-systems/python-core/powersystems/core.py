"""
Core Power Systems Framework

Implements Foucault's concept that power is not a possession but a relation,
not centralized but distributed throughout networks.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Set


class PrivilegeScope(Enum):
    """Scope of privilege reach - from Foucault's concept of power diffusion"""
    GLOBAL = "global"           # Power throughout the system
    LIMITED = "limited"         # Power in specific domains
    RESTRICTED = "restricted"   # Highly constrained power
    NONE = "none"              # No power in this dimension


class PowerDirection(Enum):
    """Direction of power flow - Foucault: power circulates"""
    TOP_DOWN = "top_down"       # Traditional hierarchical
    BOTTOM_UP = "bottom_up"     # Resistance and counter-power
    LATERAL = "lateral"         # Peer-to-peer power relations
    CIRCULAR = "circular"       # Self-reinforcing power loops
    CAPILLARY = "capillary"     # Power at micro-level (Foucault's term)


@dataclass(frozen=True)
class Privilege:
    """
    A privilege represents a capability within a power system.

    Foucault: Privileges are not just permissions but productive capacities
    that create certain types of subjects and behaviors.
    """
    name: str
    scope: PrivilegeScope
    description: str
    limitations: List[str] = field(default_factory=list)
    produces: List[str] = field(default_factory=list)  # What this privilege produces/enables

    def is_measurable(self) -> bool:
        """Can this privilege be concretely measured?"""
        return len(self.limitations) > 0 and any(
            keyword in str(self.limitations).lower()
            for keyword in ['limit', 'max', 'count', 'rate', 'number', 'size']
        )


@dataclass(frozen=True)
class PowerRelation:
    """
    Represents a power relationship between actors/positions.

    Foucault: Power is relational, not possessed. It exists in relationships.
    """
    from_position: str
    to_position: str
    privilege: Privilege
    direction: PowerDirection
    resistance_points: List[str] = field(default_factory=list)  # Where power can be resisted

    def is_reversible(self) -> bool:
        """Can this power relation be inverted? (Foucault: resistance always exists)"""
        return len(self.resistance_points) > 0


@dataclass(frozen=True)
class DisciplinaryMechanism:
    """
    Foucault's disciplinary mechanisms: surveillance, normalization, examination.

    These are the micro-techniques through which power operates.
    """
    name: str
    mechanism_type: str  # surveillance, normalization, examination, classification
    observes: List[str]  # What/who is being observed
    normalizes_to: Optional[str]  # What norm is being enforced
    produces_knowledge: bool  # Does this create knowledge? (Power/Knowledge)
    visibility_pattern: str  # "panopticon" | "distributed" | "self-surveillance"


@dataclass(frozen=True)
class ReachEstimation:
    """
    Estimation of a privilege's measurable impact.

    Foucault: We can measure the effects of power, even if power itself
    is invisible and diffuse.
    """
    is_measurable: bool
    minimum_impact: int
    maximum_impact: int
    confidence: float  # 0.0 to 1.0
    reasoning: str
    measurement_type: str  # What we're measuring: "actions", "subjects", "knowledge", "discipline"

    def __post_init__(self):
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0.0 and 1.0")
        if self.minimum_impact > self.maximum_impact:
            raise ValueError("Minimum impact cannot exceed maximum impact")


class PowerSystem(ABC):
    """
    Abstract base class for all power systems.

    Foucault: "Power is everywhere; not because it embraces everything,
    but because it comes from everywhere."
    """

    @abstractmethod
    def name(self) -> str:
        """Name of this power system"""
        pass

    @abstractmethod
    def description(self) -> str:
        """Description of how power operates in this system"""
        pass

    @abstractmethod
    def get_privileges(self) -> List[Privilege]:
        """Get all privileges in this system"""
        pass

    @abstractmethod
    def get_power_relations(self) -> List[PowerRelation]:
        """Get all power relations in this system"""
        pass

    @abstractmethod
    def get_disciplinary_mechanisms(self) -> List[DisciplinaryMechanism]:
        """Get disciplinary mechanisms (surveillance, normalization, etc.)"""
        pass

    @abstractmethod
    def estimate_reach(self, privilege: Privilege) -> ReachEstimation:
        """
        Estimate the measurable reach of a privilege.

        This is the core analytical method: can we measure this power?
        """
        pass

    def total_privileges(self) -> int:
        """Count total privileges in the system"""
        return len(self.get_privileges())

    def measurable_privileges(self) -> int:
        """Count how many privileges are measurable"""
        return sum(1 for p in self.get_privileges() if p.is_measurable())

    def power_density(self) -> float:
        """
        Calculate power density: how concentrated vs distributed is power?

        Foucault: Modern power is often diffuse and distributed (capillary)
        """
        relations = self.get_power_relations()
        if not relations:
            return 0.0

        # Count unique positions
        positions = set()
        for rel in relations:
            positions.add(rel.from_position)
            positions.add(rel.to_position)

        # More positions with fewer relations = more diffuse power
        if len(positions) == 0:
            return 0.0

        return len(relations) / len(positions)

    def surveillance_intensity(self) -> float:
        """
        Measure surveillance mechanisms in the system.

        Foucault: Surveillance is a key disciplinary technique.
        """
        mechanisms = self.get_disciplinary_mechanisms()
        surveillance_count = sum(
            1 for m in mechanisms
            if 'surveillance' in m.mechanism_type.lower()
        )
        return surveillance_count / max(len(mechanisms), 1)

    def produces_knowledge(self) -> bool:
        """
        Does this power system produce knowledge?

        Foucault: Power and knowledge directly imply one another.
        """
        return any(
            m.produces_knowledge
            for m in self.get_disciplinary_mechanisms()
        )
