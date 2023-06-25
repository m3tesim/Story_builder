const oldurl = window.location.href;
const submitComment = document.querySelector("#submit-comment");
const story = document.querySelector("#stories");
const userName = document.querySelector("#comment-user-name");
const userColor = document.querySelector("#comment-user-color");

let authed = window.localStorage.getItem("UserName");

if (authed === null || authed === "") {
  window.location.replace("/");
} 

//this function relocate the user to the correct place after choosing a story headline
function formAction() {
  const commentFrorm = document.querySelector("#comment-form");
  commentFrorm.action = window.location.href;
}

// sends title of the story to the backend so it would update the comment section
function fetchStory() {
  //the list items in the html file "dashboard" with  id="stories" sends a value immediately once clicked , which i made it "default" to avoid refreshing the page in wrong way
  if (story.value !== "default") {
    let url = new URL("http://127.0.0.1:5000/dashboard");
    url.searchParams.append("story", story.value);
    // console.log(url,oldurl);
    if (url == oldurl) return;

    //storyTitle.textContent=url.searchParams.get("story").toUpperCase()
    window.location.replace(url);
  }

  //fetch(url)
}
userColor.value = localStorage.getItem("UserColor");
userName.value = localStorage.getItem("UserName");

story.addEventListener("click", fetchStory);
submitComment.addEventListener("click", formAction);
