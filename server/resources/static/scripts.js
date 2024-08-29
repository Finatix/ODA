async function fetchDataFromAPI(url, options) {
    try {
        increaseLoadingCounter();
        const response = await fetch(url, options);
        const json = await response.json();
        decreaseLoadingCounter();
        return json;
    } catch (error) {
        console.error(error);
        decreaseLoadingCounter();
    }
}
let baseUrl = window.origin
let postConversationsURL = `${baseUrl}/api/conversations`;
let postConversationsOptions = {
    method: "POST",
    headers: {
        "Access-Allow-Origin": "*"
    }
}

async function postMessage (message) {
    let conversationList = JSON.parse(localStorage.getItem("conversations"));
    let activeConversationIndex = conversationList.findIndex((el) => el.active);
    let conversationToken = conversationList[activeConversationIndex].conversationToken;

    let postConversationsMessagesURL = `${baseUrl}/api/conversations/${conversationToken}/messages`;
    let postConversationsMessagesOptions = {
        method: "POST",
        headers: {
            "content-type": "application/json",
            "conversationToken": conversationToken,
        },
        body: JSON.stringify({
            "message": message})
    };

    let sendTime = new Date().toLocaleTimeString();
    conversationList[activeConversationIndex].messages.push({
        text: message,
        sender: "user",
        time: sendTime,
    });
    conversationList.lastMessageTime = sendTime;
    localStorage.setItem("conversations", JSON.stringify(conversationList));
    renderConversationList();
    addMessageToChat(message, "user", sendTime);

    fetchDataFromAPI(postConversationsMessagesURL, postConversationsMessagesOptions).then((response) => {
        let answer = response.response
        let receiveTime = new Date().toLocaleTimeString();

        addMessageToChat(answer, "ai", receiveTime);
        conversationList[activeConversationIndex].messages.push({
            text: answer,
            sender: "ai",
            time: receiveTime,
        })
        conversationList.lastMessageTime = receiveTime;
        localStorage.setItem("conversations", JSON.stringify(conversationList));
        renderConversationList();
    });
}

// Function to send message
function sendMessage(event) {
    let messageInput = document.querySelector("#message-input");
    let message = messageInput.value;
    messageInput.value = "";
    postMessage(message);
}

function addMessageToChat(message, author, time) {
    let chatMessages = document.getElementById("chat-messages");
    let messageContainer = document.createElement("div");
    messageContainer.classList.add("message-container");
    messageContainer.classList.add(author + "-message");
    let authorImage = (() => {
        if (author === "user") {
            let userImage = document.querySelector("#user-blueprint");
            return userImage.cloneNode(true);
        } else {
            let aiImage = document.querySelector("#oda-blueprint");
            return aiImage.cloneNode(true);
        }
    })();
    authorImage.id = "";
    authorImage.className = "avatar";
    authorImage.style.display = "";
    let messageContent = document.createElement("div");
    messageContent.className = "message-content";
    let senderHeadline = document.createElement("span");
    senderHeadline.className = "message-sender";
    senderHeadline.innerText = author === "user" ? "Du" : "ODA";
    let timeHeadline = document.createElement("span");
    timeHeadline.className = "message-time";
    timeHeadline.innerText = !time ? new Date().toLocaleTimeString() : time;
    let messageNode = document.createElement("p");
    messageNode.innerText = message;
    messageContent.appendChild(senderHeadline);
    messageContent.appendChild(timeHeadline);
    messageContent.appendChild(messageNode);
    if(author === "ai") messageContainer.appendChild(authorImage);
    messageContainer.appendChild(messageContent);
    if(author === "user") messageContainer.appendChild(authorImage);
    chatMessages.appendChild(messageContainer);
}

let _loadCounter = 0;
function increaseLoadingCounter() {
    _loadCounter++;
    checkLoadingSpinner();
}

function decreaseLoadingCounter() {
    _loadCounter--;
    checkLoadingSpinner();
}

function checkLoadingSpinner() {
    const spinner = document.querySelector(".loading-spinner");
    if (!spinner) { return; }

    spinner.setAttribute("data-counter", `${_loadCounter}`);
    if (_loadCounter > 0) {
        spinner.classList.add("active");
    } else {
        spinner.classList.remove("active");
    }
}

function addEventListeners() {
    // Event listener for mobile aside toggle
    document.querySelector(".mobile-toggle").addEventListener("click", () => {
        document.querySelector(".chat-aside").classList.toggle("visible");
    });

    // Event listener for send button click
    document.querySelector("#send-message-button").addEventListener("click", () => {
        sendMessage(conversationToken);
    });

    // Event listener for Enter key press
    document.querySelector("#message-input").addEventListener("keypress", e => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    // Event listener for add conversation button
    document.querySelector(".add-conversation").addEventListener("click", () => {
        addConversation();
    });
}

function addConversation(isActive) {
    let conversations = JSON.parse(localStorage.getItem("conversations"));
    if(!conversations) conversations = [];
    if(MAX_CONVERSATIONS <= conversations.length) {
        console.error("You have reached the limit of conversations. Please empty your cache if would like to create a new one.")
        return 0;
    }
    fetchDataFromAPI(postConversationsURL, postConversationsOptions).then((result) => {
        conversationToken = result.conversationToken;
        let conversationId = idCounter.getNextId();
        let creationTime = new Date().toLocaleTimeString();
        let newConversation = {
            title: "Conversation-" + (conversations.length+1),
            id: conversationId,
            nodeId: "conv-id-" + conversationId,
            conversationToken: conversationToken,
            active: Boolean(isActive),
            lastMessageTime: creationTime,
            messages: [
                {
                    time: creationTime,
                    sender: "ai",
                    text: ODA_GREETING_TEXT,
                },
            ],
        };
        conversations.push(newConversation);
        localStorage.setItem("conversations", JSON.stringify(conversations));
        renderConversationList();
        if(newConversation.active) {
            changeConversation(null, newConversation);
        }
    });
}

function changeConversation(event, conversationItem) {
    let conversationList = JSON.parse(localStorage.getItem("conversations"));
    conversationList = conversationList.map((el) => {
        el.active = el.id === conversationItem.id;
        return el;
    });
    localStorage.setItem("conversations", JSON.stringify(conversationList));
    renderConversationList();
    document.querySelector("#active-chat-title").innerText = conversationItem.title;
    renderMessages(conversationItem.messages);
}

function renderConversationList() {
    let conversationList = document.querySelector(".conversation-list");
    Array.from(conversationList.children).forEach(el => conversationList.removeChild(el))
    let conversations = JSON.parse(localStorage.getItem("conversations"));
    conversations = conversations.sort((a, b) => a.lastMessageTime < b.lastMessageTime);
    conversations.forEach((conversation) => {
        addConversationNode(conversation);
    });
}

function addConversationNode(conversationItem) {
    let conversationList = document.querySelector(".conversation-list");
    let articleNode = document.createElement("article");
    articleNode.id = conversationItem.nodeId;
    articleNode.classList.add("conversation-item");
    if(conversationItem.active) {
        articleNode.classList.add("active");
    }
    articleNode.addEventListener("click", (event) => { changeConversation(event, conversationItem); });
    let convHeading = document.createElement("p");
    convHeading.className = "conversation-item-name font-weight-bold";
    convHeading.innerText = conversationItem.title;
    let convPreview = document.createElement("p");
    convPreview.className = "conversation-preview";
    convPreview.innerText = getLastMessageText(conversationItem).slice(0, 30) + "...";
    articleNode.appendChild(convHeading);
    articleNode.appendChild(convPreview);
    conversationList.appendChild(articleNode);
}

function getLastMessageText(conversationItem) {
    if (!conversationItem.messages) {
        return "";
    }
    let text = "";
    for (const message of conversationItem.messages) {
        if (message.text) {
            text = message.text;
        }
    }
    return text;
}

function renderMessages(messages) {
    let chatBox = document.querySelector("#chat-messages");
    Array.from(chatBox.children).forEach(el => chatBox.removeChild(el));
    messages.forEach(msg => addMessageToChat(msg.text, msg.sender, msg.time));
}

const MAX_CONVERSATIONS = 10;
const ODA_GREETING_TEXT = "Hallo! Ich bin ODA, die Open Data Assistant der Stadt Leipzig. Ich helfe Dir gerne beim Durchsuchen der Open Data Kataloge der Partnerstädte Leipzig, Hamburg, Berlin und München. Wähle dazu oben rechts deine gewünschte Stadt aus.";

waitForElements()
function waitForElements() {
    let chatboxButton = document.querySelector("#chat-box button");
    if(!chatboxButton) {
        setTimeout(waitForElements, 200);
    } else {
        initializeApp();
    }
}

let idCounter;
function initializeApp() {
    let baseConvId = 0;
    let conversationList = JSON.parse(localStorage.getItem("conversations"));
    if(conversationList) {
        baseConvId = conversationList.sort((a, b) => a.id < b.id)[0] + 1;
    }
    idCounter = (function incrementId() {
        let startId = baseConvId;
        return {
            getNextId() {
                return startId++;
            }
        }
    })();

    addEventListeners();

    if(!conversationList) {
        addConversation(true);
    } else {
        renderConversationList();
        let activeConversations = conversationList.filter(el => el.active > 0);
        if(0 < activeConversations.length) {
            changeConversation(null, activeConversations[0]);
        }
    }
}

function logConversations() {
    return JSON.parse(localStorage.getItem("conversations"));
}