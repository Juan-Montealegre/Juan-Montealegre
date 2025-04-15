# Facial Recognition Attendance System

Este proyecto es un sistema de captura de asistencia utilizando reconocimiento facial. Utiliza la cámara del dispositivo para identificar a los usuarios y registrar su asistencia de manera automática.

## Estructura del Proyecto

```
facial-recognition-attendance
├── src
│   ├── app.py                # Punto de entrada de la aplicación
│   ├── camera.py             # Clase para manejar la cámara
│   ├── face_recognition.py   # Funciones para reconocimiento facial
│   ├── database.py           # Manejo de la base de datos
│   └── utils
│       └── helpers.py        # Funciones auxiliares
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación del proyecto
└── .gitignore                # Archivos a ignorar por Git
```

## Requisitos Previos

- Python 3.8 o superior.
- Una cámara funcional conectada al dispositivo.
- Sistema operativo Windows, macOS o Linux.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd facial-recognition-attendance
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Asegúrate de que tu cámara esté conectada y funcionando.
2. Ejecuta la aplicación:
   ```bash
   python src/app.py
   ```

3. Abre tu navegador y accede a `http://localhost:5000`.
4. Sigue las instrucciones en pantalla para:
   - Iniciar sesión o registrarte.
   - Registrar tu asistencia.
   - Administrar usuarios (si eres administrador).

## Capturas de Pantalla

### Pantalla de Inicio de Sesión
![Inicio de Sesión](https://via.placeholder.com/600x400?text=Captura+de+Inicio+de+Sesión)

### Registro de Asistencia
![Registro de Asistencia](https://via.placeholder.com/600x400?text=Captura+de+Registro+de+Asistencia)

## Configuración

- Asegúrate de tener instaladas las bibliotecas necesarias listadas en `requirements.txt`.
- Configura la base de datos en `src/database.py` según tus necesidades.

## Problemas Comunes

1. **Error al acceder a la cámara**:
   - Verifica que tu navegador tenga permisos para usar la cámara.
   - Asegúrate de que ningún otro programa esté utilizando la cámara.

2. **Problemas con dependencias**:
   - Asegúrate de instalar las dependencias con `pip install -r requirements.txt`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Contacto

- Autor: Juan Montealegre
- Correo: juan.montealegre@example.com
- LinkedIn: [Perfil de LinkedIn](https://www.linkedin.com/in/juan-montealegre)

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.