const left = document.querySelector('.left');
const right = document.querySelector('.right');
const slider = document.querySelector('.slider');
const dotsContainer = document.getElementById("dots");

const images = slider.querySelectorAll('.image'); // Select all slides
let slide = 1;
const length = images.length; // Get the number of slides

// Function to update the active dot
const updateDots = () => {
    const dots = document.querySelectorAll(".dot");
    dots.forEach(dot => dot.classList.remove("active"));
    dots[slide - 1].classList.add("active"); // Match index with the current slide
};

// Function to create dots dynamically
const createdot = () => {
    for (let i = 0; i < length; i++) {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        if (i === 0) dot.classList.add("active");
        dot.setAttribute("data-slide", i + 1); // Use 1-based indexing
        dotsContainer.appendChild(dot);
    }
};

// Function to move to the next slide
const nextSlide = () => {
    if (slide < length) {
        slider.style.transform = `translateX(-${slide * 100}%)`;
        slide++;
    } else {
        getFirstSlide(); // Reset to the first slide if it's the last one
    }
    updateDots();
};

// Function to reset to the first slide
const getFirstSlide = () => {
    slider.style.transform = 'translateX(0)';
    slide = 1;
    updateDots();
};

// Function to move to the previous slide
const preSlide = () => {
    if (slide > 1) {
        slider.style.transform = `translateX(-${(slide - 2) * 100}%)`;
        slide--;
    } else {
        getLastSlide(); // Reset to the last slide if it's the first one
    }
    updateDots();
};

// Function to reset to the last slide
const getLastSlide = () => {
    slider.style.transform = `translateX(-${(length - 1) * 100}%)`;
    slide = length;
    updateDots();
};

// Event listener for right arrow
right.addEventListener('click', nextSlide);

// Event listener for left arrow
left.addEventListener('click', preSlide);

// Auto slide functionality
let interval;
const startAutoSlide = () => {
    interval = setInterval(nextSlide, 3000);
};

const stopAutoSlide = () => {
    clearInterval(interval);
};

// Pause auto-slide on hover and resume when hover is removed
slider.addEventListener("mouseenter", stopAutoSlide);
slider.addEventListener("mouseleave", startAutoSlide);

// Event listener for dots
dotsContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("dot")) {
        const targetSlide = parseInt(e.target.getAttribute("data-slide"));
        if (targetSlide !== slide) {
            slider.style.transform = `translateX(-${(targetSlide - 1) * 100}%)`;
            slide = targetSlide;
            updateDots();
        }
    }
});

// Initialize the slider
createdot();
startAutoSlide();

// button
const productContainers = document.querySelectorAll('.product-container');
console.log(productContainers);
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];
console.log(nxtBtn);

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;
    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += 1.5 * containerWidth;
    })
    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= 1.5 * containerWidth;
    })
})

// fav
const favBtns = document.querySelectorAll('.fav-btn');

favBtns.forEach(button => {
    button.addEventListener('click', () => {
        const img = button.querySelector('.fav'); // Find the image element within the button
        const activeSrc = img.dataset.activeSrc; // Get the active image URL
        const inactiveSrc = img.dataset.inactiveSrc; // Get the inactive image URL

        console.log('Current src:', img.src); // Debugging: Log the current image source
        console.log('Active src:', activeSrc); // Debugging: Log the active source URL
        console.log('Inactive src:', inactiveSrc); // Debugging: Log the inactive source URL

        if (img.src.includes(inactiveSrc)) {
            img.src = activeSrc;
            console.log('Image switched to active');
        } else {
            img.src = inactiveSrc;
            console.log('Image switched to inactive');
        }
    });
});

// const favBtns = document.querySelectorAll('.fav-btn'); 
// favBtns.forEach(button => {
//      button.addEventListener('click', () => {
//         const img = button.querySelector('.fav'); 
//         const activeSrc = "/static/img/favorite_24dp_8B1A10_FILL0_wght700_GRAD200_opsz20.png"; 
//         const inactiveSrc = "/static/img/favorite_24dp_000000_FILL0_wght400_GRAD0_opsz24.png"; 
//         if (img.src.includes("/static/img/favorite_24dp_000000_FILL0_wght400_GRAD0_opsz24.png")) { 
//             img.src = activeSrc; 
//         } else { 
//             img.src = inactiveSrc; 
//         } 
//     });
// });
