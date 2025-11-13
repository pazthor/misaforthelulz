package com.powersystems.examples

/**
 * Analizador de Sistemas de Poder
 *
 * Herramienta para demostrar que:
 * 1. Los privilegios LIMITAN el alcance
 * 2. Ese límite es MEDIBLE (no especulación)
 * 3. Podemos hacer estimaciones mínimas concretas
 */
class PowerSystemAnalyzer {

    /**
     * Analiza un sistema de poder y determina si es medible o especulativo
     */
    fun analyze(system: PowerSystem): SystemAnalysis {
        val estimation = system.estimateMinimumReach()
        val limitations = system.getLimitations()
        val privilegeCount = system.privileges.size

        return SystemAnalysis(
            systemName = system.name,
            isMeasurable = estimation.isMeasurable,
            isSpeculation = estimation.isSpeculation(),
            isReliable = estimation.isReliable(),
            minimumReach = estimation.minimumImpact,
            maximumReach = estimation.maximumImpact,
            confidence = estimation.confidence,
            privilegeCount = privilegeCount,
            limitationCount = limitations.size,
            verdict = determineVerdict(estimation, privilegeCount, limitations.size),
            reasoning = estimation.reasoning
        )
    }

    /**
     * Compara dos sistemas de poder
     */
    fun compare(system1: PowerSystem, system2: PowerSystem): ComparisonResult {
        val analysis1 = analyze(system1)
        val analysis2 = analyze(system2)

        return ComparisonResult(
            system1 = analysis1,
            system2 = analysis2,
            moreMeasurable = if (analysis1.confidence > analysis2.confidence) system1.name else system2.name,
            morePrivileges = if (analysis1.privilegeCount > analysis2.privilegeCount) system1.name else system2.name,
            moreLimitations = if (analysis1.limitationCount > analysis2.limitationCount) system1.name else system2.name,
            comparison = buildComparisonSummary(analysis1, analysis2)
        )
    }

    /**
     * Demuestra el concepto principal: privilegios → límites → medición
     */
    fun demonstrateConcept(system: PowerSystem): ConceptDemonstration {
        val privileges = system.privileges
        val limitations = system.getLimitations()
        val estimation = system.estimateMinimumReach()

        return ConceptDemonstration(
            step1_Privileges = privileges.map {
                "${it.name}: ${it.actions.size} acciones permitidas"
            },
            step2_Limitations = limitations.map {
                "LÍMITE: $it"
            },
            step3_Measurement = mapOf(
                "¿Es medible?" to estimation.isMeasurable.toString(),
                "Alcance mínimo" to estimation.minimumImpact.toString(),
                "Alcance máximo" to estimation.maximumImpact.toString(),
                "Confianza" to "${(estimation.confidence * 100).toInt()}%",
                "¿Especulación?" to estimation.isSpeculation().toString()
            ),
            conclusion = """
                ${system.name}:
                - Tiene ${privileges.size} privilegios definidos
                - Estos generan ${limitations.size} limitaciones
                - El alcance ${if (estimation.isMeasurable) "SÍ" else "NO"} es medible
                - Confianza: ${(estimation.confidence * 100).toInt()}%
                - Veredicto: ${if (estimation.isReliable()) "MEDIBLE Y CONFIABLE" else if (estimation.isMeasurable) "MEDIBLE PERO BAJA CONFIANZA" else "PURA ESPECULACIÓN"}
            """.trimIndent()
        )
    }

    private fun determineVerdict(
        estimation: ReachEstimation,
        privilegeCount: Int,
        limitationCount: Int
    ): String {
        return when {
            estimation.isReliable() && limitationCount > 0 ->
                "✓ SISTEMA MEDIBLE - Privilegios claros con límites concretos"

            estimation.isMeasurable && !estimation.isSpeculation() ->
                "~ ESTIMABLE - Privilegios medibles pero con cierta incertidumbre"

            estimation.isSpeculation() ->
                "✗ ESPECULACIÓN - No hay forma confiable de medir el alcance"

            privilegeCount == 0 ->
                "✗ SIN PRIVILEGIOS - Alcance = 0 (perfectamente medible)"

            else ->
                "? INDETERMINADO - Requiere más análisis"
        }
    }

    private fun buildComparisonSummary(a1: SystemAnalysis, a2: SystemAnalysis): String {
        return """
            Comparación de Sistemas de Poder:

            ${a1.systemName}:
            - Medible: ${a1.isMeasurable}
            - Confianza: ${(a1.confidence * 100).toInt()}%
            - Privilegios: ${a1.privilegeCount}
            - Límites: ${a1.limitationCount}

            ${a2.systemName}:
            - Medible: ${a2.isMeasurable}
            - Confianza: ${(a2.confidence * 100).toInt()}%
            - Privilegios: ${a2.privilegeCount}
            - Límites: ${a2.limitationCount}

            Conclusión:
            ${if (a1.confidence > a2.confidence) a1.systemName else a2.systemName}
            es más medible y concreto.
        """.trimIndent()
    }
}

/**
 * Resultado del análisis de un sistema
 */
data class SystemAnalysis(
    val systemName: String,
    val isMeasurable: Boolean,
    val isSpeculation: Boolean,
    val isReliable: Boolean,
    val minimumReach: Int,
    val maximumReach: Int,
    val confidence: Double,
    val privilegeCount: Int,
    val limitationCount: Int,
    val verdict: String,
    val reasoning: String
)

/**
 * Resultado de comparación entre sistemas
 */
data class ComparisonResult(
    val system1: SystemAnalysis,
    val system2: SystemAnalysis,
    val moreMeasurable: String,
    val morePrivileges: String,
    val moreLimitations: String,
    val comparison: String
)

/**
 * Demostración del concepto privilegios → límites → medición
 */
data class ConceptDemonstration(
    val step1_Privileges: List<String>,
    val step2_Limitations: List<String>,
    val step3_Measurement: Map<String, String>,
    val conclusion: String
)

/**
 * Ejemplos de uso del analizador
 */
object AnalyzerExamples {
    fun runAllExamples(): Map<String, SystemAnalysis> {
        val analyzer = PowerSystemAnalyzer()

        return mapOf(
            "FileSystem" to analyzer.analyze(FileSystemPowerExample()),
            "Organization_Junior" to analyzer.analyze(
                OrganizationalPowerExample(OrganizationalRoles.createJuniorDeveloper())
            ),
            "Organization_Manager" to analyzer.analyze(
                OrganizationalPowerExample(OrganizationalRoles.createEngineeringManager())
            ),
            "API_Free" to analyzer.analyze(
                APIPermissionSystemExample(
                    apiKey = "free_key_123",
                    scopes = setOf(APIScopes.createFreePublicScope()),
                    rateLimitPerHour = 100
                )
            ),
            "API_Paid" to analyzer.analyze(
                APIPermissionSystemExample(
                    apiKey = "paid_key_456",
                    scopes = setOf(
                        APIScopes.createFreePublicScope(),
                        APIScopes.createPaidAnalyticsScope()
                    ),
                    rateLimitPerHour = 10000
                )
            ),
            "API_Admin" to analyzer.analyze(
                APIPermissionSystemExample(
                    apiKey = "admin_key_789",
                    scopes = setOf(APIScopes.createAdminScope()),
                    rateLimitPerHour = 100000
                )
            )
        )
    }

    /**
     * Muestra claramente la diferencia entre medible y especulativo
     */
    fun demonstrateMeasurableVsSpeculation(): String {
        val scenarios = MeasurableVsSpeculation.compareScenarios()

        val measurable = scenarios.filter { it.value.first }
        val speculation = scenarios.filter { !it.value.first }

        return """
            ═══════════════════════════════════════════════════
            MEDIBLE vs ESPECULACIÓN
            ═══════════════════════════════════════════════════

            ✓ MEDIBLE (${measurable.size} ejemplos):
            ${measurable.entries.joinToString("\n") { "  - ${it.key}: ${it.value.second}" }}

            ✗ ESPECULACIÓN (${speculation.size} ejemplos):
            ${speculation.entries.joinToString("\n") { "  - ${it.key}: ${it.value.second}" }}

            ═══════════════════════════════════════════════════
            CONCLUSIÓN:
            Los sistemas de poder con privilegios claros son MEDIBLES.
            Los conceptos vagos sin métricas son ESPECULACIÓN.
            ═══════════════════════════════════════════════════
        """.trimIndent()
    }
}
