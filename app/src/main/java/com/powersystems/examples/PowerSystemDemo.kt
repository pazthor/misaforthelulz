package com.powersystems.examples

/**
 * Demo Principal - Sistemas de Poder
 *
 * Este demo ejecuta todos los ejemplos para demostrar el concepto:
 * "Los sistemas de poder son sistemas que cumplen un fin.
 *  Tienen privilegios que LIMITAN, y esos límites son MEDIBLES."
 */
object PowerSystemDemo {

    /**
     * Ejecuta todos los ejemplos y muestra los resultados
     */
    fun runFullDemo(): String {
        val output = StringBuilder()

        output.appendLine("""
            ╔════════════════════════════════════════════════════════════════╗
            ║   SISTEMAS DE PODER: Privilegios, Límites y Medición          ║
            ╚════════════════════════════════════════════════════════════════╝
        """.trimIndent())

        output.appendLine("\n${"-".repeat(64)}\n")

        // Ejemplo 1: File System
        output.appendLine("EJEMPLO 1: Sistema de Archivos")
        output.appendLine("${"-".repeat(64)}")
        val fileSystem = FileSystemPowerExample()
        val fsDemo = PowerSystemAnalyzer().demonstrateConcept(fileSystem)
        output.appendLine(fsDemo.conclusion)
        output.appendLine("\nLimitaciones demostradas:")
        fileSystem.demonstrateLimitations().forEach { (situation, limit) ->
            output.appendLine("  • $situation")
        }

        output.appendLine("\n${"-".repeat(64)}\n")

        // Ejemplo 2: Organización
        output.appendLine("EJEMPLO 2: Sistema Organizacional")
        output.appendLine("${"-".repeat(64)}")
        val juniorDev = OrganizationalPowerExample(OrganizationalRoles.createJuniorDeveloper())
        val manager = OrganizationalPowerExample(OrganizationalRoles.createEngineeringManager())

        val juniorAnalysis = PowerSystemAnalyzer().analyze(juniorDev)
        val managerAnalysis = PowerSystemAnalyzer().analyze(manager)

        output.appendLine("Desarrollador Junior:")
        output.appendLine("  Veredicto: ${juniorAnalysis.verdict}")
        output.appendLine("  Alcance: ${juniorAnalysis.minimumReach} - ${juniorAnalysis.maximumReach}")
        output.appendLine("  Confianza: ${(juniorAnalysis.confidence * 100).toInt()}%")

        output.appendLine("\nManager de Ingeniería:")
        output.appendLine("  Veredicto: ${managerAnalysis.verdict}")
        output.appendLine("  Alcance: ${managerAnalysis.minimumReach} - ${managerAnalysis.maximumReach}")
        output.appendLine("  Confianza: ${(managerAnalysis.confidence * 100).toInt()}%")

        output.appendLine("\n${"-".repeat(64)}\n")

        // Ejemplo 3: API System
        output.appendLine("EJEMPLO 3: Sistema de API (El más medible)")
        output.appendLine("${"-".repeat(64)}")

        val freeAPI = APIPermissionSystemExample(
            apiKey = "free_12345",
            scopes = setOf(APIScopes.createFreePublicScope()),
            rateLimitPerHour = 100
        )

        val apiAnalysis = PowerSystemAnalyzer().analyze(freeAPI)
        output.appendLine("API Gratuita:")
        output.appendLine("  Veredicto: ${apiAnalysis.verdict}")
        output.appendLine("  Confianza: ${(apiAnalysis.confidence * 100).toInt()}% ← ¡CASI CERTEZA TOTAL!")
        output.appendLine("\nLímites medibles exactos:")
        freeAPI.demonstrateAPLimits().forEach { (metric, value) ->
            output.appendLine("  • $metric: $value")
        }

        output.appendLine("\nFronteras claras:")
        freeAPI.showClearBoundaries().forEach { (type, endpoints) ->
            output.appendLine("  $type: ${endpoints.joinToString(", ")}")
        }

        output.appendLine("\n${"-".repeat(64)}\n")

        // Comparación: Medible vs Especulación
        output.appendLine("COMPARACIÓN FINAL: ¿Medible o Especulación?")
        output.appendLine("${"-".repeat(64)}")
        output.appendLine(AnalyzerExamples.demonstrateMeasurableVsSpeculation())

        output.appendLine("\n${"-".repeat(64)}\n")

        // Todos los análisis
        output.appendLine("RESUMEN DE TODOS LOS SISTEMAS")
        output.appendLine("${"-".repeat(64)}")
        val allAnalyses = AnalyzerExamples.runAllExamples()
        allAnalyses.forEach { (name, analysis) ->
            output.appendLine("""
                $name:
                  • ¿Medible? ${if (analysis.isMeasurable) "✓ SÍ" else "✗ NO"}
                  • ¿Especulación? ${if (analysis.isSpeculation) "✗ SÍ" else "✓ NO"}
                  • Confianza: ${(analysis.confidence * 100).toInt()}%
                  • Privilegios: ${analysis.privilegeCount}
                  • Límites: ${analysis.limitationCount}
            """.trimIndent())
            output.appendLine()
        }

        output.appendLine("\n${"-".repeat(64)}\n")

        // Conclusión final
        output.appendLine("""
            ╔════════════════════════════════════════════════════════════════╗
            ║                    CONCLUSIÓN FINAL                            ║
            ╚════════════════════════════════════════════════════════════════╝

            1. Los sistemas de poder NO son más que sistemas con un fin:
               ser un sistema.

            2. En sistemas de poder HAY PRIVILEGIOS.

            3. Esos privilegios LIMITAN el alcance de acción.

            4. Esos límites SON MEDIBLES (no es especulación):
               • Sistemas de archivos: 95% de confianza
               • Sistemas organizacionales: 70-90% de confianza
               • Sistemas de API: 98% de confianza ¡CASI CERTEZA!

            5. PODEMOS hacer estimaciones del alcance mínimo:
               • Rate limits: EXACTOS
               • Permisos: CONCRETOS
               • Budget: MEDIBLES
               • Accesos: DEFINIDOS

            6. La diferencia entre MEDIBLE y ESPECULACIÓN:
               • Medible: Tiene métricas, números, límites concretos
               • Especulación: Vago, subjetivo, sin forma de verificar

            Este código DEMUESTRA que no es un divague.
            Es MEDIBLE. Es CONCRETO. Es VERIFICABLE.

            ╔════════════════════════════════════════════════════════════════╗
            ║  Los privilegios limitan, y esos límites se pueden MEDIR.     ║
            ╚════════════════════════════════════════════════════════════════╝
        """.trimIndent())

        return output.toString()
    }

    /**
     * Comparación rápida entre dos sistemas
     */
    fun quickCompare(system1: PowerSystem, system2: PowerSystem): String {
        val analyzer = PowerSystemAnalyzer()
        val comparison = analyzer.compare(system1, system2)

        return """
            Comparación de Sistemas:

            ${comparison.comparison}

            Sistema más medible: ${comparison.moreMeasurable}
            Sistema con más privilegios: ${comparison.morePrivileges}
            Sistema con más limitaciones: ${comparison.moreLimitations}
        """.trimIndent()
    }

    /**
     * Análisis individual de un sistema
     */
    fun analyzeSingle(system: PowerSystem): String {
        val analyzer = PowerSystemAnalyzer()
        val analysis = analyzer.analyze(system)

        return """
            Análisis de ${analysis.systemName}:

            Veredicto: ${analysis.verdict}

            Métricas:
            • ¿Es medible? ${analysis.isMeasurable}
            • ¿Es especulación? ${analysis.isSpeculation}
            • ¿Es confiable? ${analysis.isReliable}
            • Alcance mínimo: ${analysis.minimumReach}
            • Alcance máximo: ${analysis.maximumReach}
            • Confianza: ${(analysis.confidence * 100).toInt()}%
            • Privilegios: ${analysis.privilegeCount}
            • Limitaciones: ${analysis.limitationCount}

            Razonamiento:
            ${analysis.reasoning}
        """.trimIndent()
    }
}

/**
 * Punto de entrada para ejecutar el demo
 *
 * Uso:
 * val output = PowerSystemDemo.runFullDemo()
 * println(output)
 */
fun main() {
    println(PowerSystemDemo.runFullDemo())
}
