# Power Systems - Ejemplos de Privilegios y Límites Medibles

Este módulo demuestra el concepto de que **los sistemas de poder tienen privilegios que limitan, y esos límites son medibles**.

## Concepto Principal

**Los sistemas de poder no son más que sistemas que cumplen un fin: eso, ser un sistema.**

En todo sistema de poder:
1. **Existen privilegios** - Permisos, accesos, capacidades
2. **Los privilegios limitan** - Definen qué se puede y qué NO se puede hacer
3. **Los límites son medibles** - Podemos hacer estimaciones concretas del alcance mínimo
4. **No es especulación** - Son métricas verificables

## Estructura de Archivos

### Core (`PowerSystem.kt`)
- **PowerSystem**: Interface base para todos los sistemas de poder
- **Privilege**: Modelo de privilegio con scope, acciones y limitaciones
- **ReachEstimation**: Estimación del alcance con confianza medible

### Ejemplos

#### 1. FileSystemPowerExample.kt
**Sistema de Archivos Unix** - El ejemplo más claro de privilegios medibles

```kotlin
val fileSystem = FileSystemPowerExample()
// Privilegios: READ, WRITE, EXECUTE
// Limitaciones: Completamente medibles
// Confianza: 95%
```

**Demuestra:**
- Permisos READ/WRITE/EXECUTE son CONCRETOS
- Puedes contar EXACTAMENTE qué archivos puedes acceder
- Las limitaciones son CLARAS: "No puedes modificar sin WRITE"

#### 2. OrganizationalPowerExample.kt
**Jerarquía Organizacional** - Privilegios en organizaciones

```kotlin
val junior = OrganizationalPowerExample(OrganizationalRoles.createJuniorDeveloper())
val manager = OrganizationalPowerExample(OrganizationalRoles.createEngineeringManager())
// Junior: Limitado a sus tareas, no puede aprobar PRs
// Manager: Puede liderar 8 personas, presupuesto de $500k
// Confianza: 70-90%
```

**Demuestra:**
- Roles tienen alcances MEDIBLES: número de reportes directos, presupuesto
- Aunque menos preciso que file system, AÚN es estimable
- No es pura especulación, hay números concretos

#### 3. APIPermissionSystemExample.kt
**Sistema de API** - El más medible de todos

```kotlin
val api = APIPermissionSystemExample(
    apiKey = "key123",
    scopes = setOf(APIScopes.createFreePublicScope()),
    rateLimitPerHour = 100
)
// Rate limit: EXACTO (100 req/h)
// Endpoints: LISTA CONCRETA
// Confianza: 98% ¡CASI CERTEZA TOTAL!
```

**Demuestra:**
- Rate limits son PERFECTAMENTE medibles
- Sabes EXACTAMENTE cuántas llamadas puedes hacer
- Los scopes definen PRECISAMENTE qué endpoints puedes acceder
- Ejemplo MÁS CLARO de límites medibles vs especulación

### Utilidades

#### PowerSystemAnalyzer.kt
Herramienta para analizar sistemas de poder

```kotlin
val analyzer = PowerSystemAnalyzer()
val analysis = analyzer.analyze(fileSystem)
// Retorna: medible, confianza, alcance mínimo/máximo, veredicto
```

**Funciones:**
- `analyze()`: Analiza un sistema y determina si es medible
- `compare()`: Compara dos sistemas
- `demonstrateConcept()`: Muestra privilegios → límites → medición

#### PowerSystemDemo.kt
Demo completo con todos los ejemplos

```kotlin
fun main() {
    println(PowerSystemDemo.runFullDemo())
}
```

**Salida:**
- Todos los ejemplos ejecutados
- Comparación medible vs especulación
- Resumen de todos los sistemas
- Conclusión final

## Uso

### Ejecutar el Demo Completo

```kotlin
val output = PowerSystemDemo.runFullDemo()
println(output)
```

### Analizar un Sistema Individual

```kotlin
val fileSystem = FileSystemPowerExample()
val analysis = PowerSystemDemo.analyzeSingle(fileSystem)
println(analysis)
```

### Comparar Dos Sistemas

```kotlin
val system1 = FileSystemPowerExample()
val system2 = APIPermissionSystemExample(/*...*/)
val comparison = PowerSystemDemo.quickCompare(system1, system2)
println(comparison)
```

### Ver Todos los Análisis

```kotlin
val allAnalyses = AnalyzerExamples.runAllExamples()
allAnalyses.forEach { (name, analysis) ->
    println("$name: Confianza ${(analysis.confidence * 100).toInt()}%")
}
```

## Conceptos Demostrados

### 1. Privilegios → Límites

Cada sistema tiene privilegios que definen límites claros:

```kotlin
Privilege(
    name = "READ",
    actions = setOf("open", "read", "list"),
    limitations = listOf("No puede modificar contenido")
)
```

### 2. Límites → Medición

Los límites permiten hacer estimaciones concretas:

```kotlin
ReachEstimation(
    isMeasurable = true,
    minimumImpact = 100,        // Concreto
    maximumImpact = 10000,      // Estimado
    confidence = 0.95           // Alta confianza
)
```

### 3. Medible vs Especulación

```kotlin
val comparison = MeasurableVsSpeculation.compareScenarios()
// MEDIBLE: "Rate limit de 100 req/h" ✓
// ESPECULACIÓN: "Influencia en la organización" ✗
```

## Niveles de Confianza

| Sistema | Confianza | Razón |
|---------|-----------|-------|
| API | 98% | Métricas exactas, rate limits concretos |
| File System | 95% | Permisos definidos, archivos contables |
| Organización (Individual) | 90% | Métricas de tareas y accesos medibles |
| Organización (Manager) | 70-80% | Reportes directos y presupuesto medibles |

## Conclusión

Este código **DEMUESTRA** que:

1. ✓ Los sistemas de poder tienen privilegios
2. ✓ Los privilegios limitan el alcance
3. ✓ Esos límites SON medibles (no especulación)
4. ✓ Podemos estimar el alcance mínimo con confianza

**No es un divague. Es medible. Es concreto. Es verificable.**

## Extensión

Para agregar tu propio sistema de poder:

1. Implementa la interface `PowerSystem`
2. Define tus privilegios con `Privilege`
3. Implementa `estimateMinimumReach()` con métricas concretas
4. Usa `PowerSystemAnalyzer` para verificar que es medible

```kotlin
class MyCustomSystem : PowerSystem {
    override val name = "Mi Sistema"
    override val privileges = setOf(/* tus privilegios */)

    override fun estimateMinimumReach(): ReachEstimation {
        // Retorna estimación MEDIBLE con alta confianza
        // NO especulación sin fundamento
    }
}
```
