// mqtt properties
const mqtt = {
    broker: "broker.hivemq.com",
    port: 8000,
    topic: "iotlab/things/stromcek",
    clientId: `web-client-stromcek_${Math.random().toString(36).substr(2, 9)}`,
};

// the middle points of bulbs/lights on the image
const lights = [
    [147, 101],
    [188, 137],
    [116, 160],
    [156, 171],
    [214, 189],
    [186, 212],
    [128, 217],
    [86, 223],
    [77, 260],
    [236, 251],
    [191, 272],
    [133, 282],
    [77, 303],
    [230, 301],
];
