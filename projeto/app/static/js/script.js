document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.deleteButton');
    const confirmationPopup = document.getElementById('confirmationPopup');
    const overlay = document.getElementById('overlay');
    const confirmYes = document.getElementById('confirmYes');
    const confirmNo = document.getElementById('confirmNo');
    let deleteUrl = ''; // URL de exclusão temporária

    // Abrir o pop-up de confirmação
    deleteButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            deleteUrl = button.getAttribute('data-url');
            confirmationPopup.classList.add('show');
            overlay.classList.add('show');
        });
    });

    // Confirmar exclusão
    confirmYes.addEventListener('click', () => {
        window.location.href = deleteUrl;
        confirmationPopup.classList.remove('show');
        overlay.classList.remove('show');
    });

    // Cancelar exclusão
    confirmNo.addEventListener('click', () => {
        confirmationPopup.classList.remove('show');
        overlay.classList.remove('show');
    });
});
