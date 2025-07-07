async function checkRisk() {
  const incidents = document.getElementById("incidents").value;
  const last30 = document.getElementById("last30").value;
  const police = document.getElementById("police").value;

  const res = await fetch("/predict", {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      incidents: parseInt(incidents),
      last_30_days: parseInt(last30),
      police_presence: parseInt(police)
    })
  });

  const data = await res.json();
  const risk = data.risk_score;
  let msg = `⚠️ Danger Risk: ${risk}`;
  if (risk >= 0.7) msg += " (Very High)";
  else if (risk >= 0.4) msg += " (Moderate)";
  else msg += " (Low)";
  document.getElementById("output").innerText = msg;
}
