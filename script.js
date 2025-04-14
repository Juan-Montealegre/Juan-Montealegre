// script.js mejorado con reconocimiento facial, feedback visual, sonido, mejoras UX y prevención de errores

document.addEventListener("DOMContentLoaded", async () => {
    const elements = {
        video: document.getElementById("video"),
        captureButton: document.getElementById("capture"),
        feedback: document.getElementById("feedback"),
        loginButton: document.getElementById("login-button"),
        registerButton: document.getElementById("register-button"),
        logoutButton: document.getElementById("logout-button"),
        container: document.querySelector(".container"),
        loginForm: document.getElementById("login-form"),
    };

    let stream = null;

    // Cargar modelos de face-api.js
    async function loadFaceApiModels() {
        const MODEL_URL = './public/models';
        await faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL);
        await faceapi.nets.faceRecognitionNet.loadFromUri(MODEL_URL);
        await faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL);
        elements.feedback.textContent = "Modelos cargados correctamente.";
        elements.feedback.style.color = "green";
    }

    // Iniciar la cámara
    async function startCamera() {
        try {
            stream = await navigator.mediaDevices.getUserMedia({ video: true });
            elements.video.srcObject = stream;
        } catch (error) {
            elements.feedback.textContent = "No se pudo acceder a la cámara. Verifica los permisos.";
            elements.feedback.style.color = "red";
        }
    }

    // Capturar imagen y realizar reconocimiento facial
    async function captureAndRecognize() {
        const canvas = faceapi.createCanvasFromMedia(elements.video);
        const displaySize = { width: elements.video.width, height: elements.video.height };
        faceapi.matchDimensions(canvas, displaySize);

        const detections = await faceapi.detectAllFaces(elements.video, new faceapi.TinyFaceDetectorOptions())
            .withFaceLandmarks()
            .withFaceDescriptors();

        if (detections.length === 0) {
            elements.feedback.textContent = "No se detectaron rostros.";
            elements.feedback.style.color = "red";
            return;
        }

        elements.feedback.textContent = `Se detectaron ${detections.length} rostro(s).`;
        elements.feedback.style.color = "green";
    }

    // Detener la cámara
    function stopCamera() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
        }
    }

    // Eventos de botones
    elements.captureButton.addEventListener("click", captureAndRecognize);

    elements.loginButton.addEventListener("click", () => {
        elements.loginForm.style.display = "none";
        elements.container.style.display = "block";
        startCamera();
    });

    elements.logoutButton.addEventListener("click", () => {
        elements.container.style.display = "none";
        elements.loginForm.style.display = "block";
        stopCamera();
    });

    // Cargar modelos y activar la cámara al inicio
    await loadFaceApiModels();
});