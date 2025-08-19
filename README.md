# 🌌 Rossler Oscillator

Este repositorio contiene varios scripts para estudiar el oscilador de Rossler, un sistema dinámico no lineal famoso por su comportamiento caótico y su rica dinámica. 🔄✨

Se incluyen simulaciones de osciladores individuales, pares acoplados, así como análisis de diagramas de bifurcación y mapas de retorno.

##🔹 Contenido del repositorio

single_oscillator.py
Simulación de un oscilador de Rossler individual. Permite observar cómo evolucionan sus variables en el tiempo y explorar el comportamiento caótico. 🌀

two_oscillators.py
Simulación de dos osciladores acoplados. Permite estudiar fenómenos como sincronización y desincronización entre osciladores. 🤝

two_oscillators_2.py
Simulación de dos osciladores independientes (no acoplados), útil para comparar la dinámica con el caso acoplado. 🔗❌

roessler_bifurcation.py
Genera un diagrama de bifurcación del oscilador de Rossler, mostrando cómo cambian los puntos fijos y la dinámica al variar un parámetro del sistema. 📊

return_map.py
Calcula un mapa de retorno del oscilador, una herramienta clave en el análisis de sistemas caóticos. 🔁

## ⚙️ Uso

Instala las librerías necesarias (si no las tienes):

pip install numpy matplotlib


Ejecuta el script deseado, por ejemplo:

python single_oscillator.py


Observa gráficos y resultados de la simulación. Cada script tiene comentarios internos que explican los parámetros principales y cómo modificarlos. 🖥️📈

## 🌟 Conceptos clave

Oscilador de Rossler
Un sistema de ecuaciones diferenciales no lineales que exhibe comportamiento caótico para ciertos parámetros.
Se define por tres variables 
𝑥
,
𝑦
,
𝑧
x,y,z y parámetros 
𝑎
,
𝑏
,
𝑐
a,b,c.

Sincronización de osciladores
Dos osciladores acoplados pueden sincronizar sus movimientos, mostrando fenómenos interesantes en sistemas físicos, biológicos y químicos. ⚡

Diagrama de bifurcación
Permite visualizar cómo el sistema cambia su comportamiento (puntos fijos, órbitas, caos) al variar parámetros. 🔍

Mapa de retorno
Representa los valores sucesivos de una variable del sistema, útil para analizar la estructura del caos y detectar atractores. 🔁

## 📚 Referencias

Basado en códigos iniciales de Héctor Corte-León (23/02/2013).

Conceptos de dinámica no lineal y caos: Strogatz, "Nonlinear Dynamics and Chaos".
