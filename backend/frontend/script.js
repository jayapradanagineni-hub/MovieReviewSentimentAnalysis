async function analyzeReview() {

    const review = document.getElementById("review").value.trim();
    const result = document.getElementById("result");
    const button = document.getElementById("analyzeBtn");

    if (review === "") {
        result.innerHTML = "<p class='error'>Please enter a movie review!</p>";
        return;
    }

    button.disabled = true;
    button.innerText = "Analyzing...";
    result.innerHTML = "🔄 Analyzing your review...";

    try {

        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                review: review
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        if (data.sentiment === "Positive") {
            result.innerHTML = "<p class='positive'>😊 Positive Review</p>";
        } else {
            result.innerHTML = "<p class='negative'>😞 Negative Review</p>";
        }

    } catch (error) {

        result.innerHTML = "<p class='error'>Unable to connect to the backend. Please check whether Flask is running.</p>";

    } finally {

        button.disabled = false;
        button.innerText = "Analyze Review";

    }
}