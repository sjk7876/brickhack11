document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent instant navigation

            const link = this.querySelector("a"); // Get the link inside the card
            if (!link) return;

            const targetURL = link.href; // Store the Django-generated URL

            const other_cards = [...cards].filter(c => c !== this);
            gsap.to(other_cards, {
                opacity: 0,
                duration: 0.5,
                ease: "power3.out",
            });

            gsap.to(this, {
                scale: 1.2,       // Zoom in
                opacity: 0,     // Fade out
                duration: 0.5,  // Smooth transition
                ease: "power3.inOut",
                onComplete: () => {
                    window.location.href = targetURL; // Redirect after animation completes
                }
            });
        });
    });

    gsap.from(cards, {
        opacity: 0,
        scale: 0.7,
        duration: 1,
        delay: 0.2,
        // stagger: 0.1,
        ease: "power2.out",
    });
});
