"""
Biopower and Healthcare System

Demonstrates Foucault's concept of biopower: power over life itself.

Key Foucauldian concepts:
1. Biopower - power over populations, bodies, and life
2. Biopolitics - governance through management of life
3. Normalization of bodies and behaviors
4. Medical gaze - clinical observation as power
5. Population statistics and regulation
"""

from powersystems import (
    PowerSystem, Privilege, PrivilegeScope, ReachEstimation,
    PowerRelation, PowerDirection, DisciplinaryMechanism
)
from typing import List


class PublicHealthSystem(PowerSystem):
    """
    Public health as biopower.

    Foucault: Beginning in the 18th century, power shifted from the sovereign's
    right to kill to the state's power to "make live" - managing populations
    through health, reproduction, and life expectancy.
    """

    def name(self) -> str:
        return "Public Health Biopower System"

    def description(self) -> str:
        return (
            "Biopower operates on populations rather than individuals. Through "
            "statistics, norms, and interventions, states manage life itself: "
            "birth rates, mortality, disease, vaccination, reproduction. "
            "Foucault: 'Power would no longer be dealing simply with legal subjects "
            "over whom the ultimate dominion was death, but with living beings.'"
        )

    def get_privileges(self) -> List[Privilege]:
        return [
            Privilege(
                name="Population Surveillance",
                scope=PrivilegeScope.GLOBAL,
                description="Statistical monitoring of population health",
                limitations=[
                    "Disease reporting: mandatory for 120+ conditions",
                    "Vital statistics: all births, deaths recorded",
                    "Vaccination tracking: state registries",
                    "Cancer registries: comprehensive databases",
                    "COVID tracking: real-time case counts",
                    "Life expectancy: calculated to decimal points"
                ],
                produces=[
                    "Population norms",
                    "Normal vs abnormal bodies",
                    "Risk profiles",
                    "Biomedical subjects",
                    "Governable populations"
                ]
            ),

            Privilege(
                name="Health Intervention Authority",
                scope=PrivilegeScope.GLOBAL,
                description="Power to mandate health behaviors",
                limitations=[
                    "Vaccination mandates: required for school entry",
                    "Quarantine authority: forced isolation",
                    "Fluoridation: municipal water treatment",
                    "Screenings: mandatory for certain jobs/schools",
                    "Health codes: restaurant inspections, standards"
                ],
                produces=[
                    "Normalized health practices",
                    "Compliant populations",
                    "Biomedical citizenship",
                    "Healthy vs unhealthy subjects",
                    "Collective body management"
                ]
            ),

            Privilege(
                name="Reproductive Regulation",
                scope=PrivilegeScope.LIMITED,
                description="Control over reproduction and sexuality",
                limitations=[
                    "Birth certificates: state registration required",
                    "Prenatal screening: encouraged/required",
                    "Genetic counseling: normalization of genetics",
                    "IVF regulations: who can access",
                    "Abortion laws: geographic variation",
                    "Contraception access: policy-determined"
                ],
                produces=[
                    "Normal vs abnormal reproduction",
                    "Regulated sexuality",
                    "Optimized populations",
                    "Eugenic pressures",
                    "Reproductive subjects"
                ]
            ),

            Privilege(
                name="Health Data Collection",
                scope=PrivilegeScope.GLOBAL,
                description="Comprehensive medical surveillance",
                limitations=[
                    "Electronic Health Records: all encounters",
                    "Insurance claims: every procedure",
                    "Prescription monitoring: opioid databases",
                    "Genetic databases: millions of profiles",
                    "Wearable data: continuous biometric tracking"
                ],
                produces=[
                    "Legible bodies",
                    "Risk-sorted populations",
                    "Predictive health profiles",
                    "Data subjects",
                    "Algorithmic health governance"
                ]
            ),

            Privilege(
                name="Normalization Through Metrics",
                scope=PrivilegeScope.GLOBAL,
                description="Definition of healthy through measurement",
                limitations=[
                    "BMI standards: 18.5-24.9 'normal'",
                    "Blood pressure: <120/80 'normal'",
                    "Blood sugar: 70-99 mg/dL 'normal'",
                    "Cholesterol: <200 mg/dL 'desirable'",
                    "Growth charts: percentile rankings",
                    "Mental health scales: DSM-5 criteria"
                ],
                produces=[
                    "Normal vs abnormal bodies",
                    "Self-monitoring subjects",
                    "Medicalized daily life",
                    "Health anxiety",
                    "Constant self-improvement"
                ]
            )
        ]

    def get_power_relations(self) -> List[PowerRelation]:
        privileges = self.get_privileges()
        return [
            PowerRelation(
                from_position="State/Public Health",
                to_position="Population",
                privilege=privileges[0],  # Surveillance
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Privacy protections (limited)",
                    "Refusing testing",
                    "Alternative health movements",
                    "Health freedom activism"
                ]
            ),

            PowerRelation(
                from_position="State/Public Health",
                to_position="Population",
                privilege=privileges[1],  # Intervention
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Vaccine refusal",
                    "Civil disobedience",
                    "Legal challenges",
                    "Religious exemptions"
                ]
            ),

            PowerRelation(
                from_position="Individual",
                to_position="Individual (Self)",
                privilege=privileges[4],  # Normalization
                direction=PowerDirection.CIRCULAR,
                resistance_points=[
                    "Body positivity",
                    "Disability justice",
                    "Mad pride movements",
                    "Rejecting medicalization"
                ]
            ),

            PowerRelation(
                from_position="Medical Profession",
                to_position="Patient/Citizen",
                privilege=privileges[3],  # Data Collection
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Refusing tests",
                    "Data privacy laws",
                    "Alternative medicine",
                    "Patient autonomy"
                ]
            )
        ]

    def get_disciplinary_mechanisms(self) -> List[DisciplinaryMechanism]:
        return [
            DisciplinaryMechanism(
                name="The Medical Gaze",
                mechanism_type="surveillance",
                observes=[
                    "Bodies and symptoms",
                    "Deviations from norms",
                    "Risk factors",
                    "Behavioral patterns"
                ],
                normalizes_to="Medical definitions of health",
                produces_knowledge=True,
                visibility_pattern="examination"
            ),

            DisciplinaryMechanism(
                name="Population Statistics",
                mechanism_type="classification",
                observes=[
                    "Birth/death rates",
                    "Disease prevalence",
                    "Life expectancy",
                    "Health disparities"
                ],
                normalizes_to="Population-level norms",
                produces_knowledge=True,
                visibility_pattern="distributed"
            ),

            DisciplinaryMechanism(
                name="Health Campaigns",
                mechanism_type="normalization",
                observes=[
                    "Public behavior",
                    "Lifestyle choices",
                    "Compliance with recommendations"
                ],
                normalizes_to="Healthy lifestyle standards",
                produces_knowledge=False,
                visibility_pattern="distributed"
            ),

            DisciplinaryMechanism(
                name="Diagnostic Classification",
                mechanism_type="classification",
                observes=[
                    "Symptoms and signs",
                    "Test results",
                    "Behavioral patterns"
                ],
                normalizes_to="ICD-10/DSM-5 categories",
                produces_knowledge=True,
                visibility_pattern="examination"
            ),

            DisciplinaryMechanism(
                name="Biometric Tracking",
                mechanism_type="surveillance",
                observes=[
                    "Heart rate",
                    "Steps walked",
                    "Sleep patterns",
                    "Calorie consumption"
                ],
                normalizes_to="Optimal health metrics",
                produces_knowledge=True,
                visibility_pattern="self-surveillance"
            )
        ]

    def estimate_reach(self, privilege: Privilege) -> ReachEstimation:
        reach_map = {
            "Population Surveillance": ReachEstimation(
                is_measurable=True,
                minimum_impact=120,  # 120+ reportable diseases
                maximum_impact=300_000_000,  # Entire population tracked
                confidence=0.98,
                reasoning=(
                    "Extremely measurable: comprehensive vital statistics, "
                    "disease registries, mandatory reporting."
                ),
                measurement_type="data points × population × time"
            ),

            "Health Intervention Authority": ReachEstimation(
                is_measurable=True,
                minimum_impact=50_000_000,  # School-age children for vaccines
                maximum_impact=300_000_000,  # Entire population (water fluoridation)
                confidence=0.95,
                reasoning=(
                    "Highly measurable: documented vaccination rates, "
                    "quarantine orders, municipal fluoridation coverage."
                ),
                measurement_type="interventions × population coverage"
            ),

            "Reproductive Regulation": ReachEstimation(
                is_measurable=True,
                minimum_impact=3_500_000,  # Births per year
                maximum_impact=150_000_000,  # Reproductive-age population
                confidence=0.85,
                reasoning=(
                    "Measurable through birth certificates, IVF statistics, "
                    "abortion rates, though some aspects harder to quantify."
                ),
                measurement_type="reproductive events × regulations × reach"
            ),

            "Health Data Collection": ReachEstimation(
                is_measurable=True,
                minimum_impact=1_000_000_000,  # Medical encounters per year
                maximum_impact=10_000_000_000,  # Cumulative health data points
                confidence=0.99,
                reasoning=(
                    "Extremely measurable: EHRs track everything, insurance claims "
                    "documented, wearables generate continuous data."
                ),
                measurement_type="data points × encounters × retention"
            ),

            "Normalization Through Metrics": ReachEstimation(
                is_measurable=True,
                minimum_impact=300_000_000,  # Entire population exposed to norms
                maximum_impact=1_000_000_000,  # Lifetime of normalizing measurements
                confidence=0.93,
                reasoning=(
                    "Highly measurable: precise metric definitions, documented "
                    "normal ranges, standardized across medicine."
                ),
                measurement_type="measurements × individuals × lifetime"
            )
        }

        return reach_map.get(privilege.name, ReachEstimation(
            is_measurable=False,
            minimum_impact=0,
            maximum_impact=0,
            confidence=0.0,
            reasoning="Unknown privilege",
            measurement_type="unknown"
        ))


class FitnessTrackingSystem(PowerSystem):
    """
    Fitness tracking and quantified self as biopower.

    Foucault: Biopower works not just through state coercion but through
    individuals' voluntary participation in self-optimization.
    """

    def name(self) -> str:
        return "Fitness Tracking Biopower System"

    def description(self) -> str:
        return (
            "The quantified self: wearable devices turn bodies into data streams. "
            "Users voluntarily surveil themselves, internalize health norms, and "
            "optimize their biology. Biopower operates through self-discipline. "
            "Foucault: 'There is no need for arms, physical violence, material "
            "constraints. Just a gaze.'"
        )

    def get_privileges(self) -> List[Privilege]:
        return [
            Privilege(
                name="Continuous Biometric Surveillance",
                scope=PrivilegeScope.GLOBAL,
                description="24/7 tracking of body metrics",
                limitations=[
                    "Heart rate: measured every second",
                    "Steps: counted continuously",
                    "Sleep stages: monitored all night",
                    "Calories: estimated constantly",
                    "GPS tracking: continuous location",
                    "Data retention: unlimited"
                ],
                produces=[
                    "Self-optimizing subjects",
                    "Gamified health",
                    "Normalized activity levels",
                    "Data-driven bodies",
                    "Voluntary surveillance"
                ]
            ),

            Privilege(
                name="Social Comparison and Competition",
                scope=PrivilegeScope.GLOBAL,
                description="Ranking and comparing fitness data",
                limitations=[
                    "Leaderboards: ranked by steps/calories",
                    "Badges and achievements: gamification",
                    "Challenges: competitive events",
                    "Social sharing: automatic posts",
                    "Peer pressure: visible activity"
                ],
                produces=[
                    "Competitive optimization",
                    "Social pressure to perform",
                    "Normalized fitness culture",
                    "Externalized motivation",
                    "Fitness hierarchies"
                ]
            ),

            Privilege(
                name="Health Insurance Integration",
                scope=PrivilegeScope.LIMITED,
                description="Linking activity data to insurance",
                limitations=[
                    "Premium discounts: up to 25% for data sharing",
                    "Step goals: typically 7,000-10,000 per day",
                    "Wellness points: earn rewards",
                    "Data sharing: with employers/insurers",
                    "Penalties: for non-compliance"
                ],
                produces=[
                    "Coerced participation",
                    "Economic biopower",
                    "Surveillance as condition of coverage",
                    "Optimized worker bodies",
                    "Actuarial subjects"
                ]
            )
        ]

    def get_power_relations(self) -> List[PowerRelation]:
        privileges = self.get_privileges()
        return [
            PowerRelation(
                from_position="Platform/Device Company",
                to_position="User",
                privilege=privileges[0],
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Not wearing device",
                    "Data deletion",
                    "Privacy settings (limited)"
                ]
            ),

            PowerRelation(
                from_position="User",
                to_position="User (Self)",
                privilege=privileges[0],
                direction=PowerDirection.CIRCULAR,
                resistance_points=[
                    "Critical awareness",
                    "Rejecting quantification",
                    "Body autonomy"
                ]
            ),

            PowerRelation(
                from_position="Employer/Insurer",
                to_position="Employee/Insured",
                privilege=privileges[2],
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Refusing to participate (costly)",
                    "Regulation (limited)",
                    "Collective bargaining"
                ]
            )
        ]

    def get_disciplinary_mechanisms(self) -> List[DisciplinaryMechanism]:
        return [
            DisciplinaryMechanism(
                name="Activity Rings/Goals",
                mechanism_type="normalization",
                observes=["Daily activity", "Goal completion", "Streaks"],
                normalizes_to="10,000 steps, 30 active minutes, etc.",
                produces_knowledge=True,
                visibility_pattern="self-surveillance"
            ),

            DisciplinaryMechanism(
                name="Notifications and Reminders",
                mechanism_type="surveillance",
                observes=["Inactivity periods", "Missed goals", "Irregular patterns"],
                normalizes_to="Constant activity",
                produces_knowledge=True,
                visibility_pattern="panopticon"
            ),

            DisciplinaryMechanism(
                name="Health Scoring",
                mechanism_type="examination",
                observes=["All biometric data", "Activity patterns", "Trends over time"],
                normalizes_to="Optimal health score",
                produces_knowledge=True,
                visibility_pattern="examination"
            )
        ]

    def estimate_reach(self, privilege: Privilege) -> ReachEstimation:
        if "Biometric" in privilege.name:
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=86_400,  # Seconds per day of tracking
                maximum_impact=31_536_000,  # Seconds per year
                confidence=0.99,
                reasoning="Perfectly measurable: continuous digital tracking",
                measurement_type="data points per second × time"
            )
        elif "Social" in privilege.name:
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=100,  # Social network size
                maximum_impact=10_000,  # Large networks
                confidence=0.90,
                reasoning="Measurable through connection counts and engagement",
                measurement_type="connections × interactions × visibility"
            )
        else:  # Insurance
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=10_000_000,  # Users in wellness programs
                maximum_impact=100_000_000,  # Potential reach
                confidence=0.85,
                reasoning="Documented participation rates in wellness programs",
                measurement_type="participants × incentives × compliance"
            )
