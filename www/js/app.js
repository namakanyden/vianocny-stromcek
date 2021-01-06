// called when a message arrives
function onMessageArrived(message) {
    const payload = JSON.parse(message.payloadString);
    console.log(`>> received payload: ${message.payloadString}`);
    document.getElementById("current-scenario").innerText = payload.scenario;
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log(`onConnectionLost: ${responseObject.errorMessage}`);
    }
}

function publish_message(client, payload) {
    const msg = JSON.stringify(payload);
    console.log(`>> sending payload ${msg}.`);

    const message = new Paho.MQTT.Message(msg);
    message.destinationName = mqtt.topic;
    message.retained = true;
    client.send(message);
}

window.addEventListener("load", function (event) {
    // handling set effect button
    document
        .getElementById("btn-set")
        .addEventListener("click", function (event) {
            // get animation
            const animation = document.getElementById("list-of-animations")
                .value;
            if (animation.length == 0) {
                return;
            }

            // get color and delay
            const color = document.getElementById("colorpicker").value;
            const delay = document.getElementById("delay").value;

            // prepare data
            const payload = {
                scenario: animation,
                color: color,
                duration: delay,
            };

            // send message
            publish_message(client, payload);
        });

    // show description, when selection has changed
    document
        .querySelector("#list-of-animations")
        .addEventListener("change", function (event) {
            const element = document.querySelector(
                "#list-of-animations option:checked"
            );

            document.querySelector("#scenario-description").textContent =
                element.dataset.description;
        });

    // handle click events on tree image
    document.getElementById("tree").addEventListener("click", function (event) {
        const x = event.offsetX;
        const y = event.offsetY;

        // check, if coords are inside of the bulb
        lights.forEach(function (light, index) {
            const d = Math.sqrt(
                Math.pow(x - light[0], 2) + Math.pow(y - light[1], 2)
            );

            // if we found clicked bulb, send a message
            if (d < 10) {
                // console.log(`>> Clicked light ${index} with coords ${light}.`);

                // prepare the payload
                payload = {
                    scenario: "part of tree",
                    color: document.getElementById("colorpicker").value,
                    index: index, // index of selected light/part
                    parts: 14, // number of all lights on the image
                };

                // send message
                publish_message(client, payload);
            }
        });
    });

    // the main program

    // Create a MQTT client instance
    const client = new Paho.MQTT.Client(
        mqtt.broker,
        mqtt.port,
        "/mqtt",
        mqtt.clientId
    );

    // set callback handlers
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;

    // connect client
    client.connect({
        onSuccess: function () {
            // subscribe client to topic
            client.subscribe(mqtt.topic);
        },
    });
});
