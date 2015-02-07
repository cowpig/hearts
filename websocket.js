"use strict";

var wsUri = "" // TODO: put the endpoint here
var websocket = new WebSocket(wsUri);


function init() { 
	prepareWebsocket();
	// bind a function with `websocket.send(changes)` to some kind of onChange trigger
}

function onOpen(evt) { 
	writeToScreen("CONNECTED");
}

function onClose(evt) { 
	writeToScreen("DISCONNECTED");
}

function onMessage(evt) {
	// here's where we apply changes to DOM
	console.log("data received:\n" + JSON.stringify(evt));
}

function onError(evt) { 
	writeToScreen('<span style="color: red;">ERROR:</span> ' + evt.data);
}

function prepareWebsocket() {
	websocket.onopen = function(evt) { onOpen(evt) };
	websocket.onclose = function(evt) { onClose(evt) };
	websocket.onmessage = function(evt) { onMessage(evt) };
	websocket.onerror = function(evt) { onError(evt) };
}

function writeToScreen(message) { 
	document.write(message);
}


$("document").ready(init);
