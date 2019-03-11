importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-messaging.js');

let config = {
    apiKey: "AIzaSyDtTBgUjVfgs1VK4kT7wOIQZdrSy4TaxpE",
    authDomain: "webtechnika-push-notifications.firebaseapp.com",
    projectId: "webtechnika-push-notifications",
    messagingSenderId: "985803724883"
};

firebase.initializeApp(config);

const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
    console.log('[firebase-messaging-sw.js] Received background message ', payload);
    var notificationTitle = 'Background Message Title';
    var notificationOptions = {
        body: 'Background Message body.',
        icon: '/firebase-logo.png'
    };

    return self.registration.showNotification(notificationTitle,
        notificationOptions);
});