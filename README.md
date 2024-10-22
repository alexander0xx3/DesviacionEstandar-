
---

# Desviación Estándar

Este proyecto implementa una aplicación para calcular la **media (promedio)** y la **desviación estándar** de una lista de números enteros utilizando la metodología **Test Driven Development (TDD)**.

## Integrantes

|------------|--------------------|
|Alumono|NRC|
|*ROJAS LARA JACK ALEXANDER**| 15970|

## Requisitos

- Python 3.10 o superior
- `unittest` para realizar pruebas (viene integrado con Python)
- `coverage` para verificar la cobertura de código

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/desviacion-estandar.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd desviacion-estandar
   ```

3. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

4. Instala las dependencias necesarias:
   ```bash
   pip install coverage
   ```

## Uso

### Ejecutar la aplicación

Puedes ejecutar las funciones de cálculo de la media y desviación estándar desde el archivo `src/calculadora.py`. Por ejemplo:

```python
from src.calculadora import calcular_media, calcular_desviacion_estandar

lista = [1, 2, 3, 4, 5]
media = calcular_media(lista)
desviacion = calcular_desviacion_estandar(lista)

print(f"Media: {media}")
print(f"Desviación Estándar: {desviacion}")
```

### Ejecutar las pruebas

Para ejecutar las pruebas unitarias, usa el siguiente comando en la raíz del proyecto:

```bash
python -m unittest discover -s tests
```

### Verificar la cobertura de código

1. Ejecuta las pruebas con `coverage`:

   ```bash
   coverage run -m unittest discover -s tests
   ```

2. Ver el reporte de cobertura:

   ```bash
   coverage report
   ```

3. Para generar un reporte detallado en formato HTML:

   ```bash
   coverage html
   ```

4. Abre el archivo `htmlcov/index.html` en tu navegador para ver el reporte detallado.

## Estructura del proyecto

```
desviacion-estandar/
│
├── src/
│   └── calculadora.py   # Implementación del cálculo de media y desviación estándar
├── tests/
│   └── test_calculos.py  # Pruebas unitarias para las funciones
└── README.md            # Documentación del proyecto
```

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama (`git checkout -b mejora-propuesta`).
3. Haz los cambios necesarios y realiza los commits (`git commit -m "Descripción de cambios"`).
4. Sube los cambios a tu repositorio (`git push origin mejora-propuesta`).
5. Crea un **Pull Request** en este repositorio original.

## Licencia

Este proyecto está bajo la licencia MIT.

---
