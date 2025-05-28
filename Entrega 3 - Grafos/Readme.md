# Proyecto de Clase

## Resumen de los Problemas Tratados
El supermercado La Última Lágrima, ubicado en Bucaramanga, enfrenta desafíos logísticos relacionados con la eficiencia en sus operaciones de entrega y distribución interna. Por lo que requiere programas que permitan: 
1.	Optimizar las rutas de entrega a domicilio de los productos solicitados por los clientes, reduciendo el tiempo de entrega y mejorando el servicio.
2.	Adaptar las rutas a las capacidades de carga de los repartidores, teniendo en cuenta que utilizan distintos medios de transporte (a pie, bicicleta o moto), cada uno con límites distintos de peso.
3.	Planificar de manera eficiente el reabastecimiento de sus sucursales, partiendo desde una bodega central, para asegurar la disponibilidad de productos en todos sus puntos de venta.
4.	Actualizar dinámicamente la red de sucursales, permitiendo añadir nuevas ubicaciones conforme el supermercado crece, o eliminar aquellas que han sido clausuradas, sin comprometer la integridad del sistema de rutas.
Estas necesidades motivaron el desarrollo de un sistema dividido en tres etapas, cada una respondiendo a una problemática específica y construyendo progresivamente una solución más completa.

## Etapas de Desarrollo
1. Entregas básicas.
En la primera etapa del proyecto se diseñó un programa utilizando listas doblemente enlazadas, con el objetivo de encontrar la ruta más eficaz que puede tomar un mensajero del supermercado para entregar productos directamente a los hogares de los clientes. Este enfoque inicial se centró exclusivamente en optimizar la secuencia de entregas, considerando únicamente las distancias entre los puntos, sin tener en cuenta factores como la capacidad de carga del repartidor o el medio de transporte utilizado.

2. Entregas con restricción de carga según el vehículo.
En esta etapa se mejoró el sistema incorporando restricciones logísticas más realistas. En esta versión, se utilizó una estructura de árbol para organizar y asignar los pedidos según el tipo de vehículo disponible (a pie, bicicleta o moto), considerando la capacidad máxima de carga que cada repartidor puede transportar. Esta adaptación permitió distribuir las entregas de forma más eficiente, evitando sobrecargas y asegurando que cada repartidor esté en condiciones de completar sus rutas sin exceder sus límites, lo cual impacta directamente en la seguridad y en la calidad del servicio.

3. Reabastecimiento de sucursales y gestión dinámica.
En la tercera etapa, el enfoque del sistema se amplió para el proceso de reabastecimiento entre la bodega central y las distintas sucursales del supermercado. Para ello se implementó una estructura basada en grafos, lo que permitió representar y calcular las rutas más cortas entre nodos (bodega y sucursales). Además, se incorporaron funciones que permiten eliminar sucursales clausuradas y añadir nuevas ubicaciones al sistema, haciendo del programa una herramienta más flexible para la administración logística del supermercado.

## Contextualización del Problema - Tercera Entrega
El proyecto tiene como objetivo diseñar e implementar un sistema que permita encontrar la ruta más corta para realizar una entrega. El supermercado "La Última Lágrima" cuenta con una bodega, la cual reparte suministros para reabastecer las diferentes sucursales de este supermercado.
Este programa ayudará a los domiciliarios a conocer la ruta más corta para completar los pedidos que deben ser entregados a las sucursales que lo requieran. También permitirá eliminar las sucursales clausuradas y añadir las nuevas sucursales.

## Librerias usadas:
Las librerías de python que fueron usadas son:

- math: Es un módulo estándar que proporciona funciones matemáticas para trabajar con números reales. Se utiliza cuando necesitas hacer cálculos matemáticos más avanzados que los que puedes hacer con operadores básicos
- deque: Es una estructura de datos optimizada para insertar y eliminar elementos rápidamente desde ambos extremos, a diferencia de una lista y se encuentra dentro del módulo collections.
- networkx: es una librería que permite modelar grafos (redes de nodos y aristas) y aplicar sobre ellos algoritmos como búsqueda de rutas más cortas, recorrido de grafos y análisis de conectividad. Es útil para representar sistemas como mapas, redes de transporte o estructuras de datos complejas.
- matplotlib.pyplot: es una librería de visualización gráfica que proporciona funciones para crear gráficos de líneas, barras, dispersión, histogramas, etc. Es ampliamente usada para visualizar datos y también para representar gráficamente grafos.
- heapq: Se usó heapq en Dijkstra para encontrar el nodo más cercano en O(log V), lo que hizo el algoritmo más eficiente (O((V + E) log V)). Si se hubiera usado una lista normal, esa búsqueda tomaría O(V), aumentando la complejidad total a O(V² + E).

## Integrantes del Grupo:
- 2240079 – Isabel Sofía García Joya 
- 2241441 – Ibeth Oriana Ruiz Manosalva
- 2240058 – Sara Sofía Solano Rocha
