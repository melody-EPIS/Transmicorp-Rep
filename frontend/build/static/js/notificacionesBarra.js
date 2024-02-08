let notifVisibles = false;




document.getElementById('notificacion').addEventListener('click', function () {
    console.log("Clic en el botón de notificaciones");
    if (notifVisibles) {
        ocultarNotificaciones();
    } else {
        obtenerEstadoInventario();
        verificarFacturasPendientes();
    }
});

// Evento para ocultar notificaciones cuando se hace clic fuera de ellas
document.addEventListener('click', function (event) {
    const dropdownMenu = document.getElementById('nuevas-notificaciones-m');
    if (!dropdownMenu.contains(event.target)) {
        ocultarNotificaciones();
    }
});

function obtenerEstadoInventario() {
    fetch('http://127.0.0.1:8000/inventario/obtener_estado_inventario')
        .then(response => response.json())
        .then(data => {
            const elementosBajosStock = data.items_bajos_stock;

            if (elementosBajosStock.length > 0) {
                const nombresElementos = elementosBajosStock.map(item => item.NombreItem).join(', ');
                const mensajeCantidadBaja = `¡Alerta! Los elementos ${nombresElementos} en el inventario tienen cantidad menor a 10.`;
                mostrarNotificacion(mensajeCantidadBaja, 'alerta');
            }
        })
        .catch(error => {
            console.error('Error al obtener estado del inventario:', error);
    });
}

function verificarFacturasPendientes() {
    fetch('http://127.0.0.1:8000/facturas/verificar_facturas_pendientes')
        .then(response => response.json())
        .then(data => {
            const facturasPendientes = data.facturas_pendientes;

            if (facturasPendientes.length > 0) {
                const mensajesFacturasPendientes = facturasPendientes.map(factura => {
                    return `Las facturas de las órdenes de trabajo ${factura.Orden_de_trabajo} están pendientes de pago.`;
                });
                mensajesFacturasPendientes.forEach(mensaje => {
                    mostrarNotificacion(mensaje, 'alerta');
                });
            }
        })
        .catch(error => {
            console.error('Error al verificar facturas pendientes:', error);
        }
    );
}

function mostrarNotificacion(mensaje, tipo) {
    const notificationElement = document.createElement('div');
    notificationElement.classList.add('notificacion-items', tipo);
    notificationElement.textContent = mensaje;

    const dropdownMenu = document.getElementById('nuevas-notificaciones-m');
    dropdownMenu.appendChild(notificationElement);

    dropdownMenu.classList.add('show');
    notifVisibles = true;

    setTimeout(() => {
        dropdownMenu.removeChild(notificationElement);
        if (dropdownMenu.childElementCount === 0) {
            ocultarNotificaciones();
        }
    }, 3000);
}

function ocultarNotificaciones() {
    const dropdownMenu = document.getElementById('nuevas-notificaciones-m');
    dropdownMenu.classList.remove('show');
    notifVisibles = false;
}
//setInterval(obtenerEstadoInventario, 30000);
//setInterval(verificarFacturasPendientes, 30000);