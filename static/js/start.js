async function start() {
    const response = await fetch('/start', {
        headers: {
          'Content-Type': 'application/json'
        },
    });
    document.getElementById("status").innerText = "Status: Its starting"
    return await response;
}