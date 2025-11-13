"""
Knowledge/Education Power System

Demonstrates Foucault's power/knowledge relationship and examination as discipline.

Key Foucauldian concepts:
1. Power and knowledge directly imply one another
2. Examination combines surveillance and normalization
3. Schools as disciplinary institutions
4. Creation of "subjects" through knowledge categorization
5. Truth is produced, not discovered
"""

from powersystems import (
    PowerSystem, Privilege, PrivilegeScope, ReachEstimation,
    PowerRelation, PowerDirection, DisciplinaryMechanism
)
from typing import List


class EducationalSystem(PowerSystem):
    """
    The school as a disciplinary institution.

    Foucault: Schools don't just transmit knowledge, they produce
    particular types of subjects through examination, surveillance,
    and normalization.
    """

    def name(self) -> str:
        return "Educational Examination System"

    def description(self) -> str:
        return (
            "Schools as factories of normalization. Through constant examination, "
            "students are measured, compared, and categorized. Knowledge and power "
            "are inseparable: exams don't reveal truth, they produce it. "
            "Foucault: 'The examination combines the techniques of an observing "
            "hierarchy and those of a normalizing judgment.'"
        )

    def get_privileges(self) -> List[Privilege]:
        return [
            Privilege(
                name="Examination Authority",
                scope=PrivilegeScope.GLOBAL,
                description="Power to test and grade students",
                limitations=[
                    "Standardized tests: 2-4 per year",
                    "Weekly quizzes and homework",
                    "Final exams: cumulative assessment",
                    "GPA scale: 0.0-4.0",
                    "Class rank: percentile ranking",
                    "Retention: permanent academic records"
                ],
                produces=[
                    "Categorized students (A, B, C, D, F)",
                    "Normalized knowledge",
                    "Academic hierarchies",
                    "Self-identifying subjects (smart/dumb)",
                    "Measurable human capital"
                ]
            ),

            Privilege(
                name="Curriculum Control",
                scope=PrivilegeScope.GLOBAL,
                description="Power to define what counts as knowledge",
                limitations=[
                    "Standardized curriculum: state-mandated",
                    "Textbook selection: approved lists",
                    "Learning objectives: measurable outcomes",
                    "Time allocation: 50-minute periods",
                    "Subject hierarchy: STEM > humanities"
                ],
                produces=[
                    "Legitimate vs illegitimate knowledge",
                    "Disciplinary boundaries",
                    "Truth regimes",
                    "Normalized epistemology",
                    "Cultural reproduction"
                ]
            ),

            Privilege(
                name="Behavioral Surveillance",
                scope=PrivilegeScope.GLOBAL,
                description="Constant observation and discipline",
                limitations=[
                    "Attendance tracking: daily records",
                    "Behavior grades: conduct scores",
                    "Discipline referrals: documented incidents",
                    "Parent notifications: triggered by thresholds",
                    "Surveillance cameras: hallways and classrooms"
                ],
                produces=[
                    "Docile bodies",
                    "Internalized discipline",
                    "Self-regulating students",
                    "Normalized behavior",
                    "Institutional subjects"
                ]
            ),

            Privilege(
                name="Credentialing Authority",
                scope=PrivilegeScope.GLOBAL,
                description="Power to grant or deny credentials",
                limitations=[
                    "Graduation requirements: specific credit hours",
                    "Degree levels: AA, BA, MA, PhD hierarchy",
                    "Accreditation: institutional gatekeeping",
                    "Prerequisites: ordered knowledge progression",
                    "Certification exams: pass/fail gates"
                ],
                produces=[
                    "Credentialed vs non-credentialed subjects",
                    "Educational capital",
                    "Social stratification",
                    "Legitimate expertise",
                    "Barrier to entry for professions"
                ]
            ),

            Privilege(
                name="Comparative Ranking",
                scope=PrivilegeScope.GLOBAL,
                description="Power to rank and compare students",
                limitations=[
                    "Class rank: 1 to N",
                    "Percentile scores: relative standing",
                    "Honor roll: top 10-20%",
                    "Dean's list: GPA thresholds",
                    "Valedictorian: single top student"
                ],
                produces=[
                    "Competitive subjects",
                    "Internalized comparison",
                    "Winners and losers",
                    "Meritocratic ideology",
                    "Normalized inequality"
                ]
            )
        ]

    def get_power_relations(self) -> List[PowerRelation]:
        privileges = self.get_privileges()
        return [
            PowerRelation(
                from_position="Institution/Teacher",
                to_position="Student",
                privilege=privileges[0],  # Examination
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Cheating (but reinforces system)",
                    "Dropping out (costly)",
                    "Alternative education",
                    "Critical pedagogy"
                ]
            ),

            PowerRelation(
                from_position="Student",
                to_position="Student (Self)",
                privilege=privileges[0],  # Examination
                direction=PowerDirection.CIRCULAR,
                resistance_points=[
                    "Critical consciousness",
                    "Recognizing social construction",
                    "Collective resistance"
                ]
            ),

            PowerRelation(
                from_position="State/Accreditors",
                to_position="Institution",
                privilege=privileges[1],  # Curriculum Control
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Academic freedom",
                    "Teacher autonomy",
                    "Informal curriculum"
                ]
            ),

            PowerRelation(
                from_position="Institution",
                to_position="Student",
                privilege=privileges[3],  # Credentialing
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Self-education",
                    "Alternative credentials",
                    "Questioning legitimacy"
                ]
            ),

            PowerRelation(
                from_position="Student",
                to_position="Student",
                privilege=privileges[4],  # Comparative Ranking
                direction=PowerDirection.LATERAL,
                resistance_points=[
                    "Cooperative learning",
                    "Rejecting competition",
                    "Solidarity"
                ]
            )
        ]

    def get_disciplinary_mechanisms(self) -> List[DisciplinaryMechanism]:
        return [
            DisciplinaryMechanism(
                name="The Examination",
                mechanism_type="examination",
                observes=[
                    "Student knowledge",
                    "Performance under pressure",
                    "Memorization ability",
                    "Compliance with format"
                ],
                normalizes_to="Standard correct answers",
                produces_knowledge=True,
                visibility_pattern="panopticon"
            ),

            DisciplinaryMechanism(
                name="The Grade",
                mechanism_type="classification",
                observes=[
                    "Test scores",
                    "Assignment quality",
                    "Participation",
                    "Behavior"
                ],
                normalizes_to="Grade distribution curve",
                produces_knowledge=True,
                visibility_pattern="examination"
            ),

            DisciplinaryMechanism(
                name="The Class Schedule",
                mechanism_type="normalization",
                observes=[
                    "Time usage",
                    "Attention span",
                    "Transition behavior"
                ],
                normalizes_to="Industrial time discipline",
                produces_knowledge=False,
                visibility_pattern="distributed"
            ),

            DisciplinaryMechanism(
                name="The Permanent Record",
                mechanism_type="surveillance",
                observes=[
                    "Academic history",
                    "Behavioral incidents",
                    "Attendance patterns",
                    "Test scores over time"
                ],
                normalizes_to="Ideal student trajectory",
                produces_knowledge=True,
                visibility_pattern="panopticon"
            ),

            DisciplinaryMechanism(
                name="Standardized Testing",
                mechanism_type="examination",
                observes=[
                    "Comparative performance",
                    "State/national standards",
                    "School effectiveness"
                ],
                normalizes_to="National benchmarks",
                produces_knowledge=True,
                visibility_pattern="examination"
            )
        ]

    def estimate_reach(self, privilege: Privilege) -> ReachEstimation:
        reach_map = {
            "Examination Authority": ReachEstimation(
                is_measurable=True,
                minimum_impact=100,  # Tests per year
                maximum_impact=10_000,  # Over educational career
                confidence=0.99,
                reasoning=(
                    "Extremely measurable: exact number of tests, precise "
                    "grading scales, permanent records."
                ),
                measurement_type="examinations × students × permanence"
            ),

            "Curriculum Control": ReachEstimation(
                is_measurable=True,
                minimum_impact=180,  # School days per year
                maximum_impact=2340,  # K-12: 13 years × 180 days
                confidence=0.95,
                reasoning=(
                    "Highly measurable: exact hours, specific standards, "
                    "documented learning objectives."
                ),
                measurement_type="instructional hours × content coverage"
            ),

            "Behavioral Surveillance": ReachEstimation(
                is_measurable=True,
                minimum_impact=1800,  # Hours per school year
                maximum_impact=23_400,  # K-12 total hours
                confidence=0.92,
                reasoning=(
                    "Very measurable: attendance records, discipline reports, "
                    "documented incidents."
                ),
                measurement_type="surveillance hours × documented behaviors"
            ),

            "Credentialing Authority": ReachEstimation(
                is_measurable=True,
                minimum_impact=1,  # One credential
                maximum_impact=10,  # Multiple degrees/certifications
                confidence=0.98,
                reasoning=(
                    "Perfectly measurable: exact credentials, specific requirements, "
                    "clear gates."
                ),
                measurement_type="credentials × requirements × gatekeeping effects"
            ),

            "Comparative Ranking": ReachEstimation(
                is_measurable=True,
                minimum_impact=1,  # Class rank
                maximum_impact=1000,  # Multiple rankings over time
                confidence=0.99,
                reasoning=(
                    "Extremely measurable: precise rankings, exact percentiles, "
                    "documented comparisons."
                ),
                measurement_type="rankings × comparisons × psychological effects"
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


class AcademicPublishingSystem(PowerSystem):
    """
    Academic publishing as a power/knowledge regime.

    Foucault: What counts as legitimate knowledge is determined
    through power relations, not objective truth.
    """

    def name(self) -> str:
        return "Academic Publishing Power System"

    def description(self) -> str:
        return (
            "Academic publishing doesn't just disseminate knowledge, it produces "
            "legitimate knowledge and legitimate knowers. Peer review, impact factors, "
            "and citation counts create hierarchies of truth. "
            "Foucault: 'Truth is a thing of this world.'"
        )

    def get_privileges(self) -> List[Privilege]:
        return [
            Privilege(
                name="Peer Review Gatekeeping",
                scope=PrivilegeScope.GLOBAL,
                description="Power to accept/reject knowledge claims",
                limitations=[
                    "Rejection rate: 70-90% for top journals",
                    "Review time: 3-12 months average",
                    "Reviewers: 2-3 per submission",
                    "Revisions: multiple rounds typically",
                    "Appeal process: limited, rarely successful"
                ],
                produces=[
                    "Legitimate vs illegitimate knowledge",
                    "Disciplinary boundaries",
                    "Authorized knowers",
                    "Citation networks",
                    "Truth regimes"
                ]
            ),

            Privilege(
                name="Impact Factor Ranking",
                scope=PrivilegeScope.GLOBAL,
                description="Quantification of knowledge value",
                limitations=[
                    "Impact factor: 0-100+ scale",
                    "H-index: researcher ranking",
                    "Citation counts: measurable influence",
                    "Journal tiers: Q1, Q2, Q3, Q4",
                    "Rankings updated: annually"
                ],
                produces=[
                    "Hierarchies of knowledge",
                    "Prestige economies",
                    "Publishing pressure",
                    "Normalized research agendas",
                    "Quantified scholarship"
                ]
            ),

            Privilege(
                name="Institutional Credentialing",
                scope=PrivilegeScope.LIMITED,
                description="Power of institutional affiliation",
                limitations=[
                    "R1 universities: top 130 in US",
                    "Ivy League: 8 institutions",
                    "Publication rates: R1 > others",
                    "Name recognition: affects peer review",
                    "Resource access: library subscriptions, funding"
                ],
                produces=[
                    "Legitimate vs peripheral scholars",
                    "Geographic/institutional inequalities",
                    "Self-perpetuating elites",
                    "Credibility by association",
                    "Knowledge monopolies"
                ]
            )
        ]

    def get_power_relations(self) -> List[PowerRelation]:
        privileges = self.get_privileges()
        return [
            PowerRelation(
                from_position="Journal Editors/Reviewers",
                to_position="Researchers",
                privilege=privileges[0],
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Open access publishing",
                    "Preprint servers",
                    "Alternative metrics",
                    "Public scholarship"
                ]
            ),

            PowerRelation(
                from_position="Researchers",
                to_position="Researchers",
                privilege=privileges[1],
                direction=PowerDirection.LATERAL,
                resistance_points=[
                    "Ignoring impact factors",
                    "Slow scholarship movements",
                    "Collective action"
                ]
            )
        ]

    def get_disciplinary_mechanisms(self) -> List[DisciplinaryMechanism]:
        return [
            DisciplinaryMechanism(
                name="Peer Review",
                mechanism_type="examination",
                observes=[
                    "Research methodology",
                    "Argument structure",
                    "Literature engagement",
                    "Disciplinary conformity"
                ],
                normalizes_to="Disciplinary standards and paradigms",
                produces_knowledge=True,
                visibility_pattern="examination"
            ),

            DisciplinaryMechanism(
                name="Citation Analysis",
                mechanism_type="surveillance",
                observes=[
                    "Who cites whom",
                    "Citation frequency",
                    "Citation networks",
                    "Knowledge lineages"
                ],
                normalizes_to="Citation norms and impact expectations",
                produces_knowledge=True,
                visibility_pattern="distributed"
            ),

            DisciplinaryMechanism(
                name="Metrics and Rankings",
                mechanism_type="classification",
                observes=[
                    "Journal rankings",
                    "Author metrics",
                    "University rankings",
                    "Department rankings"
                ],
                normalizes_to="Quantified academic worth",
                produces_knowledge=True,
                visibility_pattern="examination"
            )
        ]

    def estimate_reach(self, privilege: Privilege) -> ReachEstimation:
        if "Peer Review" in privilege.name:
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=70,  # 70% rejection rate minimum
                maximum_impact=90,  # 90% for top journals
                confidence=0.97,
                reasoning="Highly documented rejection rates and review processes",
                measurement_type="acceptance rates × submissions × time"
            )
        elif "Impact Factor" in privilege.name:
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=1,  # Low impact journals
                maximum_impact=100,  # Highest impact journals
                confidence=0.99,
                reasoning="Precisely calculated metrics, publicly available",
                measurement_type="citations × publications × time"
            )
        else:  # Institutional
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=130,  # R1 universities
                maximum_impact=4000,  # All universities worldwide
                confidence=0.90,
                reasoning="Documented institutional hierarchies and rankings",
                measurement_type="institutions × prestige × access"
            )
