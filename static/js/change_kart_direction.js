async function changeDirection(direction) {
    let data = {
        "direction": direction
    };
    const response = await fetch('/change_direction', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    console.log(await response.json());
    return response;
}