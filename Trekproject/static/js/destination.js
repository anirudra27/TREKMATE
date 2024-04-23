document.addEventListener("DOMContentLoaded", function() {
    const lookNowButtons = document.querySelectorAll(".look-now");
    lookNowButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            const itineraryId = this.getAttribute("data-itinerary-id");
            const itineraryDetailURL = `/itinerary/${itineraryId}/`;
            window.location.href = itineraryDetailURL;
        });
    });
});