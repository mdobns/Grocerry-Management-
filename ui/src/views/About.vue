<template>
  <div class="about-page">
    <div class="header">
      <h1>About Grocery Management App</h1>
    </div>

    <div class="content">
      <section class="project-info">
        <h2>Project Overview</h2>
        <p>
          Welcome to the Grocery Management App! This app is designed to help businesses efficiently manage their grocery store inventory and orders. Built with Vue.js for the frontend and Flask for the backend, this system provides a seamless experience for adding, managing, and tracking products and orders.
        </p>
        <ul>
          <li><strong>Frontend:</strong> Vue.js, HTML, CSS, JavaScript</li>
          <li><strong>Backend:</strong> Flask, Python</li>
          <li><strong>Database:</strong> MySQL </li>
          <li><strong>Authentication:</strong> Not implemented (can be added in future)</li>
        </ul>
      </section>

      <section class="features">
        <h2>Key Features</h2>
        <ul>
          <li>Manage grocery products</li>
          <li>Track orders with product details</li>
          <li>Responsive design for both mobile and desktop</li>
          <li>Easy-to-use interface for adding new products and orders</li>
        </ul>
      </section>

      <section class="about-me">
        <h2>About Me</h2>
        <p>
          Hi! I'm <strong>Md Oshama Bin Nur</strong>, the developer behind this app. I am passionate about building full-stack web applications and solving real-world problems through technology. I created this Grocery Management App to practice my skills in Vue.js, Flask, and database integration. If you want to learn more or get in touch with me, feel free to reach out!
        </p>
      </section>
    </div>

    <div class="footer">
      <p>&copy; 2025 Md Oshama Bin Nur | All Rights Reserved</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About',
};
</script>

<style scoped>
.about-page {
  width: 80%;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  border-radius: 8px;
}

.header {
  text-align: center;
  margin-bottom: 30px;
}

.header h1 {
  font-size: 32px;
  color: #333;
}

.content {
  background-color: #fff;
  padding: 20px;
  border-radius: 6px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

section {
  margin-bottom: 20px;
}

section h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

section p {
  font-size: 16px;
  line-height: 1.6;
  color: #555;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul li {
  font-size: 16px;
  margin-bottom: 10px;
}

ul li strong {
  font-weight: bold;
}

.footer {
  text-align: center;
  margin-top: 30px;
  font-size: 14px;
  color: #888;
}
</style>
