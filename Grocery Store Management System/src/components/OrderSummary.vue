<template>
  <div>
    <h3>Order Summary</h3>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.name }} x {{ item.quantity }} = ৳{{ item.total }}
      </li>
    </ul>
    <p><strong>Total: ৳{{ totalAmount }}</strong></p>
  </div>
</template>

<script>
export default {
  props: ['items'],
  computed: {
    totalAmount() {
      return this.items.reduce((sum, i) => sum + i.total, 0);
    }
  }
};
</script>
