function predictSpecies() {
    // Get input values
    const weight = parseFloat(document.getElementById("weight").value);
    const length1 = parseFloat(document.getElementById("length1").value);
    const length2 = parseFloat(document.getElementById("length2").value);
    const length3 = parseFloat(document.getElementById("length3").value);
    const height = parseFloat(document.getElementById("height").value);
    const width = parseFloat(document.getElementById("width").value);

    // Make a POST request to the model API
    fetch("https://your-heroku-app-url/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "length": length1,
            "width": width,
            "height": height,
            "width2": length2,
            "height2": length3,
            "weight": weight
        })
    })
    .then(response => response.json())
    .then(data => {
        const predictedSpecies = data.predicted_species;
        document.getElementById("predictedSpecies").innerText = predictedSpecies;
    })
    .catch(error => console.error("Error:", error));
}
