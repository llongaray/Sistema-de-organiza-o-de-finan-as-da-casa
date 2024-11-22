document.addEventListener('DOMContentLoaded', function() {
    // Toggle do menu lateral
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }

    // Fecha o menu em telas pequenas quando clicar em um link
    const menuLinks = document.querySelectorAll('.sidebar a');
    menuLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                sidebar.classList.add('active');
            }
        });
    });
});
