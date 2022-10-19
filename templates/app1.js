const sign_in_btn = document.querySelector("#first-btn");
const sign_up_btn = document.querySelector("#submit-pin");
const container = document.querySelector(".container");

container.classList.add("sign-up-mode");

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

