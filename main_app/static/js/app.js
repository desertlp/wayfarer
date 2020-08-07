// const str = $('.card-text').html();
// console.log(str);

// function truncateString(str, num) {
//     if( num >= str.length ) {
//       return str;  
//     }
//       const newFormat = str.substr(0, num)  
//       return `${newFormat}...`; 
//   }
//   truncateString("A-tisket a-tasket A green and yellow basket","A-tisket a-tasket A green and yellow basket".length);

const deletePost = document.querySelector(".post-delete-button");
const troubleButton = document.querySelector(".trouble-shooting-button");

troubleButton.addEventListener("click", () => {
	console.log("clicked the button!!!");
});
