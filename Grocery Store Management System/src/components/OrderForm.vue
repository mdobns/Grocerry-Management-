<template>
  <form @submit.prevent="submitOrder">
    <div v-for="product in products" :key="product.id">
      <label>
        {{ product.name }} (৳{{ product.price }})
        <input type="number" v-model.number="quantities[product.id]" min="0" />
      </label>
    </div>
    <button type="submit">Submit Order</button>
  </form>
</template>

<script>
export default {
  props: ['products'],
  data() {
    return { quantities: {} };
  },
  methods: {
    submitOrder() {
      const order = this.products
        .filter(p => this.quantities[p.id] > 0)
        .map(p => ({
          ...p,
          quantity: this.quantities[p.id],
          total: p.price * this.quantities[p.id]
        }));
      this.$emit('submit-order', order);
    },
  },
};
</script>
