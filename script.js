const titleBanner = document.querySelector(".title-banner");
const titleMain = document.querySelector(".title-main");

if (titleBanner && titleMain) {
  let letterIndex = 0;

  titleMain.querySelectorAll(".title-word").forEach((word) => {
    const text = word.textContent;
    word.textContent = "";
    [...text].forEach((character) => {
      const letter = document.createElement("span");
      letter.className = "title-letter";
      letter.textContent = character;
      letter.style.setProperty("--i", letterIndex);
      letter.setAttribute("aria-hidden", "true");
      word.appendChild(letter);
      letterIndex += 1;
    });
  });

  const sparks = document.querySelector(".title-sparks");
  if (sparks) {
    for (let i = 0; i < 18; i += 1) {
      const spark = document.createElement("span");
      spark.className = "spark";
      spark.style.left = `${Math.random() * 100}%`;
      spark.style.animationDelay = `${(Math.random() * 7).toFixed(2)}s`;
      spark.style.animationDuration = `${(5 + Math.random() * 5).toFixed(2)}s`;
      spark.style.setProperty("--drift", `${(Math.random() * 50 - 25).toFixed(1)}px`);
      sparks.appendChild(spark);
    }
  }

  const playTitle = () => {
    if (document.hidden) return;
    titleBanner.classList.remove("is-playing");
    void titleBanner.offsetWidth;
    titleBanner.classList.add("is-playing");
  };

  playTitle();

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let bannerVisible = true;

  if ("IntersectionObserver" in window) {
    new IntersectionObserver(
      (entries) => {
        bannerVisible = entries[0].isIntersecting;
      },
      { threshold: 0.15 }
    ).observe(titleBanner);
  }

  window.setInterval(() => {
    if (bannerVisible && !reduceMotion.matches) playTitle();
  }, 10000);
}

const nav = document.getElementById("nav");
const navToggle = document.getElementById("navToggle");

function closeNav() {
  nav.classList.remove("open");
  navToggle.classList.remove("open");
  navToggle.setAttribute("aria-expanded", "false");
}

navToggle.addEventListener("click", () => {
  const isOpen = nav.classList.toggle("open");
  navToggle.classList.toggle("open", isOpen);
  navToggle.setAttribute("aria-expanded", String(isOpen));
});

nav.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", closeNav);
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closeNav();
});

const form = document.getElementById("contactForm");
const note = document.getElementById("formNote");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const validEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  note.classList.remove("is-error", "is-success");

  if (!name || !validEmail) {
    note.textContent = "Please add your name and a valid work email.";
    note.classList.add("is-error");
    return;
  }

  note.textContent = "Thank you. Your enquiry has been noted — we'll be in touch.";
  note.classList.add("is-success");
  form.reset();
});

document.getElementById("year").textContent = new Date().getFullYear();
