package com.powersystems.examples

/**
 * Ejemplo 1: Sistema de Archivos como Sistema de Poder
 *
 * Un sistema de archivos es un sistema de poder donde:
 * - Los privilegios (read, write, execute) LIMITAN lo que puedes hacer
 * - Podemos MEDIR exactamente el alcance de cada privilegio
 * - NO es especulación, es medible y concreto
 */
class FileSystemPowerExample : PowerSystem {
    override val name = "Sistema de Archivos Unix"

    override val privileges = setOf(
        Privilege(
            name = "READ",
            scope = PrivilegeScope.LIMITED,
            actions = setOf("open", "read", "list"),
            limitations = listOf(
                "No puede modificar contenido",
                "No puede cambiar permisos",
                "Solo acceso de lectura"
            )
        ),
        Privilege(
            name = "WRITE",
            scope = PrivilegeScope.LIMITED,
            actions = setOf("write", "append", "truncate"),
            limitations = listOf(
                "No puede leer sin permiso READ",
                "No puede ejecutar",
                "Limitado por cuota de disco"
            )
        ),
        Privilege(
            name = "EXECUTE",
            scope = PrivilegeScope.RESTRICTED,
            actions = setOf("execute", "run"),
            limitations = listOf(
                "Requiere permisos de lectura",
                "Limitado por recursos del sistema",
                "Subject to security policies"
            )
        )
    )

    override fun canPerform(action: String): Boolean {
        return privileges.any { it.actions.contains(action) }
    }

    override fun getLimitations(): List<String> {
        return privileges.flatMap { it.limitations }
    }

    override fun estimateMinimumReach(): ReachEstimation {
        // En un sistema de archivos, podemos MEDIR exactamente:
        // - Cuántos archivos podemos acceder
        // - Qué operaciones podemos realizar
        // - Los límites son CONCRETOS, no especulativos

        val measurableActions = privileges.flatMap { it.actions }.size
        val limitations = getLimitations().size

        return ReachEstimation(
            isMeasurable = true,
            minimumImpact = measurableActions,
            maximumImpact = measurableActions * 10, // Estimación basada en archivos accesibles
            confidence = 0.95, // Alta confianza porque es medible
            reasoning = """
                Sistema de archivos Unix tiene privilegios MEDIBLES:
                - ${privileges.size} tipos de privilegios definidos
                - ${measurableActions} acciones concretas permitidas
                - ${limitations} limitaciones explícitas

                NO ES ESPECULACIÓN: Cada privilegio tiene un alcance definido
                y medible. Podemos contar exactamente qué archivos y qué
                operaciones están permitidas.
            """.trimIndent()
        )
    }

    /**
     * Demuestra que los privilegios LIMITAN el alcance
     */
    fun demonstrateLimitations(): Map<String, String> {
        return mapOf(
            "READ sin WRITE" to "Puedes ver pero NO modificar → LÍMITE MEDIBLE",
            "WRITE sin EXECUTE" to "Puedes crear scripts pero NO ejecutarlos → LÍMITE CONCRETO",
            "EXECUTE sin READ" to "En algunos sistemas ni siquiera puedes ejecutar → RESTRICCIÓN REAL",
            "Sin privilegios" to "Alcance = 0, completamente medible"
        )
    }
}
