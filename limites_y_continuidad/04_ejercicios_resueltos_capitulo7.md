# 📐 Guía Completa de Ejercicios Resueltos - Capítulo 7: Límites y Continuidad

Esta guía contiene la resolución matemática detallada, paso a paso, de los ejercicios del libro **Matemáticas I (1º Bachillerato)**.

---

## 📌 1. Cálculo de Límites Indeterminados (Pág. 32-33)

### Ejercicio 1a:
$$\lim_{x \to -3} \frac{x+3}{x^2-9}$$
- **Sustitución:** $\frac{-3+3}{9-9} = \frac{0}{0}$ (Indeterminación)
- **Factorización:** $x^2 - 9 = (x+3)(x-3)$
- **Simplificación:**
  $$\lim_{x \to -3} \frac{x+3}{(x+3)(x-3)} = \lim_{x \to -3} \frac{1}{x-3} = \frac{1}{-3-3} = -\frac{1}{6}$$

### Ejercicio 1c:
$$\lim_{x \to -3} \frac{x^3+27}{x^2+3x}$$
- **Sustitución:** $\frac{-27+27}{9-9} = \frac{0}{0}$ (Indeterminación)
- **Factorización:** Suma de cubos $x^3+27 = (x+3)(x^2-3x+9)$ y factor común $x^2+3x = x(x+3)$
- **Simplificación:**
  $$\lim_{x \to -3} \frac{(x+3)(x^2-3x+9)}{x(x+3)} = \lim_{x \to -3} \frac{x^2-3x+9}{x} = \frac{(-3)^2 - 3(-3) + 9}{-3} = \frac{27}{-3} = -9$$

### Ejercicio 2d:
$$\lim_{x \to \infty} \left( \frac{3x}{x^2-4} - \frac{2}{x+2} \right)$$
- **Sustitución:** $\infty - \infty$ (Indeterminación)
- **Común denominador:** $x^2-4 = (x-2)(x+2)$
  $$\frac{3x - 2(x-2)}{x^2-4} = \frac{3x - 2x + 4}{x^2-4} = \frac{x+4}{x^2-4}$$
- **Límite:** Como el grado del denominador ($2$) es mayor que el del numerador ($1$):
  $$\lim_{x \to \infty} \frac{x+4}{x^2-4} = 0$$

---

## 📌 2. Continuidad y Cálculo de Parámetros (Pág. 34)

### Ejercicio 11:
Dada la función definida a trozos:
$$f(x) = \begin{cases} 3 - x^2 & \text{si } x < 2 \\ k + x & \text{si } x \ge 2 \end{cases}$$
Determina el valor de $k$ para que $f(x)$ sea continua en toda la recta real.

- **Análisis:** Las ramas $3-x^2$ y $k+x$ son polinómicas, por lo que son continuas en sus dominios. El único punto crítico es $x = 2$.
- **Límites laterales en $x = 2$:**
  1. Por la izquierda ($x < 2$):
     $$\lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} (3 - x^2) = 3 - 2^2 = 3 - 4 = -1$$
  2. Por la derecha ($x \ge 2$):
     $$\lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} (k + x) = k + 2$$
  3. Valor de la función: $f(2) = k + 2$.
- **Condición de continuidad:** Los límites laterales deben ser iguales:
  $$-1 = k + 2 \implies k = -1 - 2 \implies k = -3$$
- **Resultado:** Para $k = -3$, la función es continua en todo $\mathbb{R}$.

---

## 📌 3. Examen de Autoevaluación Resuelto (Pág. 35)

### Pregunta 7:
Calcular el límite:
$$\lim_{x \to \infty} \left( \frac{3x+1}{3x-2} \right)^{2x^2+1}$$

1. **Base:** $\lim_{x \to \infty} \frac{3x+1}{3x-2} = 1$
2. **Exponente:** $\lim_{x \to \infty} (2x^2+1) = \infty$
3. **Tipo:** Indeterminación $1^\infty$ (Límite tipo $e$).
4. **Fórmula:** $e^L$ donde $L = \lim_{x \to \infty} g(x) \cdot (f(x) - 1)$:
   $$f(x) - 1 = \frac{3x+1}{3x-2} - 1 = \frac{3x+1 - (3x-2)}{3x-2} = \frac{3}{3x-2}$$
   $$L = \lim_{x \to \infty} (2x^2+1) \cdot \frac{3}{3x-2} = \lim_{x \to \infty} \frac{6x^2+3}{3x-2}$$
   Como el grado del numerador ($2$) es mayor que el del denominador ($1$), $L = +\infty$.
5. **Resultado final:** $e^{+\infty} = \infty$.
- **Respuesta Autoevaluación:** **a) $\infty$**
