const submitButton = document.querySelector("#submit");
const storyInput = document.querySelector("#story-input");
const validationText = document.querySelector("#validation");
const feedBackText = document.querySelector("#feedback");

//add a feedback to create story input if wrong input is used
function validation() {
  if (!storyInput.value.length > 0) {
    validationText.classList.add("active-validation");
    return false;
  } else {
    validationText.classList.remove("active-validation");

    return true;
  }
}
