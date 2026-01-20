function analyze() {
    let contract = document.getElementById("contract").value;

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({contract: contract})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerHTML =
            "<b>Clauses:</b> " + JSON.stringify(data.clauses) +
            "<br><b>Risks:</b> " + data.risks +
            "<br><b>Negotiation Tips:</b> " + data.negotiation_tips;
    });
}

function ask() {
    let q = document.getElementById("question").value;

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question: q})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("answer").innerText = data.answer;
    });
}