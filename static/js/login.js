const loginBtn = document.querySelector("#login-btn");
const allUsers = document.querySelectorAll(".btn-color");
const loginForm = document.querySelector("#login-form");
const search = document.querySelector("#search");
const validationText = document.querySelector("#validation");

function search_users() {
  let input = document.getElementById("search").value;
  input = input.toLowerCase();
  let users = document.getElementsByClassName("btn-color");

  for (let i = 0; i < users.length; i++) {
    if (!users[i].textContent.toLowerCase().includes(input)) {
      users[i].style.display = "none";
    } else {
      users[i].style.display = "block";
    }
  }
}

// saves login info in the local storage
function login() {
  const userName = loginForm.elements.namedItem("user").value;

  if (userName === "") return false;
  window.localStorage.setItem("UserName", userName);
  return true;
}

//as user choose user name to login it activate a class style ,and remove it after
function chooseUser(i) {
  for (let i = 0; i < allUsers.length; i++) {
    allUsers[i].classList.remove("active-btn");
  }
  allUsers[i].classList.add("active-btn");
  window.localStorage.setItem("UserColor", allUsers[i].id);
}

for (let i = 0; i < allUsers.length; i++) {
  allUsers[i].addEventListener("click", function () {
    chooseUser(i);
  });
}

loginForm.addEventListener("submit", (event) => {
  if (!login()) {
    event.preventDefault();
    validationText.classList.add("active-validation");
  } else {
    validationText.classList.remove("active-validation");
  }
});
