// login.js
import { auth } from './firebase-config.js';
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} from 'https://www.gstatic.com/firebasejs/9.22.2/firebase-auth.js';

const loginForm = document.getElementById('login-form');
const toggleMsg = document.getElementById('toggle-msg');

let isLogin = true;

loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  try {
    if (isLogin) {
      // Login
      await signInWithEmailAndPassword(auth, email, password);
      alert('Login successful!');
      window.location.href = 'index.html';
    } else {
      // Register
      await createUserWithEmailAndPassword(auth, email, password);
      alert('Registration successful! Now you can log in.');
      isLogin = true;
      updateForm();
    }
  } catch (error) {
    alert(error.message);
  }
});

toggleMsg.addEventListener('click', () => {
  isLogin = !isLogin;
  updateForm();
});

function updateForm() {
  document.getElementById('submit-btn').textContent = isLogin ? 'Login' : 'Register';
  toggleMsg.innerHTML = isLogin
    ? `Don't have an account? <a href="#">Register</a>`
    : `Already have an account? <a href="#">Login</a>`;
}
