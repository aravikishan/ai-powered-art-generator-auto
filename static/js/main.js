// Navigation Interactions
const navLinks = document.querySelectorAll('nav ul li a');
navLinks.forEach(link => {
    link.addEventListener('click', function() {
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});

// Smooth Scrolling
const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
smoothScrollLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        targetElement.scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form Validation
const generateForm = document.getElementById('generate-form');
generateForm.addEventListener('submit', function(event) {
    const promptInput = document.getElementById('prompt');
    if (!promptInput.value.trim()) {
        event.preventDefault();
        alert('Please enter a valid prompt.');
    }
});

// Dynamic Content Loading
async function loadGallery() {
    const response = await fetch('/api/gallery');
    const artPieces = await response.json();
    const galleryContainer = document.querySelector('.row');
    galleryContainer.innerHTML = '';
    artPieces.forEach(art => {
        const artCard = `
            <div class="col-md-4">
                <div class="card mb-4">
                    <img src="data:image/png;base64,${art.image_data}" class="card-img-top" alt="${art.title}">
                    <div class="card-body">
                        <h5 class="card-title">${art.title}</h5>
                        <p class="card-text">Created at: ${new Date(art.created_at).toLocaleDateString()}</p>
                    </div>
                </div>
            </div>
        `;
        galleryContainer.insertAdjacentHTML('beforeend', artCard);
    });
}

// Load gallery on page load if on gallery page
if (window.location.pathname === '/gallery') {
    loadGallery();
}