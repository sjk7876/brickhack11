document.addEventListener("DOMContentLoaded", function () {
    const categoryCards = document.querySelectorAll("[id^='category-card-']");
    const cards = document.querySelectorAll("[id^='single-card-']");

    const allCards = [...categoryCards, ...cards];

    categoryCards.forEach(categoryCard => {
        categoryCard.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent instant navigation

            const link = this.querySelector("a"); // Get the link inside the card
            if (!link) return;

            const targetURL = link.href; // Store the Django-generated URL

            const otherCards = [...allCards].filter(c => c !== this);
            gsap.to(otherCards, {
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

    cards.forEach(card => {
        card.addEventListener("click", function (event) {
            const otherCards = [...allCards].filter(c => c !== this);
            gsap.to(otherCards, {
                opacity: 0.4,
                scale: 0.9,       // Zoom out
                duration: 0.5,
                ease: "power3.out",
            });

            gsap.to(this, {
                opacity: 1,
                scale: 1.1,       // Zoom in
                duration: 0.5,  // Smooth transition
                ease: "power3.inOut",
            });
            console.log(otherCards);
        });
    });

    gsap.from(allCards, {
        opacity: 0,
        scale: 0.7,
        duration: 1,
        delay: 0.2,
        ease: "power2.out",
    });
});
