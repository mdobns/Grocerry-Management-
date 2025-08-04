<template>
  <PageHeader title="Grocery Store Management System" />

  <div class="spreadsheet-container">
    <div class="header-controls">
      <h3>Manage Products</h3>
    <div class="action-buttons">
  <button class="button-link" @click="showModal = true">
    <h3>Add New Product</h3>
  </button>
</div>

<AddNewProduct v-if="showModal" @close="showModal = false" />


    </div>

    <table class="table-default">
      <thead>
        <tr>
          <th>Name</th>
          <th>Unit</th>
          <th>Price per Unit</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.products_id">
          <td>{{ product.product_name }}</td>
          <td>{{ product.ucom_name }}</td>
          <td>{{ product.price_per_unit }} Taka</td>
          <td> 
            <button class="button-link delete" @click="deleteProduct(product.product_id)">
              Delete
            </button> 
          </td>

       
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import PageHeader from '@/components/PageHeader.vue';
import AddNewProduct from './AddNewProduct.vue';

const showModal = ref(false);
const products = ref([]);

// Fetch function
const fetchProducts = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/products');
    const data = await response.json();
    console.log('Fetched data:', data);
    products.value = data;
  } catch (error) {
    console.error('Failed to load products:', error);
  }
};

// Fetch initially
onMounted(fetchProducts);

// 👇 Watch for modal close to refetch products
watch(showModal, (newVal, oldVal) => {
  if (oldVal === true && newVal === false) {
    fetchProducts();
  }
});

const deleteProduct = async (id) => {
  const confirmDelete = confirm("Are you sure you want to delete this product?");
  if (!confirmDelete) return;

  try {
    const response = await fetch(`http://127.0.0.1:5000/products/${id}`, {
      method: 'DELETE',
    });
    const result = await response.json();
    console.log(result);

    if (result.status === 'success') {
      products.value = products.value.filter(p => p.product_id !== id);
      alert('Successfully deleted: ' + result.message);
    } else {
      alert('Failed to delete: ' + result.message);
    }
  } catch (error) {
    console.error('Delete error:', error);
    alert('An error occurred while deleting the product.');
  }
};
</script>


<style scoped>



</style>
