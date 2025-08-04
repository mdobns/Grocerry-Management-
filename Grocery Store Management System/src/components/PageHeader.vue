<template>
  <div class="page-header">
    <h1>{{ title }}</h1>
    <hr class="underline" />
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  }
});
</script>

<style scoped>
.page-header {
  width: 75%;
  margin: 40px auto 20px;
}

.page-header h1 {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
  text-align: left;
}

.underline {
  border: none;
  border-top: 2px solid #ccc;
  margin-top: 5px;
}
</style>
