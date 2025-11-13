"""
Power System Analyzer

Analyzes power systems to determine measurability, reach, and Foucauldian characteristics.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from .core import PowerSystem, Privilege, PrivilegeScope, DisciplinaryMechanism


@dataclass
class SystemAnalysis:
    """
    Complete analysis of a power system's measurability and characteristics.
    """
    system_name: str
    is_measurable: bool
    confidence: float
    minimum_reach: int
    maximum_reach: int
    measurable_privileges: int
    total_privileges: int
    verdict: str  # "✓ MEASURABLE" | "~ ESTIMABLE" | "✗ SPECULATION"
    reasoning: str
    power_characteristics: Dict[str, any]

    def measurability_ratio(self) -> float:
        """Ratio of measurable to total privileges"""
        if self.total_privileges == 0:
            return 0.0
        return self.measurable_privileges / self.total_privileges

    def summary(self) -> str:
        """Generate a summary of the analysis"""
        return f"""
{self.verdict} {self.system_name}
Confidence: {self.confidence:.0%}
Measurable Privileges: {self.measurable_privileges}/{self.total_privileges}
Reach: {self.minimum_reach} - {self.maximum_reach}

{self.reasoning}

Power Characteristics:
- Power Density: {self.power_characteristics.get('power_density', 0):.2f}
- Surveillance Intensity: {self.power_characteristics.get('surveillance_intensity', 0):.0%}
- Produces Knowledge: {self.power_characteristics.get('produces_knowledge', False)}
- Disciplinary Mechanisms: {self.power_characteristics.get('disciplinary_count', 0)}
"""


class PowerSystemAnalyzer:
    """
    Analyzes power systems for measurability and Foucauldian characteristics.

    Key insight from Foucault: Power can be analyzed through its effects,
    even when it appears invisible or diffuse.
    """

    @staticmethod
    def analyze(system: PowerSystem) -> SystemAnalysis:
        """
        Perform comprehensive analysis of a power system.

        Returns SystemAnalysis with measurability verdict and characteristics.
        """
        privileges = system.get_privileges()
        total_privs = len(privileges)
        measurable_privs = sum(1 for p in privileges if p.is_measurable())

        # Calculate overall confidence
        if total_privs == 0:
            confidence = 0.0
        else:
            # Base confidence on measurability ratio
            base_confidence = measurable_privs / total_privs

            # Adjust for specific measurable elements
            reach_estimations = [
                system.estimate_reach(p) for p in privileges
            ]
            avg_reach_confidence = sum(
                r.confidence for r in reach_estimations
            ) / max(len(reach_estimations), 1)

            confidence = (base_confidence + avg_reach_confidence) / 2

        # Calculate total reach
        reach_estimations = [system.estimate_reach(p) for p in privileges]
        min_reach = sum(r.minimum_impact for r in reach_estimations)
        max_reach = sum(r.maximum_impact for r in reach_estimations)

        # Determine verdict
        is_measurable = confidence >= 0.7
        if confidence >= 0.85:
            verdict = "✓ MEASURABLE"
        elif confidence >= 0.5:
            verdict = "~ ESTIMABLE"
        else:
            verdict = "✗ SPECULATION"

        # Generate reasoning
        reasoning = PowerSystemAnalyzer._generate_reasoning(
            system, measurable_privs, total_privs, confidence
        )

        # Gather power characteristics
        characteristics = {
            'power_density': system.power_density(),
            'surveillance_intensity': system.surveillance_intensity(),
            'produces_knowledge': system.produces_knowledge(),
            'disciplinary_count': len(system.get_disciplinary_mechanisms()),
            'total_relations': len(system.get_power_relations())
        }

        return SystemAnalysis(
            system_name=system.name(),
            is_measurable=is_measurable,
            confidence=confidence,
            minimum_reach=min_reach,
            maximum_reach=max_reach,
            measurable_privileges=measurable_privs,
            total_privileges=total_privs,
            verdict=verdict,
            reasoning=reasoning,
            power_characteristics=characteristics
        )

    @staticmethod
    def _generate_reasoning(
        system: PowerSystem,
        measurable: int,
        total: int,
        confidence: float
    ) -> str:
        """Generate human-readable reasoning for the analysis"""
        ratio = measurable / max(total, 1)

        if confidence >= 0.85:
            return (
                f"This system demonstrates HIGH MEASURABILITY. "
                f"{measurable}/{total} privileges have concrete limitations. "
                f"Power effects are quantifiable and observable. "
                f"Following Foucault: we can analyze this power through its measurable effects."
            )
        elif confidence >= 0.5:
            return (
                f"This system shows MODERATE MEASURABILITY. "
                f"{measurable}/{total} privileges have some concrete limits, "
                f"but others remain more abstract. "
                f"Power is partially quantifiable but requires estimation. "
                f"Foucault: Power is more diffuse here, but still analyzable."
            )
        else:
            return (
                f"This system exhibits LOW MEASURABILITY. "
                f"Only {measurable}/{total} privileges have concrete limitations. "
                f"Power appears more as abstract influence than measurable capacity. "
                f"Foucault: This power operates through discourse and subjectification, "
                f"harder to quantify but no less real."
            )

    @staticmethod
    def compare(system1: PowerSystem, system2: PowerSystem) -> str:
        """
        Compare two power systems and their measurability.

        Useful for understanding how different power regimes work.
        """
        analysis1 = PowerSystemAnalyzer.analyze(system1)
        analysis2 = PowerSystemAnalyzer.analyze(system2)

        comparison = f"""
POWER SYSTEM COMPARISON

System 1: {analysis1.system_name}
{analysis1.verdict} | Confidence: {analysis1.confidence:.0%}

System 2: {analysis2.system_name}
{analysis2.verdict} | Confidence: {analysis2.confidence:.0%}

MEASURABILITY:
- {system1.name()}: {analysis1.measurability_ratio():.0%} measurable
- {system2.name()}: {analysis2.measurability_ratio():.0%} measurable

POWER DENSITY (relations per position):
- {system1.name()}: {analysis1.power_characteristics['power_density']:.2f}
- {system2.name()}: {analysis2.power_characteristics['power_density']:.2f}

SURVEILLANCE:
- {system1.name()}: {analysis1.power_characteristics['surveillance_intensity']:.0%}
- {system2.name()}: {analysis2.power_characteristics['surveillance_intensity']:.0%}

KNOWLEDGE PRODUCTION:
- {system1.name()}: {analysis1.power_characteristics['produces_knowledge']}
- {system2.name()}: {analysis2.power_characteristics['produces_knowledge']}
"""
        # Add interpretation
        if analysis1.confidence > analysis2.confidence:
            comparison += f"\n{system1.name()} is MORE MEASURABLE than {system2.name()}."
            comparison += "\nFoucault: More measurable systems often have more explicit disciplinary mechanisms."
        elif analysis2.confidence > analysis1.confidence:
            comparison += f"\n{system2.name()} is MORE MEASURABLE than {system1.name()}."
            comparison += "\nFoucault: More measurable systems often have more explicit disciplinary mechanisms."
        else:
            comparison += "\nBoth systems show similar measurability."
            comparison += "\nFoucault: Different power regimes can have equivalent measurability."

        return comparison

    @staticmethod
    def demonstrate_concept(system: PowerSystem) -> str:
        """
        Demonstrate the Privilege → Limitation → Measurement flow.

        Core Foucauldian insight: Power is visible through its limitations.
        """
        output = f"\n{'='*70}\n"
        output += f"FOUCAULT POWER ANALYSIS: {system.name()}\n"
        output += f"{'='*70}\n\n"
        output += f"Description: {system.description()}\n\n"

        output += "PRIVILEGE → LIMITATION → MEASUREMENT\n"
        output += "-" * 70 + "\n\n"

        for privilege in system.get_privileges():
            output += f"Privilege: {privilege.name}\n"
            output += f"  Scope: {privilege.scope.value}\n"

            if privilege.limitations:
                output += f"  Limitations:\n"
                for lim in privilege.limitations:
                    output += f"    • {lim}\n"

            reach = system.estimate_reach(privilege)
            output += f"  Measurement:\n"
            output += f"    • Measurable: {reach.is_measurable}\n"
            output += f"    • Reach: {reach.minimum_impact} - {reach.maximum_impact}\n"
            output += f"    • Confidence: {reach.confidence:.0%}\n"
            output += f"    • Type: {reach.measurement_type}\n"

            if privilege.produces:
                output += f"  Produces (Foucault - Productive Power):\n"
                for prod in privilege.produces:
                    output += f"    • {prod}\n"

            output += "\n"

        # Add disciplinary mechanisms section
        mechanisms = system.get_disciplinary_mechanisms()
        if mechanisms:
            output += "\nDISCIPLINARY MECHANISMS (Foucault)\n"
            output += "-" * 70 + "\n"
            for mech in mechanisms:
                output += f"\n{mech.name}\n"
                output += f"  Type: {mech.mechanism_type}\n"
                output += f"  Visibility Pattern: {mech.visibility_pattern}\n"
                output += f"  Produces Knowledge: {mech.produces_knowledge}\n"

        # Add power relations
        relations = system.get_power_relations()
        if relations:
            output += "\n\nPOWER RELATIONS (Foucault: Power is relational)\n"
            output += "-" * 70 + "\n"
            for rel in relations:
                arrow = "→" if rel.direction.value != "circular" else "↔"
                output += f"\n{rel.from_position} {arrow} {rel.to_position}\n"
                output += f"  Privilege: {rel.privilege.name}\n"
                output += f"  Direction: {rel.direction.value}\n"
                if rel.resistance_points:
                    output += f"  Resistance Points: {', '.join(rel.resistance_points)}\n"

        output += f"\n{'='*70}\n"
        return output
