async function predict() {
    let age = Number(document.getElementById("age").value);
    let income = Number(document.getElementById("income").value);
    let education = Number(document.getElementById("education").value);

    // Validate inputs
    if (isNaN(age) || isNaN(income) || isNaN(education)) {
        document.getElementById("result").innerText = "Please enter valid numbers.";
        return;
    }

    try {
        let response = await fetch("https://inspiration.pythonanywhere.com/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ age, income, education })
        });

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        let data = await response.json();
        document.getElementById("result").innerText =
            "Predicted party: " + data.party;
    } catch (error) {
        document.getElementById("result").innerText =
            "Error: " + error.message;
    }
}

async function loadLeaderboard() {
    let response = await fetch("https://inspiration.pythonanywhere.com/leaderboard");
    let data = await response.json();

    let board = document.getElementById("board");
    board.innerHTML = `<h3>Leader: ${data.leader}</h3>`;

    for (let party in data.parties) {
        let info = data.parties[party];
        board.innerHTML += `
            <p>
                <b>${party}</b>: 
                ${info.votes} votes 
                (${info.percentage}%)
            </p>
        `;
    }
}

// Load when page opens
loadLeaderboard();
