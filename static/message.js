window.onload = function() {
    // If there are any success messages
    if (document.getElementById("successMessage")) {
        // Show the message
        document.getElementById("successMessage").style.display = "block";

        // Set timeout to fade out the message after 3 seconds
        setTimeout(function() {
            document.getElementById("successMessage").style.display = "none";
        }, 3000);  // 3000 milliseconds = 3 seconds
    }
};
