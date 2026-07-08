console.log("script.js loaded");

async function analyzePrompt() {

    console.log("Analyze clicked");

    const prompt = document.getElementById("prompt").value;

    const sanitizeMode =
        document.getElementById("sanitizeMode").checked;

    const response = await fetch("http://localhost:7071/api/ClassifyPrompt", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            prompt: prompt,
            sanitize: sanitizeMode
        })

    });

    const data = await response.json();

    console.log(data);

    document.getElementById("risk").innerText = data.risk;
    document.getElementById("decision").innerText = data.decision;
    document.getElementById("pii").innerText = data.contains_pii;
    document.getElementById("categories").innerText = data.categories.join(", ");
    document.getElementById("reason").innerText = data.reason;

    const sanitizedSection =
        document.getElementById("sanitizedSection");

    if (data.decision === "SANITIZE") {

        sanitizedSection.style.display = "block";

        document.getElementById("sanitized").innerText =
            data.sanitized_prompt;

    } else {

        sanitizedSection.style.display = "none";

        document.getElementById("sanitized").innerText = "";

    }

}