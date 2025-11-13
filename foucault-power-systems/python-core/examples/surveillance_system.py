"""
Surveillance Power System

Demonstrates Foucault's concept of the Panopticon and disciplinary surveillance.

Key Foucauldian concepts:
1. The Panopticon - architectural surveillance creating self-discipline
2. Visibility as a trap - constant potential observation
3. Power through observation, not just force
4. Internalization of surveillance (self-policing)
"""

from powersystems import (
    PowerSystem, Privilege, PrivilegeScope, ReachEstimation,
    PowerRelation, PowerDirection, DisciplinaryMechanism
)
from typing import List


class SocialMediaSurveillanceSystem(PowerSystem):
    """
    Modern social media as a Panopticon.

    Foucault's Panopticon in digital form: users are constantly observed,
    creating self-discipline and normalization of behavior.
    """

    def name(self) -> str:
        return "Social Media Surveillance System"

    def description(self) -> str:
        return (
            "A modern panopticon: users are constantly observed by platforms, "
            "employers, governments, and each other. The knowledge that one "
            "might be watched creates self-censorship and normalization. "
            "Foucault: 'Visibility is a trap.'"
        )

    def get_privileges(self) -> List[Privilege]:
        return [
            # Platform privileges (the watchers)
            Privilege(
                name="Data Collection",
                scope=PrivilegeScope.GLOBAL,
                description="Platform can collect all user data",
                limitations=[
                    "Collects every click, scroll, pause",
                    "Tracks 150+ data points per user",
                    "Retention: unlimited duration",
                    "Shares with 1,200+ third parties on average"
                ],
                produces=[
                    "User behavioral profiles",
                    "Predictive models of behavior",
                    "Targeted manipulation capabilities",
                    "Normalized digital subjects"
                ]
            ),

            Privilege(
                name="Algorithmic Curation",
                scope=PrivilegeScope.GLOBAL,
                description="Platform controls what users see",
                limitations=[
                    "Processes 500M+ posts daily",
                    "Recommends content based on engagement metrics",
                    "Filter bubble affects 100% of users",
                    "Appeals process: < 1% success rate"
                ],
                produces=[
                    "Echo chambers",
                    "Normalized viewpoints",
                    "Behavioral modification",
                    "Attention economy subjects"
                ]
            ),

            # Employer surveillance privileges
            Privilege(
                name="Employee Monitoring",
                scope=PrivilegeScope.LIMITED,
                description="Employers monitor employee social media",
                limitations=[
                    "70% of employers screen social media",
                    "54% have rejected candidates based on posts",
                    "Monitor public posts only (legally)",
                    "Average 3-5 years of history reviewed"
                ],
                produces=[
                    "Self-censorship",
                    "Curated public personas",
                    "Professional normalization",
                    "Blurred work/life boundaries"
                ]
            ),

            # Government surveillance
            Privilege(
                name="State Surveillance",
                scope=PrivilegeScope.LIMITED,
                description="Government surveillance of social media",
                limitations=[
                    "NSA: Collects metadata from all major platforms",
                    "Warrants required for content (in theory)",
                    "Facial recognition on public photos",
                    "Keyword monitoring on millions of accounts"
                ],
                produces=[
                    "Chilling effect on speech",
                    "Political normalization",
                    "Internalized surveillance",
                    "Docile digital citizens"
                ]
            ),

            # User self-surveillance
            Privilege(
                name="Peer Surveillance",
                scope=PrivilegeScope.GLOBAL,
                description="Users police each other",
                limitations=[
                    "Every post visible to network",
                    "Average user has 338 friends/followers",
                    "Screenshots live forever",
                    "Cancel culture reach: potentially millions"
                ],
                produces=[
                    "Self-policing behavior",
                    "Conformity to group norms",
                    "Performance of identity",
                    "Lateral power relations"
                ]
            )
        ]

    def get_power_relations(self) -> List[PowerRelation]:
        privileges = self.get_privileges()
        return [
            PowerRelation(
                from_position="Platform",
                to_position="User",
                privilege=privileges[0],  # Data Collection
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Ad blockers",
                    "Privacy settings (limited)",
                    "Not using platform (social cost)",
                    "Regulations (GDPR, etc.)"
                ]
            ),

            PowerRelation(
                from_position="Platform",
                to_position="User",
                privilege=privileges[1],  # Algorithmic Curation
                direction=PowerDirection.CIRCULAR,  # Users feed the algorithm
                resistance_points=[
                    "Chronological feeds (rarely available)",
                    "Diverse following",
                    "Recognizing manipulation"
                ]
            ),

            PowerRelation(
                from_position="Employer",
                to_position="Employee/Candidate",
                privilege=privileges[2],  # Employee Monitoring
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Private accounts",
                    "Separate professional/personal accounts",
                    "Self-censorship (but this is power working!)"
                ]
            ),

            PowerRelation(
                from_position="State",
                to_position="Citizen",
                privilege=privileges[3],  # State Surveillance
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Encryption",
                    "Anonymity tools",
                    "Legal challenges",
                    "Public awareness"
                ]
            ),

            PowerRelation(
                from_position="User",
                to_position="User",
                privilege=privileges[4],  # Peer Surveillance
                direction=PowerDirection.LATERAL,
                resistance_points=[
                    "Limited sharing",
                    "Private accounts",
                    "Awareness of performance"
                ]
            ),

            # The panopticon effect: self to self
            PowerRelation(
                from_position="User",
                to_position="User (Self)",
                privilege=privileges[4],
                direction=PowerDirection.CIRCULAR,
                resistance_points=[
                    "Critical awareness",
                    "Intentional authenticity",
                    "Rejecting normalization"
                ]
            )
        ]

    def get_disciplinary_mechanisms(self) -> List[DisciplinaryMechanism]:
        return [
            DisciplinaryMechanism(
                name="The Digital Panopticon",
                mechanism_type="surveillance",
                observes=[
                    "All user activity",
                    "Behavioral patterns",
                    "Social connections",
                    "Location data",
                    "Consumption habits"
                ],
                normalizes_to="Algorithmically-defined 'engagement'",
                produces_knowledge=True,
                visibility_pattern="panopticon"
            ),

            DisciplinaryMechanism(
                name="Algorithmic Normalization",
                mechanism_type="normalization",
                observes=[
                    "User content",
                    "Engagement metrics",
                    "Deviation from norms"
                ],
                normalizes_to="Platform community standards + engagement optimization",
                produces_knowledge=True,
                visibility_pattern="distributed"
            ),

            DisciplinaryMechanism(
                name="Metrics and Analytics",
                mechanism_type="examination",
                observes=[
                    "Likes, shares, comments",
                    "Follower counts",
                    "Reach and impressions",
                    "Engagement rates"
                ],
                normalizes_to="Quantified social worth",
                produces_knowledge=True,
                visibility_pattern="self-surveillance"
            ),

            DisciplinaryMechanism(
                name="Content Moderation",
                mechanism_type="normalization",
                observes=[
                    "All posted content",
                    "Reported content",
                    "Flagged keywords"
                ],
                normalizes_to="Acceptable discourse boundaries",
                produces_knowledge=True,
                visibility_pattern="distributed"
            ),

            DisciplinaryMechanism(
                name="Social Comparison",
                mechanism_type="examination",
                observes=[
                    "Others' curated lives",
                    "Others' metrics",
                    "Others' achievements"
                ],
                normalizes_to="Idealized lifestyle standards",
                produces_knowledge=False,
                visibility_pattern="self-surveillance"
            )
        ]

    def estimate_reach(self, privilege: Privilege) -> ReachEstimation:
        """Estimate the reach of each surveillance privilege"""

        reach_map = {
            "Data Collection": ReachEstimation(
                is_measurable=True,
                minimum_impact=150,  # 150 data points per user
                maximum_impact=1200,  # Plus 1200 third parties
                confidence=0.95,
                reasoning=(
                    "Highly measurable: concrete data points tracked, "
                    "documented third-party sharing numbers."
                ),
                measurement_type="data points × users × time"
            ),

            "Algorithmic Curation": ReachEstimation(
                is_measurable=True,
                minimum_impact=500_000_000,  # 500M posts daily
                maximum_impact=3_000_000_000,  # Affects billions
                confidence=0.90,
                reasoning=(
                    "Very measurable: daily post processing numbers, "
                    "100% user reach within platform."
                ),
                measurement_type="posts processed × users affected"
            ),

            "Employee Monitoring": ReachEstimation(
                is_measurable=True,
                minimum_impact=70,  # 70% of employers
                maximum_impact=100,
                confidence=0.85,
                reasoning=(
                    "Survey data provides concrete percentages of employer "
                    "surveillance and rejection rates."
                ),
                measurement_type="percentage of workforce × actions taken"
            ),

            "State Surveillance": ReachEstimation(
                is_measurable=True,
                minimum_impact=1_000_000,  # Millions monitored
                maximum_impact=100_000_000,  # Potentially everyone
                confidence=0.60,
                reasoning=(
                    "Partially measurable: some programs documented (PRISM, etc.), "
                    "but full scope classified. Known metadata collection is total."
                ),
                measurement_type="accounts monitored × data collected"
            ),

            "Peer Surveillance": ReachEstimation(
                is_measurable=True,
                minimum_impact=338,  # Average network size
                maximum_impact=10_000_000,  # Viral reach potential
                confidence=0.80,
                reasoning=(
                    "Network size measurable, viral potential calculable, "
                    "screenshot permanence documented."
                ),
                measurement_type="network size × visibility duration"
            )
        }

        return reach_map.get(
            privilege.name,
            ReachEstimation(
                is_measurable=False,
                minimum_impact=0,
                maximum_impact=0,
                confidence=0.0,
                reasoning="Unknown privilege",
                measurement_type="unknown"
            )
        )


class WorkplaceSurveillanceSystem(PowerSystem):
    """
    Modern workplace surveillance and productivity monitoring.

    Foucault: Disciplinary institutions create docile bodies through
    constant observation and measurement.
    """

    def name(self) -> str:
        return "Workplace Surveillance System"

    def description(self) -> str:
        return (
            "Digital Taylorism: constant measurement and surveillance of worker "
            "productivity. Every keystroke, mouse movement, and minute tracked. "
            "Workers internalize surveillance, becoming self-disciplining subjects. "
            "Foucault: 'Discipline makes individuals.'"
        )

    def get_privileges(self) -> List[Privilege]:
        return [
            Privilege(
                name="Productivity Monitoring",
                scope=PrivilegeScope.GLOBAL,
                description="Track all employee computer activity",
                limitations=[
                    "Keystroke logging: every key press",
                    "Mouse movement tracking: 60 times per minute",
                    "Screenshot capture: every 5-10 minutes",
                    "Active/idle time: down to the second",
                    "Application usage: full timeline"
                ],
                produces=[
                    "Productivity scores",
                    "Normalized work pace",
                    "Self-monitoring behavior",
                    "Anxiety and compliance"
                ]
            ),

            Privilege(
                name="Communication Surveillance",
                scope=PrivilegeScope.GLOBAL,
                description="Monitor all workplace communications",
                limitations=[
                    "Email scanning: 100% of messages",
                    "Slack/Teams monitoring: all channels",
                    "Keyword flagging: customizable lists",
                    "Sentiment analysis: automated scoring",
                    "Retention: typically 7 years"
                ],
                produces=[
                    "Self-censorship",
                    "Professional language norms",
                    "Controlled discourse",
                    "Risk-averse communication"
                ]
            ),

            Privilege(
                name="Performance Metrics",
                scope=PrivilegeScope.GLOBAL,
                description="Quantify all work output",
                limitations=[
                    "Tickets closed per day",
                    "Lines of code written",
                    "Calls handled per hour",
                    "Customer satisfaction scores",
                    "Time to completion metrics"
                ],
                produces=[
                    "Quantified workers",
                    "Competitive pressure",
                    "Normalized productivity levels",
                    "Gamification of labor"
                ]
            )
        ]

    def get_power_relations(self) -> List[PowerRelation]:
        privileges = self.get_privileges()
        return [
            PowerRelation(
                from_position="Employer/Management",
                to_position="Employee",
                privilege=privileges[0],
                direction=PowerDirection.TOP_DOWN,
                resistance_points=[
                    "Union organizing",
                    "Legal limits (minimal)",
                    "Quiet quitting",
                    "Working to rule"
                ]
            ),

            PowerRelation(
                from_position="Employee",
                to_position="Employee (Self)",
                privilege=privileges[0],
                direction=PowerDirection.CIRCULAR,
                resistance_points=[
                    "Awareness of surveillance",
                    "Collective resistance",
                    "Finding other employment"
                ]
            )
        ]

    def get_disciplinary_mechanisms(self) -> List[DisciplinaryMechanism]:
        return [
            DisciplinaryMechanism(
                name="Productivity Dashboard",
                mechanism_type="examination",
                observes=["All work metrics", "Time utilization", "Output quality"],
                normalizes_to="Optimal productivity score",
                produces_knowledge=True,
                visibility_pattern="panopticon"
            ),

            DisciplinaryMechanism(
                name="Automated Alerts",
                mechanism_type="surveillance",
                observes=["Idle time", "Policy violations", "Productivity dips"],
                normalizes_to="Constant activity",
                produces_knowledge=True,
                visibility_pattern="distributed"
            )
        ]

    def estimate_reach(self, privilege: Privilege) -> ReachEstimation:
        if "Monitoring" in privilege.name:
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=10_000,  # Thousands of data points per day
                maximum_impact=1_000_000,  # Cumulative surveillance
                confidence=0.98,
                reasoning="Extremely precise tracking of every action",
                measurement_type="actions tracked × time"
            )
        elif "Communication" in privilege.name:
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=100,  # Messages per day
                maximum_impact=50_000,  # All communications over time
                confidence=0.95,
                reasoning="Every message logged and analyzable",
                measurement_type="communications × retention period"
            )
        else:  # Performance Metrics
            return ReachEstimation(
                is_measurable=True,
                minimum_impact=10,  # Daily metrics
                maximum_impact=10_000,  # Cumulative metrics
                confidence=0.99,
                reasoning="Perfectly quantified performance data",
                measurement_type="metrics × frequency"
            )
