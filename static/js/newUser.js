const loginBtn = document.querySelector("#login-btn");
const allColors = document.querySelectorAll(".btn-color");
const newUserForm = document.querySelector("#new-user-form");
const validationText = document.querySelector(".validation");
const userNameInput = document.querySelector("#user-name-input");

let authed = window.localStorage.getItem("UserName");

if (authed?.length > 0) {
  window.location.replace("/dashboard");
}

function chooseColor(i) {
  for (let i = 0; i < allColors.length; i++) {
    allColors[i].classList.remove("active-btn");
  }
  allColors[i].classList.add("active-btn");
  window.localStorage.setItem("UserColor", allColors[i].id);
}

for (let i = 0; i < allColors.length; i++) {
  allColors[i].addEventListener("click", function () {
    chooseColor(i);
  });
}

// creating new user and adding it to the users_db.text

newUserForm.addEventListener("submit", (event) => {
  if (
    !userNameInput.value.length > 0 ||
    !newUserForm.elements.namedItem("user").value
  ) {
    event.preventDefault();
    validationText.classList.add("active-validation");
  } else {
    //validationText.classList.remove("active-validation");
    const userName = newUserForm.elements.namedItem("name").value;

    window.localStorage.setItem("UserName", userName);
  }
});
