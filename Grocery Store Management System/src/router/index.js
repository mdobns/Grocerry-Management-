import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import ManageProducts from '@/views/ManageProducts.vue';
import OrderPage from '@/views/OrderPage.vue';
import About from '@/views/About.vue';
import '../assets/global.css';


const routes = [
  { 
    path: '/', 
    name: 'Home', 
    component: HomeView 
  },
  { 
    path: '/about', 
    name: 'About', 
    component: About 
  },
  { path: '/manage-products', 
    name: 'ManageProducts', 
    component: ManageProducts 
  },
  { path: '/order',
    name: 'OrderPage', 
    component: OrderPage 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
