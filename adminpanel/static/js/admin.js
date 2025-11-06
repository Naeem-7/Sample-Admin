document.addEventListener("DOMContentLoaded", () => {
    const approveButtons = document.querySelectorAll(".approve-btn");
  
    approveButtons.forEach(button => {
      button.addEventListener("click", () => {
        alert("Approval submitted!");
      });
    });
  });
  