<template>
  <div class="modal-overlay fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div class="modal">
      <h2>Add New Product</h2>
      <form @submit.prevent="submitProduct">
        <label>
          Product Name:
          <input v-model="newProduct.product_name" required />
        </label>

        <label>
          Unit:
          <select v-model="newProduct.ucom_id" required>
            <option value="">-- Select Unit --</option>
            <option v-for="unit in ucomList" :key="unit.ucom_id" :value="unit.ucom_id">
              {{ unit.ucom_name }}
            </option>
          </select>
        </label>

        <label>
          Price per Unit:
          <input type="number" v-model="newProduct.price_per_unit" required />
        </label>

        <div class="modal-actions">
          <button type="submit">Submit</button>
          <button type="button" @click="cancel">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const emit = defineEmits(['close', 'added']);

const newProduct = ref({
  product_name: '',
  ucom_id: '',
  price_per_unit: ''
});

const ucomList = ref([]);

const fetchUcomUnits = async () => {
  try {
    const res = await fetch('http://127.0.0.1:5000/ucom');
    ucomList.value = await res.json();
  } catch (err) {
    console.error('Failed to load units:', err);
  }
};

const submitProduct = async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/products', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newProduct.value),
    });
    const result = await response.json();

    if (result.status === 'success') {
      emit('added');
      emit('close');
      newProduct.value = { product_name: '', ucom_id: '', price_per_unit: '' };
    } else {
      alert('Failed to add: ' + result.message);
    }
  } catch (error) {
    alert('An error occurred while adding the product.');
  }
};

const cancel = () => {
  emit('close');
};

onMounted(() => {
  fetchUcomUnits();
});
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 350px;
  max-width: 90%;
}

.modal label {
  display: block;
  margin-bottom: 10px;

}

.modal input,
.modal select {
  width: 100%;
  padding: 5px;
  margin-top: 5px;
  margin-bottom: 15px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}
</style>
