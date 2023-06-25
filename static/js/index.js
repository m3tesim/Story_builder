const logOutLink = document.getElementById("log-out");
const logedUser = document.getElementById("current-user");
const user = localStorage.getItem("UserName");
if (logedUser) logedUser.textContent = user;

//clear local storage once the user log out
function logOut() {
  localStorage.clear();
}

logOutLink?.addEventListener("click", logOut);

// this function works on the info page as  "hot it works" link  is accessible in the header on all pages
//i have added authentication so user who is not logged in wouldn't  find himself in the dashboard page
function authorised() {
  let authed = window.localStorage.getItem("UserName");

  if (authed === null || authed === "") {
    window.location.replace("/");
  } else {
    window.location.replace("/dashboard");
  }
}
