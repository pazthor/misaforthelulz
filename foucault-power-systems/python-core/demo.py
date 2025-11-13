#!/usr/bin/env python3
"""
Foucault Power Systems Demo

Demonstrates the analysis of various power systems through a Foucauldian lens.
"""

import sys
sys.path.insert(0, '/home/user/misaforthelulz/foucault-power-systems/python-core')

from powersystems import PowerSystemAnalyzer
from examples import (
    SocialMediaSurveillanceSystem,
    WorkplaceSurveillanceSystem,
    EducationalSystem,
    AcademicPublishingSystem,
    PublicHealthSystem,
    FitnessTrackingSystem
)


def print_separator(char="=", length=80):
    """Print a visual separator"""
    print("\n" + char * length + "\n")


def run_individual_analysis(system, detailed=True):
    """Analyze a single power system"""
    print_separator("=")
    print(f"ANALYZING: {system.name()}")
    print_separator("=")

    if detailed:
        # Show the full Foucauldian analysis
        print(PowerSystemAnalyzer.demonstrate_concept(system))

    # Show the measurability analysis
    analysis = PowerSystemAnalyzer.analyze(system)
    print(analysis.summary())


def run_comparison_analysis():
    """Compare different types of power systems"""
    print_separator("=")
    print("COMPARATIVE POWER ANALYSIS")
    print_separator("=")

    systems = [
        SocialMediaSurveillanceSystem(),
        WorkplaceSurveillanceSystem(),
        EducationalSystem(),
        AcademicPublishingSystem(),
        PublicHealthSystem(),
        FitnessTrackingSystem()
    ]

    print("\nSYSTEM OVERVIEW\n")
    print(f"{'System':<45} {'Verdict':<20} {'Confidence':<12} {'Measurable/Total'}")
    print("-" * 95)

    analyses = []
    for system in systems:
        analysis = PowerSystemAnalyzer.analyze(system)
        analyses.append(analysis)
        ratio = f"{analysis.measurable_privileges}/{analysis.total_privileges}"
        print(f"{system.name():<45} {analysis.verdict:<20} {analysis.confidence:>6.0%}      {ratio:>8}")

    print_separator("-")

    # Find most and least measurable
    most_measurable = max(analyses, key=lambda a: a.confidence)
    least_measurable = min(analyses, key=lambda a: a.confidence)

    print(f"\nMOST MEASURABLE: {most_measurable.system_name}")
    print(f"Confidence: {most_measurable.confidence:.0%}")
    print(f"Why: {most_measurable.reasoning}\n")

    print(f"LEAST MEASURABLE: {least_measurable.system_name}")
    print(f"Confidence: {least_measurable.confidence:.0%}")
    print(f"Why: {least_measurable.reasoning}\n")


def run_thematic_analysis():
    """Analyze systems by Foucauldian themes"""
    print_separator("=")
    print("THEMATIC ANALYSIS: KEY FOUCAULDIAN CONCEPTS")
    print_separator("=")

    systems = [
        SocialMediaSurveillanceSystem(),
        WorkplaceSurveillanceSystem(),
        EducationalSystem(),
        AcademicPublishingSystem(),
        PublicHealthSystem(),
        FitnessTrackingSystem()
    ]

    # Theme 1: Surveillance and the Panopticon
    print("\n1. SURVEILLANCE AND THE PANOPTICON")
    print("-" * 80)
    print("Foucault: Power through visibility - the awareness of being watched")
    print("creates self-discipline.\n")

    for system in systems:
        surveillance_intensity = system.surveillance_intensity()
        if surveillance_intensity > 0:
            print(f"  {system.name()}: {surveillance_intensity:.0%} surveillance intensity")
            mechanisms = [m for m in system.get_disciplinary_mechanisms()
                         if 'surveillance' in m.mechanism_type.lower()]
            for mech in mechanisms:
                print(f"    → {mech.name} ({mech.visibility_pattern})")

    # Theme 2: Power/Knowledge
    print("\n\n2. POWER/KNOWLEDGE RELATIONSHIP")
    print("-" * 80)
    print("Foucault: Power and knowledge directly imply one another.\n")

    for system in systems:
        if system.produces_knowledge():
            print(f"  {system.name()}: Produces knowledge")
            knowledge_mechanisms = [m for m in system.get_disciplinary_mechanisms()
                                  if m.produces_knowledge]
            for mech in knowledge_mechanisms:
                print(f"    → {mech.name}: {mech.mechanism_type}")

    # Theme 3: Normalization
    print("\n\n3. NORMALIZATION AND DISCIPLINARY MECHANISMS")
    print("-" * 80)
    print("Foucault: Power normalizes by establishing standards and measuring")
    print("deviations from those standards.\n")

    for system in systems:
        mechanisms = [m for m in system.get_disciplinary_mechanisms()
                     if 'normalization' in m.mechanism_type.lower() or
                        'examination' in m.mechanism_type.lower()]
        if mechanisms:
            print(f"  {system.name()}:")
            for mech in mechanisms:
                if mech.normalizes_to:
                    print(f"    → Normalizes to: {mech.normalizes_to}")

    # Theme 4: Power Circulation
    print("\n\n4. POWER AS RELATIONAL AND CIRCULATING")
    print("-" * 80)
    print("Foucault: Power is not possessed but exercised in relations.\n")

    for system in systems:
        relations = system.get_power_relations()
        circular = [r for r in relations if r.direction.value == "circular"]
        lateral = [r for r in relations if r.direction.value == "lateral"]

        if circular or lateral:
            print(f"  {system.name()}:")
            for rel in circular:
                print(f"    ↔ Circular: {rel.from_position} ⟷ {rel.to_position}")
            for rel in lateral:
                print(f"    ↔ Lateral: {rel.from_position} ↔ {rel.to_position}")

    # Theme 5: Resistance
    print("\n\n5. RESISTANCE POINTS")
    print("-" * 80)
    print("Foucault: Where there is power, there is resistance.\n")

    for system in systems:
        relations = system.get_power_relations()
        reversible = [r for r in relations if r.is_reversible()]

        if reversible:
            print(f"  {system.name()}:")
            for rel in reversible[:2]:  # Show first 2
                print(f"    Resistance to '{rel.privilege.name}':")
                for point in rel.resistance_points[:3]:  # Show first 3
                    print(f"      • {point}")


def demonstrate_key_concept():
    """Deep dive into one system to show core Foucauldian concepts"""
    print_separator("=")
    print("DEEP DIVE: SOCIAL MEDIA AS MODERN PANOPTICON")
    print_separator("=")

    system = SocialMediaSurveillanceSystem()

    print("""
Michel Foucault's analysis of the Panopticon describes a prison design where
a central tower can observe all prisoners, but prisoners cannot see the tower.
The key insight: prisoners don't need to be constantly watched - the mere
possibility of observation creates self-discipline.

Social media platforms function as digital panopticons:
- Users are potentially always observed (by platforms, employers, governments, peers)
- Users can't know when they're being watched
- This creates self-censorship and normalization
- Power operates through visibility, not force

Let's analyze the measurable effects of this power system:
""")

    print(PowerSystemAnalyzer.demonstrate_concept(system))

    print("""
FOUCAULT'S KEY INSIGHT:

Traditional power (sovereign power): "I can kill you"
Modern power (disciplinary/biopower): "I can optimize you"

Social media doesn't primarily work through censorship (though that exists).
It works by producing certain types of subjects: quantified, visible,
self-policing users who internalize the platform's norms.

The most effective power is the power you exercise on yourself.
""")


def main():
    """Main demo function"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    FOUCAULT POWER SYSTEMS FRAMEWORK                          ║
║                                                                              ║
║                   Analyzing Power Through Measurability                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

"Power is not an institution, and not a structure; neither is it a certain
strength we are endowed with; it is the name that one attributes to a complex
strategical situation in a particular society."
                                                    — Michel Foucault

This framework demonstrates how Foucault's theoretical concepts about power
can be analyzed through concrete, measurable systems.

""")

    # Run different analyses
    demonstrate_key_concept()

    print_separator()
    input("Press Enter to continue to comparative analysis...")

    run_comparison_analysis()

    print_separator()
    input("Press Enter to continue to thematic analysis...")

    run_thematic_analysis()

    print_separator()
    input("Press Enter to see individual system analyses...")

    # Show a few detailed examples
    systems_to_detail = [
        EducationalSystem(),
        PublicHealthSystem()
    ]

    for system in systems_to_detail:
        run_individual_analysis(system, detailed=True)
        print_separator()
        input("Press Enter to continue...")

    print_separator("=")
    print("CONCLUSION")
    print_separator("=")

    print("""
WHAT WE'VE DEMONSTRATED:

1. Foucault's abstract concepts about power can be analyzed through
   concrete, measurable systems.

2. Different power systems show different levels of measurability:
   - Technical systems (APIs, workplace monitoring): 95-99% measurable
   - Institutional systems (education, healthcare): 85-95% measurable
   - Social systems (peer surveillance): 70-90% measurable

3. Power is not just repressive ("don't do this") but productive
   ("become this type of person"):
   - Surveillance produces self-policing subjects
   - Examination produces quantified, comparable individuals
   - Normalization produces docile, optimized bodies

4. Power and knowledge are inseparable:
   - Educational systems produce legitimate vs illegitimate knowledge
   - Medical systems produce normal vs pathological bodies
   - Platform algorithms produce engagement-optimized subjects

5. Resistance exists wherever power operates:
   - But often, resistance itself reinforces the system
   - The panopticon works best when prisoners police themselves

"The judges of normality are present everywhere. We are in the society of
the teacher-judge, the doctor-judge, the educator-judge, the social worker-judge;
it is on them that the universal reign of the normative is based."
                                                    — Michel Foucault

Thank you for exploring power systems through a Foucauldian lens.
""")


if __name__ == "__main__":
    main()
