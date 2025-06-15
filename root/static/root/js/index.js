

// -----------------HamburgerMenu-----------------
const menu = document.querySelector('.menu');
const openMenuButton = document.querySelector('.open-menu-btn');
const closeMenuButton = document.querySelector('.close-menu-btn');

[openMenuButton, closeMenuButton].forEach((button) => {
    button.addEventListener('click', () => {
        menu.classList.toggle('open');
        menu.style.transition = "transform 0.5s ease";
    });
});


menu.addEventListener("transitionend", function() {
    this.removeAttribute("style");
});


menu.querySelectorAll(".dropdown > i").forEach((arrow) => {
    arrow.addEventListener("click", function() {
        this.closest(".dropdown").classList.toggle("active");
    });
});







// -----------------Sticky Header-----------------
window.addEventListener("scroll", function() {
  var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);  
});











// ------------------Home Carousel-----------------

let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');

let carouselDom = document.querySelector('.carousel');
let SliderDom = carouselDom.querySelector('.carousel .list');
let thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
let thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');
let timeDom = document.querySelector('.carousel .time');

thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
let timeRunning = 4000;
let timeAutoNext = 5000;

nextDom.onclick = function(){
    showSlider('next');    
}

prevDom.onclick = function(){
    showSlider('prev');    
}
let runTimeOut;
let runNextAuto = setTimeout(() => {
    next.click();
}, timeAutoNext)
function showSlider(type){
    let  SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
    let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
    if(type === 'next'){
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    }else{
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('prev');
    }
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning);

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => {
        next.click();
    }, timeAutoNext)
}









// ------------------Event Carousel-----------------
// Initialize Swiper
const swiper = new Swiper('.card-wrapper', {
    loop: false,
    spaceBetween: 30,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
      pauseOnMouseEnter: true,
    },
    breakpoints: {
      0: { slidesPerView: 1 },
      768: { slidesPerView: 2 },
      1024: { slidesPerView: 3 },
    },
  });
  
  // Tab filter logic
  const filterButtons = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.card-item');
  const noImagesMessage = document.getElementById('no-images-message');
  
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
  
      const filterValue = button.getAttribute('data-filter');
      let visibleCount = 0;
  
      // Filter cards
      cards.forEach(card => {
        if (filterValue === 'All' || card.classList.contains(filterValue)) {
          card.style.display = 'block';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });
  
      // Show/hide message
      if (visibleCount === 0) {
        noImagesMessage.style.display = 'block';
      } else {
        noImagesMessage.style.display = 'none';
      }
  
      // Update swiper slides
      swiper.update();
    });
  });
  
  // Optional: Make sure All button is active on load
  document.querySelector('[data-filter="All"]').click();
  









// ------------------Courses-----------------


const swiperCourses = new Swiper('.card_wrapper_courses', {
  loop: true,
  spaceBetween: 30,
  pagination: {
      el: '.swiper-pagination-courses',
      clickable: true,
      dynamicBullets: true,
  },
  navigation: {
      nextEl: '.swiper-button-next-courses',
      prevEl: '.swiper-button-prev-courses',
  },
  breakpoints: {
      0: {
          slidesPerView: 1,
      },
      768: {
          slidesPerView: 2,
      },
      1024: {
          slidesPerView: 3,
      }
  }
});
