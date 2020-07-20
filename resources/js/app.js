import router from './router';
import api from './api';
import './prototype';

require('./bootstrap');

window.Vue = require('vue');
window.api = api;

const app = new Vue({
    el: '#app',
    router
});
