package com.powersystems.examples

/**
 * Sistema de Poder Base
 *
 * Un sistema de poder es simplemente un sistema que cumple un fin.
 * Todo sistema tiene privilegios que definen sus límites.
 */
interface PowerSystem {
    val name: String
    val privileges: Set<Privilege>

    /**
     * Estima el alcance mínimo del sistema basado en sus privilegios
     */
    fun estimateMinimumReach(): ReachEstimation

    /**
     * Verifica si una acción está dentro de los privilegios
     */
    fun canPerform(action: String): Boolean

    /**
     * Obtiene las limitaciones impuestas por los privilegios
     */
    fun getLimitations(): List<String>
}

/**
 * Privilegio en un sistema
 * Los privilegios definen qué puede hacer un sistema y qué no
 */
data class Privilege(
    val name: String,
    val scope: PrivilegeScope,
    val actions: Set<String>,
    val limitations: List<String>
)

/**
 * Alcance del privilegio
 */
enum class PrivilegeScope {
    GLOBAL,      // Sin restricciones de alcance
    LIMITED,     // Alcance limitado
    RESTRICTED,  // Altamente restringido
    NONE         // Sin privilegios
}

/**
 * Estimación del alcance
 * Permite determinar si es medible o solo especulación
 */
data class ReachEstimation(
    val isMeasurable: Boolean,
    val minimumImpact: Int,  // Impacto mínimo medible
    val maximumImpact: Int,  // Impacto máximo estimado
    val confidence: Double,   // Nivel de confianza (0.0 a 1.0)
    val reasoning: String     // Razonamiento detrás de la estimación
) {
    fun isSpeculation(): Boolean = !isMeasurable || confidence < 0.5

    fun isReliable(): Boolean = isMeasurable && confidence >= 0.7
}
