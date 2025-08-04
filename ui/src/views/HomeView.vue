<template>
<PageHeader title="Grocery Store Management System" />

  <div class="spreadsheet-container">
    <div class="header-controls">
      <h3>All Orders</h3>
      <div class="action-buttons">
      <router-link to="/manage-products" class="button-link"><h3>Manage Products</h3></router-link>
      <router-link to="/order" class="button-link delete"><h3>New Order</h3></router-link>
      </div>
      </div>
      
   

    <table class="table-default">
      <thead>
        <tr>
          <th>Date</th>
          <th>Order Number</th>
          <th>Customer Name</th>
          <th>Total Cost</th>
        </tr>
      </thead>
        <tbody>
        <tr v-for="(order, index) in orders" :key="order.order_id || index">
          <td>{{ order.order_id }}</td>
          <td>{{ order.customer_name }}</td>
          <td>{{ order.total.toFixed(2) }} Taka</td>
          <td>{{ new Date(order.datetime).toLocaleString() }}</td>
        </tr>
  </tbody>

    </table>
  </div>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue';
import { ref, onMounted } from 'vue';

const orders = ref([]);

const fetchOrders = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/orders');
    const data = await response.json();
    console.log('Fetched data:', data);
    orders.value = data;
  } catch (error) {
    console.error('Failed to load orders:', error);
  }
};

onMounted(fetchOrders);



</script>

<style scoped>
.spreadsheet-container {
  width: 75%;
  margin: 40px auto; /* ← centers horizontally */
  overflow-x: auto;
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  padding: 20px;
  font-family: Arial, sans-serif;
}


</style>
