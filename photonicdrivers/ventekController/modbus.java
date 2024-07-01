// Import the Modbus client library
var Modbus = global.get('modbus');

// Create a Modbus client instance
var client = new Modbus();

// Define the Modbus TCP server configuration
var serverConfig = {
    'host': '10.209.67.120', // Replace with your Modbus server IP address
    'port': 502, // Default Modbus TCP port
};

// Connect to the Modbus TCP server
client.connectTCP(serverConfig);

// Function to handle the Modbus TCP read request and convert to 32-bit float
function readModbus() {
    // Read the 16-bit integer value from Modbus register 30000
    client.readInputRegisters(30000, 1)
        .then(function (data) {
            // Extract the 16-bit integer value from the response
            var int16Value = data.response.data[0];

            // Convert the 16-bit integer value to a 32-bit float
            var float32Value = new Float32Array([int16Value])[0];

            // Send the float value to the next Node-RED node
            node.send({ payload: float32Value });
        })
        .catch(function (err) {
            // Log any errors
            node.error(err);
        });
}

// Trigger the readModbus function when the node receives an input
node.on('input', function (msg) {
    readModbus();
});

// Close the Modbus TCP connection when the Node-RED flow is stopped
node.on('close', function () {
    client.close();
});
