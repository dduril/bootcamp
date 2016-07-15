var sayings = [
    "Frankly, my dear, I don't give a damn.",
    "I'm gonna make him an offer he can't refuse.",
    "Toto, I've got a feeling we're not in Kansas anymore.",
    "Here's looking at you, kid.",
    "Go ahead, make my day.",
    "All right, Mr. DeMille, I'm ready for my close-up.",
    "May the Force be with you.",
    "Fasten your seatbelts. It's going to be a bumpy night."
];

var interval = setInterval(function() {
    var i = Math.floor(Math.random() * sayings.length);
    process.stdout.write(`${sayings[i]} \n`);
}, 1000);

process.stdin.on('data', function(data) {
    console.log(`STDIN Data Received -> ${data.toString().trim()}`);
    clearInterval(interval)
    process.exit();
});