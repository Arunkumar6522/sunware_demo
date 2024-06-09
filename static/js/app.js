const containers = document.querySelectorAll(".input-container");
const form = document.querySelector("form");

const tl = gsap.timeline({ defaults: { duration: 1 } });

// Line
const start =
  "M0 0.999512C0 0.999512 60.5 0.999512 150 0.999512C239.5 0.999512 300 0.999512 300 0.999512";
const end =
  "M1 0.999512C1 0.999512 61.5 7.5 151 7.5C240.5 7.5 301 0.999512 301 0.999512";


$(document).ready(function () {
  $('.input-branch').select2();
});

// Revert back if it's not focused
form.addEventListener("click", () => {
  containers.forEach((container) => {
    const input = container.querySelector(".input");
    const line = container.querySelector(".elastic-line");
    const placeholder = container.querySelector(".placeholder");

    if (document.activeElement !== input) {
      if (!input.value) {
        gsap.to(placeholder, {
          top: 0,
          left: 0,
          scale: 1,
          duration: 0.5,
          ease: "Power2.easeOut",
        });
      }
    }

    // Name Validation
    input.addEventListener("input", (e) => {
      if (e.target.type === "text") {
        let inputText = e.target.value;
        if (inputText.length > 2) {
          colorize("#66FF00", line, placeholder);
        } else {
          colorize("#FF2400", line, placeholder);
        }
      }
      // Validate Email
      if (e.target.type === "email") {
        let valid = validateEmail(e.target.value);
        if (valid) {
          colorize("#66FF00", line, placeholder);
        } else {
          colorize("#FF2400", line, placeholder);
        }
      }
      // Validate Phone
      if (e.target.type === "tel") {
        let valid = validatePhone(e.target.value);
        if (valid) {
          colorize("#66FF00", line, placeholder);
        } else {
          colorize("#FF2400", line, placeholder);
        }
      }
    });
  });
});

// Validation functions
function validateEmail(email) {
  let re = /\S+@\S+\.\S+/;
  return re.test(email);
}

function validatePhone(phone) {
  let re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
  return re.test(phone);
}

// Colorize function
function colorize(color, line, placeholder) {
  gsap.to(line, { stroke: color, duration: 0.75 });
  gsap.to(placeholder, { color: color, duration: 0.75 });
}

// Animating Character
gsap.set("#eye", { transformOrigin: "center" });
gsap.fromTo(
  "#eye",
  { scaleY: 1 },
  {
    scaleY: 0.3,
    repeat: -1,
    yoyo: true,
    repeatDelay: 0.5,
    ease: "Power2.easeOut",
  }
);
gsap.fromTo(
  "#eyebrow",
  { y: 0 },
  { y: -1, repeat: -1, yoyo: true, repeatDelay: 0.5, ease: "Power2.easeOut" }
);

// Submit button
const PersonalSubmitbutton = document.getElementById("submitPersonalDataButton");
const TechnicalSubmitbutton = document.getElementById("submitTechDataButton")
const tl3 = gsap.timeline({
  defaults: { duration: 0.75, ease: "Power2.easeOut" },
});


const personalStepBtn = document.getElementById("personal");
const technicalStepBtn = document.getElementById("technical");
const submittedStepBtn = document.getElementById("submittedStep");

PersonalSubmitbutton.addEventListener("click", (e) => {
  e.preventDefault();
  const inputName = document.querySelector(".input-name");

  if (inputName.value.length > 2) {
    tl3.to(".contact-right, .contact-left", {
      y: 30,
      opacity: 0,
      pointerEvents: "none",
    });
    gsap.set(".contact-right", { opacity: 0, minHeight: 0, display: "none" });

    tl3.to("personal", { scale: 1 }, "<");

    tl3.fromTo(".technical", { display: "none", height: 0, y: 30 }, { display: "flex", y: 0 });

    // Hand wave
    gsap.set("#hand", { transformOrigin: "left" });
    gsap.fromTo(
      "#hand",
      { rotation: 0, y: 0 },
      { rotation: -10, y: 2, ease: "elastic(3,0.3)", duration: 2, delay: 1 }
    );

    // Update the URL to include the ID "submitted"
    history.pushState(null, null, "#technical");

    // Update progress bar
    personalStepBtn.classList.add("js-active");
    technicalStepBtn.classList.add("js-active");
    submittedStepBtn.classList.remove("");
  } else {
    alert("Input valid data!!!");
  }
});


TechnicalSubmitbutton.addEventListener("click", (e) => {
  e.preventDefault();
  const inputName = document.querySelector(".input-name");

  if (inputName.value.length > 2) {
    // If the condition is met, animate the hiding of the "technical" div
    tl3.to("technical", {
      y: 30,
      opacity: 0,
      pointerEvents: "none",
    });
    gsap.set(".technical", { opacity: 0, height: 0, display: "none" });
    tl3.to("technical", { scale: 0.8 }, "<");
    tl3.fromTo(".submitted", { opacity: 0, height: 0, y: 30 }, { opacity: 1, y: 0 });

    // Hand wave
    gsap.set("#hand", { transformOrigin: "left" });
    gsap.fromTo(
      "#hand",
      { rotation: 0, y: 0 },
      { rotation: -10, y: 2, ease: "elastic(3,0.3)", duration: 2, delay: 1 }
    );

    // Update the URL to include the ID "submitted"
    history.pushState(null, null, "#submitted");

    // Update progress bar
    personalStepBtn.classList.add("js-active");
    technicalStepBtn.classList.add("js-active");
    submittedStepBtn.classList.add("js-active");
  } else {
    alert("Input valid data!!!");
  }
});





document.addEventListener("DOMContentLoaded", function () {
  // Get the button element
  var formStepBtn = document.getElementById("personal");

  // Add click event listener to the button
  formStepBtn.addEventListener("click", function () {
    // Get the ID you want to pass to the URL
    var id = "personal";

    // Update the URL to include the ID
    history.pushState(null, null, "#" + id);
  });
});
