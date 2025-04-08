// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB6orezruYcHbOJqgKvhbPk4z8rws78Qy8",
  authDomain: "cc-lab-6-9d038.firebaseapp.com",
  projectId: "cc-lab-6-9d038",
  storageBucket: "cc-lab-6-9d038.firebasestorage.app",
  messagingSenderId: "1078182586191",
  appId: "1:1078182586191:web:dbdd859189c2edb34d873a",
  measurementId: "G-FRPMWY8JH3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);