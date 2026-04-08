# Proyecto 1: NutriUTP

Desacoplamiento de software: Principios para gestionar y aislar dependencias

Programación 4

Nombre Alumno
Nombre Alumno

Docente: Alejandro Rodas Vásquez
Universidad Tecnológica de Pereira
13 de marzo de 2026

---

# Descripción del Proyecto

El sistema NutriUTP es una aplicación diseñada para gestionar la entrega de almuerzos en la cafetería estudiantil de la universidad.

Permite administrar menús diarios, procesar subsidios estudiantiles y generar reportes, aplicando principios de desacoplamiento de software para facilitar su mantenimiento y evolución.

---

# Objetivo

Diseñar un sistema flexible donde los cambios en las reglas de negocio como subsidios o menú no afecten el resto del sistema, mediante bajo acoplamiento, alta cohesión, encapsulamiento e inyección de dependencias.

---

# Estructura del Proyecto

```
NutriUTP/
│
├── main.py
├── README.md
│
├── modelos/
│   ├── plato.py
│   ├── menu_dia.py
│   └── comensal.py
│
├── servicios/
│   ├── procesador_venta.py
│   └── servicio_pago.py
│
├── reportes/
│   └── generador_reportes.py
```

---

# Funcionalidades

Gestión del menú
Creación dinámica de platos
Opción estándar y vegetariana
Consulta del menú del día

Procesamiento de subsidios
Cálculo del precio según tipo de usuario
Aplicación de descuentos alto, medio y bajo
Aislamiento de lógica matemática

Gestión de ventas
Generación de tiquetes
Validación de pago
Uso de inyección de dependencias

Reportes
Total recaudado
Cantidad de ventas

---

# Principios de Diseño Aplicados

Principio de Responsabilidad Única
Plato gestiona la información del plato
MenuDia gestiona el menú
Comensal calcula descuentos
ProcesadorVenta gestiona la venta
GeneradorReportes genera reportes

Bajo Acoplamiento
Las clases interactúan mediante métodos y no dependencias rígidas. ProcesadorVenta no crea objetos, los recibe como parámetros.

Inyección de Dependencias
El servicio de pago se inyecta en el procesador, lo que permite cambiarlo sin afectar el resto del sistema.

Encapsulamiento
Los atributos se mantienen protegidos y el acceso se realiza mediante métodos.

---

# Ejecución del Proyecto

Requisitos
Python 3.x

Ejecución

```
python main.py
```

---

# Uso del Sistema

El sistema inicia sin datos predefinidos.

Opciones disponibles
Agregar plato
Ver menú
Comprar plato
Ver reporte
Salir

---

# Escalabilidad

El sistema permite integrar base de datos, API, interfaz gráfica, nuevos tipos de subsidio e integración con sistemas de pago.

---

# Conclusión

El proyecto demuestra cómo aplicar principios de diseño de software para construir sistemas flexibles, mantenibles y escalables, evitando dependencias innecesarias.
