/**
 * Power System Analyzer - TypeScript Client
 *
 * Provides TypeScript interface for analyzing Foucauldian power systems
 */

import {
  PowerSystemType,
  SystemAnalysis,
  PowerAnalysisVisualization,
  PowerNode,
  PowerEdge,
  PowerMetrics,
  FoucaultConceptType,
  ThematicAnalysis,
  PowerDirection
} from './types';

export class PowerSystemAnalyzer {
  /**
   * Analyze a single power system
   */
  static analyze(systemType: PowerSystemType): SystemAnalysis {
    // In a full implementation, this would call the Python backend
    // For now, we'll provide a mock implementation
    const mockAnalyses: Record<PowerSystemType, Partial<SystemAnalysis>> = {
      [PowerSystemType.SOCIAL_MEDIA_SURVEILLANCE]: {
        system_name: "Social Media Surveillance System",
        is_measurable: true,
        confidence: 0.93,
        measurable_privileges: 5,
        total_privileges: 5,
        verdict: "✓ MEASURABLE"
      },
      [PowerSystemType.WORKPLACE_SURVEILLANCE]: {
        system_name: "Workplace Surveillance System",
        is_measurable: true,
        confidence: 0.97,
        measurable_privileges: 3,
        total_privileges: 3,
        verdict: "✓ MEASURABLE"
      },
      [PowerSystemType.EDUCATIONAL]: {
        system_name: "Educational Examination System",
        is_measurable: true,
        confidence: 0.95,
        measurable_privileges: 5,
        total_privileges: 5,
        verdict: "✓ MEASURABLE"
      },
      [PowerSystemType.ACADEMIC_PUBLISHING]: {
        system_name: "Academic Publishing Power System",
        is_measurable: true,
        confidence: 0.95,
        measurable_privileges: 3,
        total_privileges: 3,
        verdict: "✓ MEASURABLE"
      },
      [PowerSystemType.PUBLIC_HEALTH]: {
        system_name: "Public Health Biopower System",
        is_measurable: true,
        confidence: 0.94,
        measurable_privileges: 5,
        total_privileges: 5,
        verdict: "✓ MEASURABLE"
      },
      [PowerSystemType.FITNESS_TRACKING]: {
        system_name: "Fitness Tracking Biopower System",
        is_measurable: true,
        confidence: 0.91,
        measurable_privileges: 3,
        total_privileges: 3,
        verdict: "✓ MEASURABLE"
      }
    };

    const base = mockAnalyses[systemType];
    return {
      system_name: base.system_name!,
      is_measurable: base.is_measurable!,
      confidence: base.confidence!,
      minimum_reach: 1000,
      maximum_reach: 1000000,
      measurable_privileges: base.measurable_privileges!,
      total_privileges: base.total_privileges!,
      verdict: base.verdict!,
      reasoning: "This system demonstrates high measurability through concrete limitations and metrics.",
      power_characteristics: {
        power_density: 2.5,
        surveillance_intensity: 0.8,
        produces_knowledge: true,
        disciplinary_count: 4,
        total_relations: 6
      }
    };
  }

  /**
   * Compare two power systems
   */
  static compare(system1: PowerSystemType, system2: PowerSystemType): string {
    const analysis1 = this.analyze(system1);
    const analysis2 = this.analyze(system2);

    return `
POWER SYSTEM COMPARISON

System 1: ${analysis1.system_name}
${analysis1.verdict} | Confidence: ${(analysis1.confidence * 100).toFixed(0)}%

System 2: ${analysis2.system_name}
${analysis2.verdict} | Confidence: ${(analysis2.confidence * 100).toFixed(0)}%

MEASURABILITY:
- ${analysis1.system_name}: ${((analysis1.measurable_privileges / analysis1.total_privileges) * 100).toFixed(0)}% measurable
- ${analysis2.system_name}: ${((analysis2.measurable_privileges / analysis2.total_privileges) * 100).toFixed(0)}% measurable

POWER DENSITY (relations per position):
- ${analysis1.system_name}: ${analysis1.power_characteristics.power_density.toFixed(2)}
- ${analysis2.system_name}: ${analysis2.power_characteristics.power_density.toFixed(2)}

SURVEILLANCE:
- ${analysis1.system_name}: ${(analysis1.power_characteristics.surveillance_intensity * 100).toFixed(0)}%
- ${analysis2.system_name}: ${(analysis2.power_characteristics.surveillance_intensity * 100).toFixed(0)}%

${analysis1.confidence > analysis2.confidence
        ? `${analysis1.system_name} is MORE MEASURABLE than ${analysis2.system_name}.`
        : analysis2.confidence > analysis1.confidence
          ? `${analysis2.system_name} is MORE MEASURABLE than ${analysis1.system_name}.`
          : 'Both systems show similar measurability.'
      }
`;
  }

  /**
   * Generate visualization data for a power system
   */
  static visualize(systemType: PowerSystemType): PowerAnalysisVisualization {
    const analysis = this.analyze(systemType);

    // Create nodes for different positions
    const nodes: PowerNode[] = [
      {
        id: "platform",
        label: "Platform/Institution",
        type: "position",
        measurability: analysis.confidence,
        metadata: { role: "power_holder" }
      },
      {
        id: "user",
        label: "User/Subject",
        type: "position",
        measurability: analysis.confidence,
        metadata: { role: "subject" }
      },
      {
        id: "surveillance",
        label: "Surveillance Mechanism",
        type: "mechanism",
        metadata: { foucault_concept: "panopticon" }
      },
      {
        id: "normalization",
        label: "Normalization",
        type: "mechanism",
        metadata: { foucault_concept: "discipline" }
      }
    ];

    // Create edges for power relations
    const edges: PowerEdge[] = [
      {
        from: "platform",
        to: "user",
        label: "Data Collection",
        direction: PowerDirection.TOP_DOWN,
        resistance_points: ["Privacy settings", "Regulations", "User awareness"]
      },
      {
        from: "user",
        to: "user",
        label: "Self-surveillance",
        direction: PowerDirection.CIRCULAR,
        resistance_points: ["Critical awareness", "Collective resistance"]
      }
    ];

    // Metrics
    const metrics: PowerMetrics = {
      total_privileges: analysis.total_privileges,
      measurable_privileges: analysis.measurable_privileges,
      power_density: analysis.power_characteristics.power_density,
      surveillance_intensity: analysis.power_characteristics.surveillance_intensity,
      knowledge_production: analysis.power_characteristics.produces_knowledge,
      overall_measurability: analysis.confidence
    };

    return {
      system_name: analysis.system_name,
      nodes,
      edges,
      metrics
    };
  }

  /**
   * Analyze systems by Foucauldian theme
   */
  static analyzeByTheme(theme: FoucaultConceptType): ThematicAnalysis {
    const themeDescriptions: Record<FoucaultConceptType, string> = {
      [FoucaultConceptType.SURVEILLANCE]: "Power through visibility and observation",
      [FoucaultConceptType.PANOPTICON]: "Architectural surveillance creating self-discipline",
      [FoucaultConceptType.POWER_KNOWLEDGE]: "Power and knowledge directly imply one another",
      [FoucaultConceptType.NORMALIZATION]: "Establishing standards and measuring deviations",
      [FoucaultConceptType.DISCIPLINE]: "Techniques for controlling and optimizing bodies",
      [FoucaultConceptType.BIOPOWER]: "Power over life, populations, and biology",
      [FoucaultConceptType.GOVERNMENTALITY]: "Art of government and population management",
      [FoucaultConceptType.RESISTANCE]: "Where there is power, there is resistance",
      [FoucaultConceptType.SUBJECTIFICATION]: "Power creates particular types of subjects"
    };

    // Mock implementation - in reality would analyze all systems
    const systems = [
      {
        system_name: "Social Media Surveillance System",
        relevance_score: 0.95,
        examples: [
          "Digital Panopticon",
          "Algorithmic Normalization",
          "Metrics and Analytics"
        ]
      },
      {
        system_name: "Educational Examination System",
        relevance_score: 0.90,
        examples: [
          "The Examination",
          "The Grade",
          "The Permanent Record"
        ]
      }
    ];

    return {
      theme,
      description: themeDescriptions[theme],
      systems
    };
  }

  /**
   * Get summary statistics across all systems
   */
  static getSummaryStatistics(): {
    total_systems: number;
    avg_measurability: number;
    most_measurable: string;
    least_measurable: string;
    foucault_concepts_demonstrated: string[];
  } {
    const systems = Object.values(PowerSystemType);
    const analyses = systems.map(s => this.analyze(s));

    const avgMeasurability = analyses.reduce((sum, a) => sum + a.confidence, 0) / analyses.length;
    const mostMeasurable = analyses.reduce((max, a) => a.confidence > max.confidence ? a : max);
    const leastMeasurable = analyses.reduce((min, a) => a.confidence < min.confidence ? a : min);

    return {
      total_systems: systems.length,
      avg_measurability: avgMeasurability,
      most_measurable: mostMeasurable.system_name,
      least_measurable: leastMeasurable.system_name,
      foucault_concepts_demonstrated: [
        "Surveillance and Panopticon",
        "Power/Knowledge",
        "Normalization",
        "Discipline",
        "Biopower",
        "Resistance"
      ]
    };
  }
}
