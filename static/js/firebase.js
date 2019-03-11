let config = {
    apiKey: "AIzaSyDtTBgUjVfgs1VK4kT7wOIQZdrSy4TaxpE",
    authDomain: "webtechnika-push-notifications.firebaseapp.com",
    projectId: "webtechnika-push-notifications",
    messagingSenderId: "985803724883"
};

firebase.initializeApp(config);

const messaging = firebase.messaging();

messaging.getToken().then(function (currentToken) {
    if (currentToken) {
        console.log(currentToken);
    } else {
        console.log('No Instance ID token available. Request permission to generate one.');
    }
}).catch(function (err) {
    console.log('An error occurred while retrieving token. ', err);
});

messaging.onTokenRefresh(function () {
    messaging.getToken().then(function (refreshedToken) {
        console.log('Token refreshed.');
        console.log(refreshedToken);
    }).catch(function (err) {
        console.log('Unable to retrieve refreshed token ', err);
    });
});

messaging.onMessage(function(payload) {
  console.log('Message received. ', payload);
  // ...
});

$(document).ready(function() {
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function () {
            navigator.serviceWorker.register('/firebase-messaging-sw.js').then(function (registration) {
                // Registration was successful
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
            }, function (err) {
                // registration failed :(
                console.log('ServiceWorker registration failed: ', err);
            });
        });
    }
});