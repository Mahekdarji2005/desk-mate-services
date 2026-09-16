document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add sticky class to header on scroll
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
        } else {
            header.style.boxShadow = '0 2px 4px rgba(0,0,0,0.05)';
        }
    });

    // Add animation classes to elements when they come into view (simple Intersection Observer)
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    // Select elements to animate
    const animatedElements = document.querySelectorAll('.feature-card, .service-card, .industry-card, .step');
    animatedElements.forEach(el => {
        el.style.opacity = 0;
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.5s ease-out';
        observer.observe(el);
    });
});

// Modal Logic
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById("trialModal");
    const btn = document.getElementById("openTrialModalBtn");
    const span = document.querySelector(".close-modal");

    if (btn && modal && span) {
        btn.onclick = function(e) {
            e.preventDefault();
            modal.style.display = "block";
        }

        span.onclick = function() {
            modal.style.display = "none";
        }

        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    }
});

// WhatsApp Form Submission Logic
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('.schedule-form');
    
    forms.forEach(form => {
        const submitBtn = form.querySelector('.submit-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Get form fields (using specific child selectors or relative paths)
                const inputs = form.querySelectorAll('input, textarea');
                let name = "", email = "", phone = "", company = "", notes = "";
                
                inputs.forEach(input => {
                    const label = input.previousElementSibling ? input.previousElementSibling.innerText : "";
                    if (label.includes("Full Name")) name = input.value;
                    if (label.includes("Business Email")) email = input.value;
                    if (label.includes("Phone Number")) phone = input.value;
                    if (label.includes("Company Name")) company = input.value;
                    if (label.includes("Anything you'd like us to know")) notes = input.value;
                });
                
                // Basic validation
                if (!name || !email) {
                    alert("Please fill in your Full Name and Business Email.");
                    return;
                }
                
                // Construct message
                let message = `*New Inquiry Call*\n\n`;
                message += `*Name:* ${name}\n`;
                message += `*Email:* ${email}\n`;
                if (phone) message += `*Phone:* ${phone}\n`;
                if (company) message += `*Company:* ${company}\n`;
                if (notes) message += `*Notes:* ${notes}\n`;
                
                // WhatsApp URLs for both numbers
                const waUrl1 = `https://wa.me/919898143719?text=${encodeURIComponent(message)}`;
                const waUrl2 = `https://wa.me/919316049623?text=${encodeURIComponent(message)}`;
                
                // Open WhatsApp in new tabs
                window.open(waUrl1, '_blank');
                window.open(waUrl2, '_blank');
                
                // Optionally close modal if in one
                const modal = form.closest('.modal');
                if (modal) {
                    modal.style.display = 'none';
                }
            });
        }
    });
});
