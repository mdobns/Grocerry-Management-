<template>
   <PageHeader title="Grocery Store Management System" />
  <div class="new-order-container">
    <div class="top-bar">
      <h2>New Order</h2>
      <div class="customer-name">
        <label>Customer Name:</label>
        <input v-model="customerName" type="text" placeholder="Enter customer name" />
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th>Product</th>
          <th>Price</th>
          <th>Quantity</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        
        <tr v-for="(item, index) in orderItems" :key="index">
          <td>
                    <select v-model="item.product" @change="onProductChange(index)">
          <option disabled value="">Select</option>
          <option v-for="p in products" :key="p.product_id" :value="p.product_name">
            {{ p.product_name }}
          </option>
        </select>

          </td>
          <td>{{ item.price}}</td>
          <td><input type="number" v-model.number="item.quantity" /></td>
          <td>{{ item.price * item.quantity || 0 }}</td>
        </tr>
      </tbody>
    </table>

    <div class="controls">
      <button class="add-btn" @click="addProductRow">+ Add Product</button>
    </div>

    <div class="total-section">
      <strong>Total:</strong> {{ totalTaka }} taka
    </div>

    <div class="save-button">
      <button @click="saveOrder">Save</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import PageHeader from '@/components/PageHeader.vue';

const customerName = ref('');
const products = ref([]);
const orderItems = ref([{ product: '', price: 0, quantity: 0 }]);


const fetchProducts = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/products');
    const data = await response.json();
    products.value = data;
  } catch (err) {
    console.error('Error fetching products:', err);
  }
};

const totalTaka = computed(() =>
  orderItems.value.reduce((acc, item) => acc + (item.price * item.quantity || 0), 0)
);


const addProductRow = () => {
  orderItems.value.push({ product: '', price: 0, quantity: 0 });
};


const saveOrder = async () => {
  const orderPayload = {
    customer_name: customerName.value,
    total: totalTaka.value,
    datetime: new Date().toISOString().slice(0, 19).replace('T', ' '),
  };

  try {
    const response = await fetch('http://127.0.0.1:5000/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(orderPayload)
    });

    if (!response.ok) throw new Error('Failed to save order');
    alert('Order saved successfully!');
    setTimeout(() => {
      window.location.href = '/';  // Redirect to home page
    }, 500); // Delay redirect to ensure alert is seen

    customerName.value = '';
    orderItems.value = [{ product: null, price: 0, quantity: 0 }];
  } catch (err) {
    console.error('Error saving order:', err);
    alert('Failed to save order.');
  }
};

onMounted(fetchProducts);

const onProductChange = (index) => {
  const selectedName = orderItems.value[index].product;
  const product = products.value.find(p => p.product_name === selectedName);
  if (product) {
    orderItems.value[index].price = product.price_per_unit;
  } else {
    orderItems.value[index].price = 0;
  }
};

</script>


<style scoped>
.new-order-container {
  width: 75%;
  margin: 40px auto;
  background: #fff;
  padding: 20px;
  border-radius: 6px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.customer-name input {
  padding: 6px;
  width: 200px;
  margin-left: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 10px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

select, input[type="number"] {
  width: 100%;
  padding: 6px;
  box-sizing: border-box;
}

.controls {
  text-align: left;
  margin-bottom: 20px;
}

.add-btn {
  background-color: #2196F3;
  color: white;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}

.add-btn:hover {
  background-color: #1976d2;
}

.total-section {
  text-align: right;
  font-size: 16px;
  margin-bottom: 20px;
}

.save-button {
  text-align: right;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.page-header {
    width: 75%;
    margin: 40px auto;
    margin-bottom: 20px;
}

.page-header h1 {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
  text-align: center;
}

.underline {
  border: none;
  border-top: 2px solid #ccc;
  margin-top: 5px;
}
</style>
