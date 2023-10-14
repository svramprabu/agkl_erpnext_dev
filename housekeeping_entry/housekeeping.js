// custom_app/custom_page/custom_page.js

const videoElement = document.getElementById('videoElement');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        videoElement.srcObject = stream;
    })
    .catch(error => {
        console.error('Error accessing camera: ', error);
    });

function scanQRCode() {
    // Implement your QR code scanning logic here
}

document.getElementById('entryButton').addEventListener('click', scanQRCode);
document.getElementById('exitButton').addEventListener('click', scanQRCode);
