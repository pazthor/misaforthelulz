/**
 * TypeScript types for Foucault Power Systems Framework
 *
 * These types correspond to the Python implementation.
 */

export enum PrivilegeScope {
  GLOBAL = "global",
  LIMITED = "limited",
  RESTRICTED = "restricted",
  NONE = "none"
}

export enum PowerDirection {
  TOP_DOWN = "top_down",
  BOTTOM_UP = "bottom_up",
  LATERAL = "lateral",
  CIRCULAR = "circular",
  CAPILLARY = "capillary"
}

export interface Privilege {
  name: string;
  scope: PrivilegeScope;
  description: string;
  limitations: string[];
  produces: string[];
}

export interface PowerRelation {
  from_position: string;
  to_position: string;
  privilege: Privilege;
  direction: PowerDirection;
  resistance_points: string[];
}

export interface DisciplinaryMechanism {
  name: string;
  mechanism_type: string;
  observes: string[];
  normalizes_to: string | null;
  produces_knowledge: boolean;
  visibility_pattern: "panopticon" | "distributed" | "self-surveillance" | "examination";
}

export interface ReachEstimation {
  is_measurable: boolean;
  minimum_impact: number;
  maximum_impact: number;
  confidence: number;
  reasoning: string;
  measurement_type: string;
}

export interface PowerSystem {
  name: string;
  description: string;
  privileges: Privilege[];
  power_relations: PowerRelation[];
  disciplinary_mechanisms: DisciplinaryMechanism[];
  reach_estimations: Map<string, ReachEstimation>;
}

export interface SystemAnalysis {
  system_name: string;
  is_measurable: boolean;
  confidence: number;
  minimum_reach: number;
  maximum_reach: number;
  measurable_privileges: number;
  total_privileges: number;
  verdict: "✓ MEASURABLE" | "~ ESTIMABLE" | "✗ SPECULATION";
  reasoning: string;
  power_characteristics: {
    power_density: number;
    surveillance_intensity: number;
    produces_knowledge: boolean;
    disciplinary_count: number;
    total_relations: number;
  };
}

export interface ComparisonResult {
  system1: SystemAnalysis;
  system2: SystemAnalysis;
  comparison_text: string;
}

/**
 * Foucauldian concepts as structured data
 */
export interface FoucaultConcept {
  name: string;
  description: string;
  examples_in_system: string[];
  measurability: number;
}

/**
 * Power analysis result for visualization
 */
export interface PowerAnalysisVisualization {
  system_name: string;
  nodes: PowerNode[];
  edges: PowerEdge[];
  metrics: PowerMetrics;
}

export interface PowerNode {
  id: string;
  label: string;
  type: "position" | "privilege" | "mechanism";
  measurability?: number;
  metadata: Record<string, any>;
}

export interface PowerEdge {
  from: string;
  to: string;
  label: string;
  direction: PowerDirection;
  resistance_points: string[];
}

export interface PowerMetrics {
  total_privileges: number;
  measurable_privileges: number;
  power_density: number;
  surveillance_intensity: number;
  knowledge_production: boolean;
  overall_measurability: number;
}

/**
 * Available power system types
 */
export enum PowerSystemType {
  SOCIAL_MEDIA_SURVEILLANCE = "SocialMediaSurveillanceSystem",
  WORKPLACE_SURVEILLANCE = "WorkplaceSurveillanceSystem",
  EDUCATIONAL = "EducationalSystem",
  ACADEMIC_PUBLISHING = "AcademicPublishingSystem",
  PUBLIC_HEALTH = "PublicHealthSystem",
  FITNESS_TRACKING = "FitnessTrackingSystem"
}

/**
 * Analysis request configuration
 */
export interface AnalysisConfig {
  system_type: PowerSystemType;
  detailed: boolean;
  compare_with?: PowerSystemType;
  focus_concepts?: FoucaultConceptType[];
}

/**
 * Foucault's key concepts for analysis focus
 */
export enum FoucaultConceptType {
  SURVEILLANCE = "surveillance",
  PANOPTICON = "panopticon",
  POWER_KNOWLEDGE = "power_knowledge",
  NORMALIZATION = "normalization",
  DISCIPLINE = "discipline",
  BIOPOWER = "biopower",
  GOVERNMENTALITY = "governmentality",
  RESISTANCE = "resistance",
  SUBJECTIFICATION = "subjectification"
}

/**
 * Thematic analysis result
 */
export interface ThematicAnalysis {
  theme: FoucaultConceptType;
  description: string;
  systems: {
    system_name: string;
    relevance_score: number;
    examples: string[];
  }[];
}
