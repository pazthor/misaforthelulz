package com.powersystems.examples

/**
 * Ejemplo 2: Jerarquía Organizacional como Sistema de Poder
 *
 * Una organización es un sistema de poder donde:
 * - Los roles tienen privilegios específicos
 * - Estos privilegios LIMITAN el alcance de acción
 * - Podemos ESTIMAR (aunque con menos precisión) el impacto
 */
class OrganizationalPowerExample(
    private val role: OrganizationalRole
) : PowerSystem {

    override val name = "Sistema Organizacional - Rol: ${role.title}"

    override val privileges: Set<Privilege>
        get() = role.privileges

    override fun canPerform(action: String): Boolean {
        return privileges.any { it.actions.contains(action) }
    }

    override fun getLimitations(): List<String> {
        return privileges.flatMap { it.limitations }
    }

    override fun estimateMinimumReach(): ReachEstimation {
        // En organizaciones, el alcance es MENOS preciso pero AÚN medible
        // Podemos contar: personas bajo tu mando, presupuesto, decisiones

        val directReports = role.directReports
        val budgetControl = role.budgetAccess
        val decisionScope = privileges.count { it.scope != PrivilegeScope.NONE }

        val minimumImpact = directReports + (if (budgetControl > 0) 1 else 0)
        val maximumImpact = directReports * 10 + (budgetControl / 1000)

        // La confianza es menor que file system pero AÚN es medible
        val confidence = when {
            role.level == RoleLevel.EXECUTIVE -> 0.7  // Más difícil de medir
            role.level == RoleLevel.MANAGER -> 0.8    // Medible con cierta precisión
            else -> 0.9                               // Muy medible
        }

        return ReachEstimation(
            isMeasurable = true,
            minimumImpact = minimumImpact,
            maximumImpact = maximumImpact,
            confidence = confidence,
            reasoning = """
                Rol organizacional '${role.title}' tiene alcance ESTIMABLE:
                - Reportes directos: $directReports personas (MEDIBLE)
                - Control de presupuesto: $$budgetControl (CONCRETO)
                - Alcance de decisiones: $decisionScope áreas (DEFINIDO)

                Aunque menos preciso que un sistema de archivos,
                PODEMOS hacer estimaciones mínimas concretas.
                NO es pura especulación.
            """.trimIndent()
        )
    }

    /**
     * Demuestra límites organizacionales medibles
     */
    fun demonstrateOrganizationalLimits(): List<String> {
        return listOf(
            "Empleado Junior: Puede acceder a ${role.systemsAccess.size} sistemas → LÍMITE MEDIBLE",
            "No puede aprobar presupuestos > $${role.approvalLimit} → LÍMITE CONCRETO",
            "Requiere ${role.approvalsNeeded} aprobaciones para decisiones → RESTRICCIÓN CLARA",
            "Alcance limitado a ${role.departments.joinToString()} → FRONTERA DEFINIDA"
        )
    }
}

/**
 * Rol organizacional con privilegios específicos
 */
data class OrganizationalRole(
    val title: String,
    val level: RoleLevel,
    val directReports: Int,
    val budgetAccess: Int,
    val approvalLimit: Int,
    val approvalsNeeded: Int,
    val departments: List<String>,
    val systemsAccess: List<String>,
    val privileges: Set<Privilege>
)

enum class RoleLevel {
    INDIVIDUAL_CONTRIBUTOR,
    TEAM_LEAD,
    MANAGER,
    DIRECTOR,
    EXECUTIVE
}

/**
 * Factory para crear ejemplos de roles
 */
object OrganizationalRoles {
    fun createJuniorDeveloper() = OrganizationalRole(
        title = "Desarrollador Junior",
        level = RoleLevel.INDIVIDUAL_CONTRIBUTOR,
        directReports = 0,
        budgetAccess = 0,
        approvalLimit = 0,
        approvalsNeeded = 2,
        departments = listOf("Ingeniería"),
        systemsAccess = listOf("Git", "Jira", "Slack"),
        privileges = setOf(
            Privilege(
                name = "CODE_ACCESS",
                scope = PrivilegeScope.LIMITED,
                actions = setOf("read_code", "write_code", "create_pr"),
                limitations = listOf(
                    "No puede aprobar PRs",
                    "No puede mergear a main",
                    "Requiere code review"
                )
            ),
            Privilege(
                name = "TASK_MANAGEMENT",
                scope = PrivilegeScope.RESTRICTED,
                actions = setOf("create_task", "update_own_tasks"),
                limitations = listOf(
                    "No puede asignar tareas a otros",
                    "No puede cambiar prioridades",
                    "Solo sus propias tareas"
                )
            )
        )
    )

    fun createEngineeringManager() = OrganizationalRole(
        title = "Manager de Ingeniería",
        level = RoleLevel.MANAGER,
        directReports = 8,
        budgetAccess = 500000,
        approvalLimit = 50000,
        approvalsNeeded = 1,
        departments = listOf("Ingeniería", "Producto"),
        systemsAccess = listOf("Git", "Jira", "Slack", "AWS Console", "Analytics"),
        privileges = setOf(
            Privilege(
                name = "TEAM_MANAGEMENT",
                scope = PrivilegeScope.LIMITED,
                actions = setOf("hire", "fire", "promote", "assign_work"),
                limitations = listOf(
                    "Limitado a su equipo de ${8} personas",
                    "Requiere aprobación de HR para contratar",
                    "Budget limitado a $500k"
                )
            ),
            Privilege(
                name = "CODE_APPROVAL",
                scope = PrivilegeScope.LIMITED,
                actions = setOf("approve_pr", "merge_code", "deploy"),
                limitations = listOf(
                    "Solo en sus repositorios",
                    "Producción requiere segundo aprobador"
                )
            ),
            Privilege(
                name = "BUDGET_CONTROL",
                scope = PrivilegeScope.RESTRICTED,
                actions = setOf("approve_expenses", "allocate_resources"),
                limitations = listOf(
                    "Máximo $50k por aprobación individual",
                    "Budget anual limitado",
                    "Requiere director para gastos mayores"
                )
            )
        )
    )
}
