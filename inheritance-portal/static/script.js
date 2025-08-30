function updateCountdown() {
  const today = new Date();
  const nextMonth = new Date(today);
  nextMonth.setMonth(today.getMonth() + 1);

  document.getElementById("deadline").innerText = nextMonth.toDateString();

  function tick() {
    const now = new Date().getTime();
    const distance = nextMonth - now;

    if (distance <= 0) {
      document.getElementById("countdown").innerText = "Deadline Passed!";
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const mins = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const secs = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("countdown").innerText =
      `${days}d ${hours}h ${mins}m ${secs}s`;

    setTimeout(tick, 1000);
  }
  tick();
}
updateCountdown();