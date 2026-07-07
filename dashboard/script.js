console.log("script.js loaded");

async function analyzePrompt() {

    console.log("Analyze clicked");

    const prompt = document.getElementById("prompt").value;

    const response = await fetch("http://localhost:7071/api/ClassifyPrompt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            prompt: prompt
        })
    });

    const data = await response.json();

    console.log(data);

    document.getElementById("risk").innerText = data.risk;
    document.getElementById("decision").innerText = data.decision;
    document.getElementById("pii").innerText = data.contains_pii;
    document.getElementById("categories").innerText = data.categories.join(", ");
    document.getElementById("reason").innerText = data.reason;
    document.getElementById("sanitized").innerText = data.sanitized_prompt;
}