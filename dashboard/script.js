console.log("script.js loaded");

async function analyzePrompt() {

    const prompt = document.getElementById("prompt").value;

    const sanitizeMode =
        document.getElementById("sanitizeMode").checked;

    const button =
        document.querySelector("button");

    button.disabled = true;

    button.innerText = "Scanning...";

    const response = await fetch(
        "http://localhost:7071/api/ClassifyPrompt",
        {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                prompt:prompt,

                sanitize:sanitizeMode

            })

        }
    );

    const data = await response.json();

    button.disabled = false;

    button.innerText = "Analyze";

    /* -----------------------------
       Risk
    ----------------------------- */

    const risk =
        document.getElementById("risk");

    risk.innerText = data.risk;

    risk.className="";

    if(data.risk==="LOW")
        risk.classList.add("risk-low");

    if(data.risk==="MEDIUM")
        risk.classList.add("risk-medium");

    if(data.risk==="HIGH")
        risk.classList.add("risk-high");



    /* -----------------------------
       Decision
    ----------------------------- */

    const decision =
        document.getElementById("decision");

    decision.innerText=data.decision;

    decision.className="";

    if(data.decision==="ALLOW")
        decision.classList.add("decision-allow");

    if(data.decision==="SANITIZE")
        decision.classList.add("decision-sanitize");

    if(data.decision==="BLOCK")
        decision.classList.add("decision-block");



    document.getElementById("pii").innerText =
        data.contains_pii;

    document.getElementById("reason").innerText =
        data.reason;



    /* -----------------------------
       Categories
    ----------------------------- */

    const categoryBox =
        document.getElementById("categories");

    categoryBox.innerHTML="";

    data.categories.forEach(cat=>{

        categoryBox.innerHTML +=
        `<span class="category-tag">${cat}</span>`;

    });



    /* -----------------------------
       Risk Score
    ----------------------------- */

    document.getElementById("riskBar").style.width =
        data.risk_score+"%";



    /* -----------------------------
       Confidence
    ----------------------------- */

    document.getElementById("confidenceBar").style.width =
        data.confidence+"%";



    /* -----------------------------
       Sanitized Prompt
    ----------------------------- */

    if(data.decision==="SANITIZE"){

        document.getElementById(
            "sanitizedSection"
        ).style.display="block";

        document.getElementById(
            "sanitized"
        ).innerText=data.sanitized_prompt;

    }

    else{

        document.getElementById(
            "sanitizedSection"
        ).style.display="none";

    }

}