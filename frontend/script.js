function addToCart(productName) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.push(productName);
    localStorage.setItem("cart", JSON.stringify(cart));
    alert(productName + " added to cart!");
  }
  
  function showCartItems() {
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const ul = document.getElementById("cart-items");
    ul.innerHTML = "";
    cart.forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      ul.appendChild(li);
    });
  }
  function checkout() {
    alert("Checkout feature coming soon!");
  }
  if (window.location.pathname.includes("cart.html")) {
    showCartItems();
  }
  
  function register() {
    const email = document.getElementById("register-email").value;
    const password = document.getElementById("register-password").value;
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .then(() => alert("Registered successfully!"))
      .catch((error) => alert(error.message));
  }
  
  function login() {
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then(() => alert("Login successful!"))
      .catch((error) => alert(error.message));
  }