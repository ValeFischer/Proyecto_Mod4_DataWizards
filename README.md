![CancelInsight: Análisis y Optimización de Cancelaciones de Reservas de Hoteles](https://github.com/ValeFischer/Proyecto_Mod4_DataWizards/blob/main/assets/header-cancelinsight.jpg)

# CancelInsight: Análisis y Optimización de Cancelaciones de Reservas de Hotel
*Equipo desarrollo: [Marta García](https://github.com/martam3t3oro), [Valentina Fischer](https://github.com/ValeFischer), [Franca Tortarolo](https://github.com/FrancaTortaroloo) y [Elena Águila](https://github.com/eaguilag)*

## Introducción

**CancelInsights** es un análisis de las reservas de un hotel, cuyo objetivo es identificar patrones que puedan ayudar a reducir las tasas de cancelación.

La gerencia del hotel nos contactó con el objetivo de incrementar la ocupación del hotel y optimizar la gestión de las reservas. Para ello, hemos elaborado un análisis del conjunto de datos proporcionado por el cliente que contiene información detallada sobre las reservas del hotel. Estos datos nos permiten identificar patrones que nos pueden ayudar a reducir la tasa de cancelación. Para ello hemos hecho tres casos de estudio centrándonos en el estado de la reserva (si se ha cancelado o no) en relación con:

1. Estacionalidad y patrones temporales

2. Factores operativos o detalles de la reserva

3. Características demográficas del huésped


## Objetivos de Negocio:

1. Reducción de la Tasa de Cancelación: Identificar las causas y patrones de las cancelaciones para implementar medidas que reduzcan la tasa de cancelación.

2. Optimización de la Capacidad Hotelera: Aumentar la ocupación mediante la reducción de las cancelaciones y la maximización del uso de las habitaciones disponibles.

3. Incremento de los Ingresos: Reducir la pérdida de ingresos por cancelaciones y aumentar la efectividad de las estrategias de pricing y promociones.

4. Mejora de la Satisfacción del Cliente: Asegurar que las reservas no canceladas se traduzcan en estancias satisfactorias y repetidas.


## Casos de Uso

### Caso de Estudio 1: Análisis de Estacionalidad y Patrones Temporales

- **Objetivo:** Analizar cómo varían las cancelaciones según factores temporales de la reserva.

- **Preguntas:**
    - ¿Existe alguna estacionalidad o patrón temporal en las cancelaciones?
    - ¿Las cancelaciones son más frecuentes en ciertos meses o estaciones?
    - ¿Hay una diferencia significativa en las tasas de cancelación entre reservas para el fin de semana y días laborables?

- **KPIs:**
    - Tasa de Cancelación Anual: Porcentaje de reservas canceladas por año.
    - Tasa de Cancelación por Temporada: Porcentaje de reservas canceladas por estación del año.
    - Tasa de Cancelación Mensual: Porcentaje de reservas canceladas cada mes.
    - Tasa de Cancelación por Tipo de Día: Porcentaje de cancelaciones por tipo de día (día entre semana o fin de semana).

### Caso de Estudio 2: Análisis de Detalles de Reserva

- **Objetivo:** Evaluar si hay factores en relación a la reserva que influyen en la probabilidad de cancelación.

- **Preguntas:**
    - ¿Qué detalles de la reserva están asociadas con una mayor probabilidad de cancelación?
    - ¿Qué impacto tiene el tiempo de anticipación de la reserva (lead time) en la probabilidad de cancelación?
	- ¿Hay una relación entre el tipo de habitación, el ADR (Average Daily Rate), y las cancelaciones?
	- ¿El historial de cancelaciones previas o cambios en la reserva incrementan la probabilidad de una nueva cancelación?

- **KPIs:**
    - Tasa de Cancelación por Cambios de Reservas: Porcentaje de cancelaciones en función del número de cambios de reserva realizados.
    - Tasa de Cancelación por Historial de Reservas: Porcentaje de cancelaciones en función del número de reservas anteriores no canceladas.
    - Tasa de Cancelación vs. ADR: Relación entre la tasa de cancelación y la tarifa promedio diaria (ADR) por tipo de cliente.
    - Tasa de Cancelación por Tipo de Habitación: Porcentaje de cancelaciones en función del tipo de habitación asignada al cliente.
    - Distribución del Lead Time: Días transcurridos desde las reservas canceladas vs. no canceladas.

### Caso de Estudio 3: Análisis de Comportamiento de Clientes y Repetición de Visitas

- **Objetivo:** Identificar perfiles de clientes que tienden a cancelar con mayor frecuencia.

- **Preguntas:**
    - ¿Qué características del cliente están asociadas con una mayor probabilidad de cancelación?
    - ¿Existen ciertos países o segmentos de clientes (tipos de clientes) con mayores tasas de cancelación?
	- ¿Los clientes con necesidades especiales tienden a cancelar más?
    - ¿Cómo influyen los datos demográficos como la presencia de niños o bebés en la probabilidad de cancelación?

- **KPIs:**
    - Tasa de Cancelación por Tipo de Cliente: Porcentaje de cancelaciones para diferentes tipos de clientes.
    - Tasa de Cancelación por País de Origen: Porcentaje de cancelaciones por país de origen del cliente.
    - Tasa de Cancelación por Necesidades Especiales: Porcentaje de cancelaciones por necesidades especiales.
    - Tasa de Cancelación por Presencia de Niños o Bebés: Porcentaje de cancelaciones en función de si hay presencia de niños o bebés.

## Estrategias de Optimización y Mejora de las Reservas

Al comprender más profundamente los factores que pueden causar cancelaciones, podemos diseñar estrategias que no solo las reduzcan, sino que también mejoren la ocupación y la satisfacción general los huéspedes.

1. Temporalidad:
    - Público objetivo: Gerencia del Hotel, responsable de la toma de decisiones estratégicas y operativas.
    - Medidas: Ajustar las políticas de reserva según la temporada para reducir las cancelaciones y optimizar la ocupación, minimizando así la pérdida de ingresos.

2. Detalles de Reserva:
    - Público objetivo: Departamento de Reservas, encargado de gestionar las reservas y las relaciones con los clientes.
    - Medidas: Revisar tarifas y condiciones de cambio o cancelación de la reserva para mejorar la relación con los clientes, así como mejorar la asignación de habitaciones.

3. Detalles de Cliente:
    - Público objetivo: Equipo de Marketing, responsable de atraer y retener clientes.
    - Medidas: Desarrollar estrategias de retención basadas en segmentos de clientes propensos a cancelar, como mejorar la dirección u orientación de las campañas.