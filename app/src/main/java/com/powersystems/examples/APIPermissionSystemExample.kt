package com.powersystems.examples

/**
 * Ejemplo 3: Sistema de Permisos API como Sistema de Poder
 *
 * Los sistemas de API demuestran claramente:
 * - Privilegios = Scopes de OAuth, API Keys, Roles
 * - Límites = Rate limits, endpoints permitidos, data access
 * - Medición = Exactamente cuántas llamadas, qué datos, qué recursos
 */
class APIPermissionSystemExample(
    private val apiKey: String,
    private val scopes: Set<APIScope>,
    private val rateLimitPerHour: Int
) : PowerSystem {

    override val name = "Sistema de API - Key: ${apiKey.take(8)}..."

    override val privileges: Set<Privilege> = scopes.map { scope ->
        Privilege(
            name = scope.name,
            scope = when {
                scope.isPaid -> PrivilegeScope.GLOBAL
                scope.allowedEndpoints.size > 10 -> PrivilegeScope.LIMITED
                else -> PrivilegeScope.RESTRICTED
            },
            actions = scope.allowedEndpoints.toSet(),
            limitations = buildList {
                add("Rate limit: $rateLimitPerHour requests/hour")
                if (!scope.isPaid) add("Solo endpoints públicos")
                if (scope.requiresAuth) add("Requiere autenticación")
                scope.dataAccessLimits.forEach { add("Límite de datos: $it") }
            }
        )
    }.toSet()

    override fun canPerform(action: String): Boolean {
        // Cuenta las llamadas realizadas para verificar rate limit
        return scopes.any { it.allowedEndpoints.contains(action) } &&
                getCurrentHourCalls() < rateLimitPerHour
    }

    override fun getLimitations(): List<String> {
        return privileges.flatMap { it.limitations }
    }

    override fun estimateMinimumReach(): ReachEstimation {
        // En APIs, el alcance es EXTREMADAMENTE medible
        // Sabemos EXACTAMENTE cuántas llamadas, qué endpoints, qué datos

        val allowedEndpoints = scopes.flatMap { it.allowedEndpoints }.distinct().size
        val dataRows = scopes.sumOf { it.maxDataRowsPerRequest }

        val minimumImpact = rateLimitPerHour // Mínimo: tus propias llamadas
        val maximumImpact = rateLimitPerHour * allowedEndpoints * 30 // Máx: un mes de uso completo

        return ReachEstimation(
            isMeasurable = true,
            minimumImpact = minimumImpact,
            maximumImpact = maximumImpact,
            confidence = 0.98, // CASI certeza total
            reasoning = """
                Sistema de API tiene privilegios PERFECTAMENTE medibles:
                - Rate limit EXACTO: $rateLimitPerHour requests/hora
                - Endpoints permitidos CONCRETOS: $allowedEndpoints endpoints
                - Datos por request DEFINIDOS: $dataRows filas máximo
                - Scopes EXPLÍCITOS: ${scopes.size} scopes

                Este es el ejemplo MÁS CLARO de que los privilegios LIMITAN
                y ese límite es 100% MEDIBLE, NO especulación.

                Puedes calcular EXACTAMENTE:
                - Cuánta data puedes acceder por día
                - Qué operaciones puedes realizar
                - Dónde terminan tus privilegios
            """.trimIndent()
        )
    }

    /**
     * Demuestra límites de API medibles y concretos
     */
    fun demonstrateAPLimits(): Map<String, Int> {
        return mapOf(
            "Llamadas máximas por hora" to rateLimitPerHour,
            "Endpoints accesibles" to scopes.flatMap { it.allowedEndpoints }.distinct().size,
            "Filas de datos por request" to scopes.maxOf { it.maxDataRowsPerRequest },
            "Alcance máximo en 24h" to (rateLimitPerHour * 24),
            "Datos máximos por día (filas)" to (rateLimitPerHour * 24 * scopes.maxOf { it.maxDataRowsPerRequest })
        )
    }

    /**
     * Muestra qué SÍ puedes hacer vs qué NO puedes hacer
     */
    fun showClearBoundaries(): Map<String, List<String>> {
        val allPossibleEndpoints = listOf(
            "/users", "/posts", "/admin", "/analytics",
            "/payments", "/private", "/public", "/reports"
        )

        val allowed = scopes.flatMap { it.allowedEndpoints }
        val denied = allPossibleEndpoints.filter { it !in allowed }

        return mapOf(
            "PERMITIDO (medible)" to allowed,
            "DENEGADO (límite claro)" to denied
        )
    }

    // Simulación de contador de llamadas
    private var callsThisHour = 0
    private fun getCurrentHourCalls() = callsThisHour
}

/**
 * Scope de API con privilegios específicos
 */
data class APIScope(
    val name: String,
    val allowedEndpoints: List<String>,
    val isPaid: Boolean,
    val requiresAuth: Boolean,
    val maxDataRowsPerRequest: Int,
    val dataAccessLimits: List<String>
)

/**
 * Factory para crear ejemplos de API scopes
 */
object APIScopes {
    fun createFreePublicScope() = APIScope(
        name = "public:read",
        allowedEndpoints = listOf("/public", "/posts", "/users"),
        isPaid = false,
        requiresAuth = false,
        maxDataRowsPerRequest = 100,
        dataAccessLimits = listOf(
            "Solo datos públicos",
            "Máximo 100 filas por request",
            "No incluye datos sensibles"
        )
    )

    fun createPaidAnalyticsScope() = APIScope(
        name = "analytics:read",
        allowedEndpoints = listOf("/analytics", "/reports", "/metrics", "/dashboards"),
        isPaid = true,
        requiresAuth = true,
        maxDataRowsPerRequest = 10000,
        dataAccessLimits = listOf(
            "Requiere suscripción Pro",
            "Incluye métricas privadas",
            "Datos históricos de 2 años"
        )
    )

    fun createAdminScope() = APIScope(
        name = "admin:*",
        allowedEndpoints = listOf("/admin", "/users", "/posts", "/analytics", "/config", "/system"),
        isPaid = true,
        requiresAuth = true,
        maxDataRowsPerRequest = 50000,
        dataAccessLimits = listOf(
            "Acceso completo",
            "Puede modificar configuración",
            "Sin límites de datos históricos"
        )
    )
}

/**
 * Ejemplo que demuestra la diferencia entre especulación y medición
 */
class MeasurableVsSpeculation {
    companion object {
        fun compareScenarios(): Map<String, Pair<Boolean, String>> {
            return mapOf(
                "Rate limit de 100 req/h" to Pair(
                    true,
                    "MEDIBLE: Puedes contar exactamente 100 requests"
                ),
                "Acceso a /users y /posts" to Pair(
                    true,
                    "MEDIBLE: Lista exacta de 2 endpoints"
                ),
                "Máximo 1000 filas por request" to Pair(
                    true,
                    "MEDIBLE: 1000 es un número concreto"
                ),
                "Influencia en la organización" to Pair(
                    false,
                    "ESPECULACIÓN: No se puede medir exactamente"
                ),
                "Impacto cultural del proyecto" to Pair(
                    false,
                    "ESPECULACIÓN: Subjetivo y no cuantificable"
                ),
                "Posible mejora de rendimiento" to Pair(
                    false,
                    "ESPECULACIÓN: Sin métrica concreta definida"
                )
            )
        }
    }
}
