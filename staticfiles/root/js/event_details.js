
    document.addEventListener("DOMContentLoaded", function() {
        const slides = document.querySelectorAll(".slide");
        let current = 0;

        function showSlide(index) {
            slides.forEach((img, i) => {
                img.classList.toggle("active", i === index);
            });
        }

        document.querySelector(".next a").addEventListener("click", function(e) {
            e.preventDefault();
            current = (current + 1) % slides.length;
            showSlide(current);
        });

        document.querySelector(".prev a").addEventListener("click", function(e) {
            e.preventDefault();
            current = (current - 1 + slides.length) % slides.length;
            showSlide(current);
        });
    });

