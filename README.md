# Misaforthelulz - Aprendiendo Conceptos desde Sistemas de Poder

Este repositorio es un intento de aprender nuevos conceptos desde una perspectiva de sistemas de poder.

## Concepto Principal

**Los sistemas de poder no son más que sistemas que cumplen un fin: eso, ser un sistema.**

Por ello, este proyecto contiene varios ejemplos donde se ve claramente que en sistemas de poder existen **privilegios**. Estos privilegios **limitan**, y por lo tanto se puede hacer una **estimación del alcance mínimo** o determinar si solo es un divague.

## Estructura del Proyecto

### 1. Journaler App (Android)
Una aplicación de notas/diario que demuestra:
- Sistema de permisos y accesos
- Jerarquía de componentes
- Ciclo de vida como sistema de control

### 2. Power Systems Module (`com.powersystems.examples`)
Ejemplos concretos en Kotlin que demuestran el concepto principal:

#### Ejemplos incluidos:
1. **FileSystemPowerExample**: Sistema de archivos Unix (permisos read/write/execute)
   - Confianza: 95% - Privilegios perfectamente medibles
   - Demuestra límites concretos y verificables

2. **OrganizationalPowerExample**: Jerarquías organizacionales
   - Roles: Junior Developer, Engineering Manager
   - Confianza: 70-90% - Métricas como reportes directos, presupuesto
   - Demuestra que incluso en organizaciones hay límites medibles

3. **APIPermissionSystemExample**: Sistemas de API con rate limits
   - Confianza: 98% - Casi certeza total
   - El ejemplo MÁS CLARO de privilegios medibles
   - Rate limits, scopes, endpoints: todo perfectamente cuantificable

#### Herramientas:
- **PowerSystemAnalyzer**: Analiza sistemas y determina si son medibles o especulativos
- **PowerSystemDemo**: Demo ejecutable que muestra todos los ejemplos
- **MeasurableVsSpeculation**: Comparación clara entre conceptos medibles y especulativos

Ver [documentación completa del módulo](app/src/main/java/com/powersystems/examples/README.md)

## Objetivo

Entender que cualquier sistema de poder (tecnológico, social, organizacional) puede ser analizado mediante:
1. Identificación de privilegios
2. Medición de sus límites
3. Estimación de su alcance mínimo
4. Diferenciación entre conceptos medibles y mera especulación

## Uso

Este proyecto usa Gradle y Kotlin. Para compilar:

```bash
./gradlew build
```

### Ejecutar los ejemplos de Power Systems

Los ejemplos están en Kotlin y pueden ser ejecutados directamente:

```kotlin
// En PowerSystemDemo.kt
fun main() {
    println(PowerSystemDemo.runFullDemo())
}
```

Esto mostrará:
- Análisis de cada sistema de poder
- Medición de privilegios y límites
- Comparación entre medible vs especulación
- Conclusiones sobre el alcance mínimo estimable

### Ejemplos de uso individual

```kotlin
// Analizar un sistema de archivos
val fileSystem = FileSystemPowerExample()
val analysis = PowerSystemAnalyzer().analyze(fileSystem)
println("Confianza: ${(analysis.confidence * 100).toInt()}%")
println("¿Es medible? ${analysis.isMeasurable}")

// Comparar dos sistemas
val api = APIPermissionSystemExample(/*...*/)
val comparison = PowerSystemDemo.quickCompare(fileSystem, api)
println(comparison)
```

## Contribuciones

Este es un proyecto educativo para explorar conceptos de sistemas de poder desde una perspectiva práctica de programación.
