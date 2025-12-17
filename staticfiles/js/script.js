// Falling hearts
const heartCount = 40;
const bg = document.querySelector('.hearts-background');

for (let i = 0; i < heartCount; i++) {
    const heart = document.createElement('div');
    heart.classList.add('heart');
    heart.style.left = Math.random() * 100 + 'vw';
    heart.style.animationDuration = (3 + Math.random() * 5) + 's';
    heart.style.animationDelay = Math.random() * 5 + 's';
    bg.appendChild(heart);
}

// Heart explosion on card click
function showHeartExplosion(e, cardId) {
    for (let i = 0; i < 20; i++) {
        const heart = document.createElement('div');
        heart.classList.add('heart-explosion');
        heart.style.left = e.clientX + 'px';
        heart.style.top = e.clientY + 'px';
        heart.style.setProperty('--x', (Math.random() - 0.5) * 200 + 'px');
        heart.style.setProperty('--y', (Math.random() - 0.5) * 200 + 'px');
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 1000);
    }
    // redirect after short delay
    setTimeout(() => {
        window.location.href = `/letter/${cardId}/`;
    }, 500);
}
