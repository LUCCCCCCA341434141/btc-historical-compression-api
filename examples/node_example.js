import fetch from "node-fetch";

const API_URL = "https://api.btcinsights.online/compress";

async function run() {
  const payload = {
    start: "2018-01-01",
    end: "2020-01-01"
  };

  console.log("Sending request to BTC Compression API...");

  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const data = await response.json();

  console.log("\n=== Compression Result Summary ===");
  console.log("Range:", data.range.start, "→", data.range.end);
  console.log("Volatility:", data.statistics.volatility);
  console.log("Max Drawdown:", data.statistics.max_drawdown);
  console.log("Spike Days:", data.statistics.spike_days);

  console.log("\nMonthly Best:", data.monthly_analysis.best_months);
  console.log("Monthly Worst:", data.monthly_analysis.worst_months);

  console.log("\nSummary:");
  console.log(data.summary);
}

run();
