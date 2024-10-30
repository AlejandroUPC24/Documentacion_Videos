// Link del video
// https://youtu.be/lytO0QJ5XSQ

// Link de formulario
// https://forms.office.com/r/CEiXmWnyE0


//Codigo para completar informacion del formulario y hacer scroll
function llenarFormulario() {
    // Selecciona los elementos de los campos
    let elementos = document.getElementsByClassName('-at-66');
    
    // Define los valores para cada campo
    let valores = ["%nombre%", "%apellido%", "%correo%", "%dni%", "%edad%"];
    
    // Itera sobre cada campo y valor
    valores.forEach((valor, index) => {
        // Hace scroll al campo para que esté visible
        elementos[index].scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Asigna el valor después de que el scroll se haya completado
        setTimeout(() => {
            elementos[index].value = valor;

            // Dispara un evento de cambio para que el formulario detecte la modificación
            let evento = new Event('input', { bubbles: true });
            elementos[index].dispatchEvent(evento);
        }, index * 1000); // Ajusta el retraso entre cada campo
    });
}

// Codigo para darle clic en el desplegable
function llenarFormulario() {
    document.getElementsByClassName("-a-201")[0].click()
    }

// Codigo para darle clic en M o F
function llenarFormulario() {
    document.getElementsByClassName("css-242")["%sexo%"].click()
    }
