async function getPrice() {
  const laptop = document.getElementById("laptop").value;
  const condition = document.getElementById("condition").value;
  const market = document.getElementById("market").value;
  const resultDiv = document.getElementById("result");

  resultDiv.innerHTML = "⏳ Getting best deal advice...";

  const res = await fetch("http://127.0.0.1:5000/price-advisor", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ laptop, condition, market })
  });

  const data = await res.json();
  resultDiv.innerHTML = data.analysis;
}
