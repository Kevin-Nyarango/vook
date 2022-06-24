
//select the get in touch btn
const openModalBtn = document.querySelector('.open-modal');
//select the hire me btn
const openModalBtn2 = document.querySelector('.open-modal-2');
//select the modal
const modal = document.querySelector('.modal');
//select the close btn
const modalCloseBtn = document.querySelector('.modal-close-btn')
//select the get in touch btn on mobile single post page
const openModalBtnMobileSinglePost = document.querySelector('.get-in-touch-single-blog-btn')


const mobileWidth = window.matchMedia("(max-width: 799px)")


// Show Modal
showModal = () => {
  modal.style.display = 'block';
}
// Hide Modal
closeModal = () => {
  modal.style.display = 'none';
}

// Hide Modal if outside click
function modalClick(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
}

if (modal) {

  // Listen for a Click Event to display the form
  if (openModalBtn) {
    openModalBtn.addEventListener('click', e => {
      showModal();
    })
  }

  // Listen for a Click Event to display the form (click on the hire me btn)
  if (openModalBtn2) {
    openModalBtn2.addEventListener('click', e => {
      showModal();
    })
  }

  // Listen for a Click Event to the Modal Close Button

  modalCloseBtn.addEventListener('click', e => {
    closeModal();
  })

  // Listen for a Click Event outside the form to close the Modal
  window.addEventListener('click', modalClick);


}

// making the get in touch btn on mobile single post page visible after 45 seconds
if (openModalBtnMobileSinglePost) {

  maxWidthBtnMobileSinglePost = (mobileWidth) => {
    if (mobileWidth.matches) { // If media query matches

      setTimeout(showBtnMobileSinglePost = () => {
        openModalBtnMobileSinglePost.style.display = 'block'
      }, 45000);
    } else {
      openModalBtnMobileSinglePost.style.display = 'none'
    }
  }
  //calling the maxWidthBtnMobileSinglePost function
  maxWidthBtnMobileSinglePost(mobileWidth)
}





// window.addEventListener('DOMContentLoaded', setup());
// Intersection Observers
