#!/usr/bin/env ts-node
/**
 * CLI for Foucault Power Systems Analysis
 *
 * Usage:
 *   npm run analyze -- <command> [options]
 *
 * Commands:
 *   analyze <system>     - Analyze a single power system
 *   compare <s1> <s2>    - Compare two power systems
 *   theme <concept>      - Analyze by Foucauldian theme
 *   summary              - Get summary statistics
 */

import { PowerSystemAnalyzer } from './analyzer';
import { PowerSystemType, FoucaultConceptType } from './types';

const SYSTEMS_MAP: Record<string, PowerSystemType> = {
  'social-media': PowerSystemType.SOCIAL_MEDIA_SURVEILLANCE,
  'workplace': PowerSystemType.WORKPLACE_SURVEILLANCE,
  'education': PowerSystemType.EDUCATIONAL,
  'academic': PowerSystemType.ACADEMIC_PUBLISHING,
  'health': PowerSystemType.PUBLIC_HEALTH,
  'fitness': PowerSystemType.FITNESS_TRACKING
};

const THEMES_MAP: Record<string, FoucaultConceptType> = {
  'surveillance': FoucaultConceptType.SURVEILLANCE,
  'panopticon': FoucaultConceptType.PANOPTICON,
  'power-knowledge': FoucaultConceptType.POWER_KNOWLEDGE,
  'normalization': FoucaultConceptType.NORMALIZATION,
  'discipline': FoucaultConceptType.DISCIPLINE,
  'biopower': FoucaultConceptType.BIOPOWER,
  'resistance': FoucaultConceptType.RESISTANCE
};

function printHeader(title: string) {
  console.log('\n' + '='.repeat(80));
  console.log(title.toUpperCase().padStart(40 + title.length / 2));
  console.log('='.repeat(80) + '\n');
}

function printHelp() {
  console.log(`
╔══════════════════════════════════════════════════════════════════════════════╗
║                FOUCAULT POWER SYSTEMS ANALYZER - CLI                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

USAGE:
  npm run analyze -- <command> [options]

COMMANDS:

  analyze <system>
    Analyze a single power system

    Systems:
      social-media   - Social Media Surveillance System
      workplace      - Workplace Surveillance System
      education      - Educational Examination System
      academic       - Academic Publishing System
      health         - Public Health Biopower System
      fitness        - Fitness Tracking System

    Example: npm run analyze -- analyze social-media

  compare <system1> <system2>
    Compare two power systems

    Example: npm run analyze -- compare education workplace

  theme <concept>
    Analyze systems by Foucauldian theme

    Themes:
      surveillance      - Power through observation
      panopticon       - Architectural surveillance
      power-knowledge  - Power/knowledge relationship
      normalization    - Establishing norms
      discipline       - Control techniques
      biopower         - Power over life
      resistance       - Points of resistance

    Example: npm run analyze -- theme surveillance

  summary
    Display summary statistics across all systems

    Example: npm run analyze -- summary

  visualize <system>
    Generate visualization data for a system

    Example: npm run analyze -- visualize social-media

  help
    Display this help message

EXAMPLES:

  # Analyze social media surveillance
  npm run analyze -- analyze social-media

  # Compare education and workplace systems
  npm run analyze -- compare education workplace

  # Analyze surveillance theme across systems
  npm run analyze -- theme surveillance

  # Get summary of all systems
  npm run analyze -- summary

ABOUT:

This CLI tool provides TypeScript-based analysis of power systems through
Michel Foucault's theoretical framework. It demonstrates how abstract
philosophical concepts can be analyzed through concrete, measurable systems.

"Power is everywhere; not because it embraces everything, but because
it comes from everywhere." — Michel Foucault

`);
}

function analyzeSystem(systemKey: string) {
  const systemType = SYSTEMS_MAP[systemKey];
  if (!systemType) {
    console.error(`Unknown system: ${systemKey}`);
    console.log(`Available systems: ${Object.keys(SYSTEMS_MAP).join(', ')}`);
    return;
  }

  printHeader(`Analyzing: ${systemKey}`);

  const analysis = PowerSystemAnalyzer.analyze(systemType);

  console.log(`System: ${analysis.system_name}`);
  console.log(`Verdict: ${analysis.verdict}`);
  console.log(`Confidence: ${(analysis.confidence * 100).toFixed(0)}%`);
  console.log(`\nMeasurable Privileges: ${analysis.measurable_privileges}/${analysis.total_privileges}`);
  console.log(`Reach: ${analysis.minimum_reach.toLocaleString()} - ${analysis.maximum_reach.toLocaleString()}`);
  console.log(`\nReasoning: ${analysis.reasoning}`);

  console.log('\nPower Characteristics:');
  console.log(`  Power Density: ${analysis.power_characteristics.power_density.toFixed(2)}`);
  console.log(`  Surveillance Intensity: ${(analysis.power_characteristics.surveillance_intensity * 100).toFixed(0)}%`);
  console.log(`  Produces Knowledge: ${analysis.power_characteristics.produces_knowledge ? 'Yes' : 'No'}`);
  console.log(`  Disciplinary Mechanisms: ${analysis.power_characteristics.disciplinary_count}`);
  console.log(`  Power Relations: ${analysis.power_characteristics.total_relations}`);
}

function compareSystems(system1Key: string, system2Key: string) {
  const system1 = SYSTEMS_MAP[system1Key];
  const system2 = SYSTEMS_MAP[system2Key];

  if (!system1 || !system2) {
    console.error('Invalid system(s)');
    console.log(`Available systems: ${Object.keys(SYSTEMS_MAP).join(', ')}`);
    return;
  }

  printHeader('Power System Comparison');
  console.log(PowerSystemAnalyzer.compare(system1, system2));
}

function analyzeTheme(themeKey: string) {
  const theme = THEMES_MAP[themeKey];
  if (!theme) {
    console.error(`Unknown theme: ${themeKey}`);
    console.log(`Available themes: ${Object.keys(THEMES_MAP).join(', ')}`);
    return;
  }

  printHeader(`Thematic Analysis: ${themeKey}`);

  const analysis = PowerSystemAnalyzer.analyzeByTheme(theme);

  console.log(`Theme: ${theme}`);
  console.log(`Description: ${analysis.description}\n`);

  console.log('Systems demonstrating this theme:\n');
  for (const system of analysis.systems) {
    console.log(`${system.system_name} (Relevance: ${(system.relevance_score * 100).toFixed(0)}%)`);
    console.log('  Examples:');
    for (const example of system.examples) {
      console.log(`    • ${example}`);
    }
    console.log();
  }
}

function showSummary() {
  printHeader('Summary Statistics');

  const stats = PowerSystemAnalyzer.getSummaryStatistics();

  console.log(`Total Systems Analyzed: ${stats.total_systems}`);
  console.log(`Average Measurability: ${(stats.avg_measurability * 100).toFixed(0)}%`);
  console.log(`\nMost Measurable: ${stats.most_measurable}`);
  console.log(`Least Measurable: ${stats.least_measurable}`);

  console.log('\nFoucauldian Concepts Demonstrated:');
  for (const concept of stats.foucault_concepts_demonstrated) {
    console.log(`  • ${concept}`);
  }

  console.log('\n' + '-'.repeat(80));
  console.log('\nKey Insight:');
  console.log('Power systems vary in measurability, but Foucault\'s concepts help us');
  console.log('analyze power even when it appears diffuse or invisible. The most');
  console.log('effective power often operates through self-discipline rather than');
  console.log('external force.\n');
}

function visualizeSystem(systemKey: string) {
  const systemType = SYSTEMS_MAP[systemKey];
  if (!systemType) {
    console.error(`Unknown system: ${systemKey}`);
    console.log(`Available systems: ${Object.keys(SYSTEMS_MAP).join(', ')}`);
    return;
  }

  printHeader(`Visualization: ${systemKey}`);

  const viz = PowerSystemAnalyzer.visualize(systemType);

  console.log(`System: ${viz.system_name}\n`);

  console.log('NODES (Positions and Mechanisms):');
  for (const node of viz.nodes) {
    console.log(`  [${node.type}] ${node.label}`);
    if (node.measurability !== undefined) {
      console.log(`    Measurability: ${(node.measurability * 100).toFixed(0)}%`);
    }
  }

  console.log('\nEDGES (Power Relations):');
  for (const edge of viz.edges) {
    console.log(`  ${edge.from} → ${edge.to}`);
    console.log(`    Privilege: ${edge.label}`);
    console.log(`    Direction: ${edge.direction}`);
    console.log(`    Resistance: ${edge.resistance_points.join(', ')}`);
  }

  console.log('\nMETRICS:');
  console.log(`  Total Privileges: ${viz.metrics.total_privileges}`);
  console.log(`  Measurable: ${viz.metrics.measurable_privileges}`);
  console.log(`  Power Density: ${viz.metrics.power_density.toFixed(2)}`);
  console.log(`  Surveillance Intensity: ${(viz.metrics.surveillance_intensity * 100).toFixed(0)}%`);
  console.log(`  Knowledge Production: ${viz.metrics.knowledge_production ? 'Yes' : 'No'}`);
  console.log(`  Overall Measurability: ${(viz.metrics.overall_measurability * 100).toFixed(0)}%`);
}

// Main CLI logic
const args = process.argv.slice(2);
const command = args[0];

switch (command) {
  case 'analyze':
    if (!args[1]) {
      console.error('Please specify a system to analyze');
      printHelp();
    } else {
      analyzeSystem(args[1]);
    }
    break;

  case 'compare':
    if (!args[1] || !args[2]) {
      console.error('Please specify two systems to compare');
      printHelp();
    } else {
      compareSystems(args[1], args[2]);
    }
    break;

  case 'theme':
    if (!args[1]) {
      console.error('Please specify a theme to analyze');
      printHelp();
    } else {
      analyzeTheme(args[1]);
    }
    break;

  case 'summary':
    showSummary();
    break;

  case 'visualize':
    if (!args[1]) {
      console.error('Please specify a system to visualize');
      printHelp();
    } else {
      visualizeSystem(args[1]);
    }
    break;

  case 'help':
  default:
    printHelp();
    break;
}
